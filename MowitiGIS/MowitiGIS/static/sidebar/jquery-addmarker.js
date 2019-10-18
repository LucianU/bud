/**
 * Create a new sidebar on this jQuery object.
 *
 * @example
 * var sidebar = $('#sidebar').sidebar();
 *
 * @param {Object} [options] - Optional options object
 * @param {string} [options.position=left] - Position of the sidebar: 'left' or 'right'
 * @returns {jQuery}
 */
$.fn.add_poi = function(options) {
    var add_poi = this;
    var $tabs = add_poi.find('ul.sidebar-tabs, .sidebar-tabs > ul');
    var $container = add_poi.children('.sidebar-content').first();

    options = $.extend({
        position: 'left'
    }, options || {});

    add_poi.addClass('sidebar-' + options.position);

    $tabs.children('li').children('a[href^="#"]').on('click', function(e) {
        e.preventDefault();
        var $tab = $(this).closest('li');

        if ($tab.hasClass('active'))
            add_poi.close();
        else if (!$tab.hasClass('disabled'))
            add_poi.open(this.hash.slice(1), $tab);
    });

    add_poi.find('.sidebar-close').on('click', function() {
        add_poi.close();
    });

    /**
     * Open sidebar (if necessary) and show the specified tab.
     *
     * @param {string} id - The id of the tab to show (without the # character)
     * @param {jQuery} [$tab] - The jQuery object representing the tab node (used internally for efficiency)
     */
    add_poi.open = function(id, $tab) {
        if (typeof $tab === 'undefined')
            $tab = $tabs.find('li > a[href="#' + id + '"]').parent();

        // hide old active contents
        $container.children('.sidebar-pane.active').removeClass('active');

        // show new content
        $container.children('#' + id).addClass('active');

        // remove old active highlights
        $tabs.children('li.active').removeClass('active');

        // set new highlight
        $tab.addClass('active');

        add_poi.trigger('content', { 'id': id });

        if (add_poi.hasClass('collapsed')) {
            // open sidebar
            add_poi.trigger('opening');
            add_poi.removeClass('collapsed');
        }
    };

    /**
     * Close the sidebar (if necessary).
     */
    add_poi.close = function() {
        // remove old active highlights
        $tabs.children('li.active').removeClass('active');

        if (!add_poi.hasClass('collapsed')) {
            // close sidebar
            add_poi.trigger('closing');
            add_poi.addClass('collapsed');
        }
    };

    return add_poi;
};
