var centru = new L.LatLng(45.2, 29.2);
var osm = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
var greyscale = L.tileLayer('http://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png');
var mqi = L.tileLayer('http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}');


// ******************  DEFINIRE MARKERI ************** //
// Creaza un marker pentru asezarea pescareasca
var pescarMarker = L.ExtraMarkers.icon({
    icon: 'fa-flag',
    markerColor: 'orange',
    shape: 'star',
    prefix: 'fa'
});
// Creaza un marker pentru pensiune
var pensiuneMarker = L.ExtraMarkers.icon({
    icon: 'fa-bed',
    markerColor: 'purple',
    shape: 'square',
    prefix: 'fa'
});
// Creaza un marker pentru localitate
var localitateMarker = L.ExtraMarkers.icon({
    icon: 'fa-circle',
    markerColor: 'yellow',
    shape: 'circle',
    prefix: 'fa'
});
// Creaza un marker pentru loc de pescuit
var locDePescuitMarker = L.ExtraMarkers.icon({
    icon: 'fa-trophy',
    markerColor: 'green',
    shape: 'circle',
    prefix: 'fa'
});
// Creaza un marker pentru colonie de pasari
var coloniePasariMarker = L.ExtraMarkers.icon({
    icon: 'fa-binoculars',
    markerColor: 'green',
    shape: 'circle',
    prefix: 'fa'
});
// Creaza un marker pentru canal colmatat
var colmatatMarker = L.ExtraMarkers.icon({
    icon: 'fa-minus-circle',
    markerColor: 'red',
    shape: 'penta',
    prefix: 'fa'
});
// Creaza un marker pentru apa scazuta
var apaScazutaMarker = L.ExtraMarkers.icon({
    icon: 'fa-exclamation-circle',
    markerColor: 'red',
    shape: 'penta',
    prefix: 'fa'
});
// Creaza un marker pentru arbori cazuti
var arboreCazutMarker = L.ExtraMarkers.icon({
    icon: 'fa-tree',
    markerColor: 'red',
    shape: 'penta',
    prefix: 'fa'
});
// Creaza un marker pentru vegetatie abundenta
var vegetatieMarker = L.ExtraMarkers.icon({
    icon: 'fa-leaf',
    markerColor: 'red',
    shape: 'penta',
    prefix: 'fa'
});
// Creaza un marker pentru punct de lansare
var lansareMarker = L.ExtraMarkers.icon({
    icon: 'fa-ship',
    markerColor: 'yellow',
    shape: 'circle',
    prefix: 'fa'
});
// Creaza un marker pentru camping
var campingMarker = L.ExtraMarkers.icon({
    icon: 'fa-fire',
    markerColor: 'purple',
    shape: 'square',
    prefix: 'fa'
});

function addStartPosition(e) {
    alert(e.latlng);
}

function addEndPosition(e) {
    alert(e.latlng);
}

function showCoordinates(e) {
    alert(e.latlng);
}

function centerMap(e) {
    map.panTo(e.latlng);
}

function zoomIn(e) {
    map.zoomIn();
}

function zoomOut(e) {
    map.zoomOut();
}

map = L.map('map', {
    center: centru,
    zoom: 10,
    layers: mqi,
    contextmenu: true,
    contextmenuWidth: 140,
    contextmenuItems: [
        {
            text: 'Start from here',
            icon: 'static/images/start-mk.png',
            callback: addStartPosition
        }, {
            text: 'End here',
            icon: 'static/images/finish-mk.png',
            callback: addEndPosition
        },
        {
            text: 'Show coordinates',
            callback: showCoordinates
        }, {
            text: 'Center map here',
            callback: centerMap
        }, '-', {
            text: 'Zoom in',
            icon: 'static/images/zoom-in.png',
            callback: zoomIn
        }, {
            text: 'Zoom out',
            icon: 'static/images/zoom-out.png',
            callback: zoomOut
        }],

});

/*map.on('mousemove', function(e) {
    alert("Lat, Lon : " + e.latlng.lat + ", " + e.latlng.lng)
});*/
//map.removeControl(map.zoomControl);

L.Control.geocoder().addTo(map);

// adauga toate punctele de interes
/*var PunctInteres = new L.GeoJSON.AJAX("poi_data", {
    onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.name.toString());
        layer.bindContextMenu({
            contextmenu: true,
            contextmenuItems: [{
                text: 'Marker item'
            }]
        });
    }
});*/
// adauga asezarile pescaresti
var AsezariPOI = new L.GeoJSON.AJAX("asezari_data", {
    onEachFeature: function (feature, layer) {
        layer.bindPopup("<h4>" + feature.properties.name.toString() + "</h4><img src=" + "media/" + feature.properties.image + " class='img-fluid'/><strong> Nr. de telefon </strong> " + feature.properties.telephone.toString());
        layer.setIcon(pescarMarker)
    }
});


// adauga pensiunile
var PensiuniPOI = new L.GeoJSON.AJAX("pensiuni_data", {
    onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.name.toString());
        layer.setIcon(pensiuneMarker)
    }
});
// adauga arborii cazuti
var ArboriPOI = new L.GeoJSON.AJAX("arbori_data", {
    onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.name.toString());
        layer.setIcon(arboreCazutMarker)
    }
});
// adauga localitate
var LocalitatePOI = new L.GeoJSON.AJAX("localitate_data", {
    onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.name.toString());
        layer.setIcon(localitateMarker)
    }
});
// adauga zona de pescuit
var PescuitPOI = new L.GeoJSON.AJAX("pescuit_data", {
    onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.name.toString());
        layer.setIcon(locDePescuitMarker)
    }
});
// adauga colonii de pasari
var ColoniePOI = new L.GeoJSON.AJAX("colonie_data", {
    onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.name.toString());
        layer.setIcon(coloniePasariMarker)
    }
});
// adauga zona cu apa scazuta
var ApaScazutaPOI = new L.GeoJSON.AJAX("apascazuta_data", {
    onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.name.toString());
        layer.setIcon(apaScazutaMarker)
    }
});
// adauga zona cu vegetatie abundenta
var VegetatiePOI = new L.GeoJSON.AJAX("vegetatie_data", {
    onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.name.toString());
        layer.setIcon(vegetatieMarker)
    }
});
// adauga puncte de lansare
var PuncteLansarePOI = new L.GeoJSON.AJAX("punctlansare_data", {
    onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.name.toString());
        layer.setIcon(lansareMarker)
    }
});
// adauga camping
var CampingPOI = new L.GeoJSON.AJAX("camping_data", {
    onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.name.toString());
        layer.setIcon(campingMarker)
    }
});
// adauga canal colmatat
var ColmatatPOI = new L.GeoJSON.AJAX("colmatat_data", {
    onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.name.toString());
        layer.setIcon(colmatatMarker)
    }
});
// adauga arii protejate
var ProtejatZone = new L.GeoJSON.AJAX("ariiprotejate_data", {
    style: {fillColor: '#ff0000', fillOpacity: 0.6, color: "#9b0000"},
    onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.name.toString());

    }
});
// adauga grinduri
var GrinduriZone = new L.GeoJSON.AJAX("grinduri_data", {
    style: {fillColor: '#ffe100', fillOpacity: 0.6, color: "#ffae00"},
    onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.name.toString());

    }
});
// adauga paduri
var PaduriZone = new L.GeoJSON.AJAX("paduri_data", {
    style: {color: '#2f7200', fillOpacity: 0.7},
    onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.name.toString());

    }
});
// adauga canalele editate din fisierul SHP
var Canale = new L.GeoJSON.AJAX("canale", {
    style: function colors(feature) {
        if (feature.properties.name !== '') {
            return {
                color: 'orange'
            }
        }
    },
    onEachFeature: function (feature, layer) {
        layer.bindPopup(feature.properties.name.toString());

    }
});
/*PunctInteres.addTo(map);
AsezariPOI.addTo(map);
PensiuniPOI.addTo(map);
Canale.addTo(map);*/


var baseLayers = {
    "Satelite": mqi,
    "OSM": osm,
    "Greyscale": greyscale
};
var groupedOverlays = {
    "Zone importante": {
        "Canale": Canale,
        "Grinduri": GrinduriZone,
        "Paduri": PaduriZone,
        "Zone strict protejate": ProtejatZone,
        "Localități": LocalitatePOI,
    },
    "Puncte de interes": {
        "Așezări pescărești": AsezariPOI,
        "Pensiuni": PensiuniPOI,
        "Camping": CampingPOI,
        "Puncte de lansare": PuncteLansarePOI,
    },
    "Divertisment": {
        "Colonii de păsări": ColoniePOI,
        "Locuri de pescuit": PescuitPOI
    },
    "Obstacole": {
        "Vegetație abundentă": VegetatiePOI,
        "Canal Colmatat": ColmatatPOI,
        "Apă scăzută": ApaScazutaPOI,
        "Blocaj arbori": ArboriPOI,
    }
};
var options = {
    // Make the "Landmarks" group exclusive (use radio inputs)
    exclusiveGroups: ["Landmarks"],
    // Show a checkbox next to non-exclusive group labels for toggling all
    groupCheckboxes: true
};

// L.control.groupedLayers(baseLayers, groupedOverlays, options).addTo(map);

var layerControl = L.control.groupedLayers(baseLayers, groupedOverlays, options);
map.addControl(layerControl);

//L.control.zoom({position: 'topleft'}).addTo(map);
//   map.on('click', function (e) {
//       var marker = new L.marker(e.latlng).addTo(map);
//
//
//       function addMarker(e) {
//           // Add marker to map at click location; add popup window
//           var newMarker = new L.marker(e.latlng).addTo(map);
//
//       }
//   });


/* ********** ROUTING CONTROL *************** */
/*window.lrmConfig = {
//    serviceUrl: 'https://api.mapbox.com/directions/v5',
//    profile: 'mapbox/driving',
};*/
/*function createButton(label, container) {
    var btn = L.DomUtil.create('button', '', container);
    btn.setAttribute('type', 'button');
    btn.innerHTML = label;
    return btn;
}




var control = L.Routing.control({
/!*waypoints: [
		L.latLng(45.16, 28.62),
		L.latLng(45.11, 28.85)
	],*!/
   	geocoder: L.Control.Geocoder.nominatim(),
	routeWhileDragging: true,
	reverseWaypoints: true,
	showAlternatives: true,
	altLineOptions: {
		styles: [
			{color: 'black', opacity: 0.15, weight: 9},
			{color: 'white', opacity: 0.8, weight: 6},
			{color: 'blue', opacity: 0.5, weight: 2}
		]
	}
}).addTo(map);

L.Routing.errorControl(control).addTo(map);


map.on('click', function(e) {
    var container = L.DomUtil.create('div'),
        startBtn = createButton('Pleacă din poziția asta', container),
        destBtn = createButton('Ajungi la poziția asta', container);

    L.popup()
        .setContent(container)
        .setLatLng(e.latlng)
        .openOn(map);
                L.DomEvent.on(startBtn, 'click', function() {
        control.spliceWaypoints(0, 1, e.latlng);
        map.closePopup();
    });



    L.DomEvent.on(destBtn, 'click', function() {
        control.spliceWaypoints(control.getWaypoints().length - 1, 1, e.latlng);
        map.closePopup();
    });



});

var ReversablePlan = L.Routing.Plan.extend({
    createGeocoders: function() {
        var container = L.Routing.Plan.prototype.createGeocoders.call(this),
            reverseButton = createButton('↑↓', container);
        return container;
    }
});*/

/* ******************END ROUTING CODE **************************** */

// L.control.groupedLayers = L.Control.extend();


/*   function onLocationFound(e) {
       var radius = e.accuracy / 2;

       L.marker(e.latlng).addTo(map).bindPopup("You are within " + radius + " meters from this point").openPopup();

       L.circle(e.latlng, radius).addTo(map);
   }

   function onLocationError(e) {
       alert(e.message);
   }

   map.on('locationfound', onLocationFound);
   map.on('locationerror', onLocationError);

   map.locate({setView: true, maxZoom: 16});*/
var sidebar = L.control.sidebar('sidebar', {position: 'left'}).addTo(map);
//console.log(map);
//  console.log(options);


$(document).ready(function () {
    $('#nav-planificator-tab').click(function (e) {
        e.preventDefault();
        $.ajax({
            type: "GET",
            url: "ture",
            data: {},
            success: function (data) {
                $('#nav-planificator').html(data);
            }
        });
    });

    $("[data-toggle=popover]").each(function (i, obj) {

        $(this).popover({
            html: true,
            content: function () {
                var id = $(this).attr('id')
                return $('#popover-content-' + id).html();
            }
        });

    });

    $('#radioBtn a').on('click', function () {
        var sel = $(this).data('title');
        var tog = $(this).data('toggle');
        $('#' + tog).prop('value', sel);

        $('a[data-toggle="' + tog + '"]').not('[data-title="' + sel + '"]').removeClass('active').addClass('notActive');
        $('a[data-toggle="' + tog + '"][data-title="' + sel + '"]').removeClass('notActive').addClass('active');
    });


$(document).on('change', '#scara_harta', function() {
  // Does some stuff and logs the event to the console
    var scara = L.control.scale({metric:false, imperial:true});
            if ($(this).prop('checked')){
                console.log("on");
                 scara.addTo(map);
            }
            else{
                console.log("off");
                L.control.scara.remove();
            }
});

   /* $('#scara_harta').change(function() {


    });*/




});
var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
navigator.geolocation.getCurrentPosition(function (location) {
    var latlng = new L.LatLng(location.coords.latitude, location.coords.longitude);
    var lat = location.coords.latitude;
    var long = location.coords.longitude;

    $(document).on('click', '#asezari_btn', function () {
        console.log("click");
        L.marker(latlng, {icon: pescarMarker}).addTo(map).bindPopup('Ai adaugat o asezare pescarească aici. ' +
            '<button type="button" class="btn btn-warning" data-spoi="pescar" data-poi = "așezare pescărească" data-latlng="' + latlng + '" >Salvezi?</button>').openPopup();
    });
    $(document).on('click', '#lansare_btn', function () {
        console.log("click");
        L.marker(latlng, {icon: lansareMarker}).addTo(map).bindPopup("Ai adaugat un loc de lansare aici. " +
            '<button type="button" class="btn btn-warning" data-poi = "lansare" >Salvezi?</button>').openPopup();
    });
    $(document).on('click', '#camping_btn', function () {
        console.log("click");
        L.marker(latlng, {icon: campingMarker}).addTo(map).bindPopup("Ai adaugat un loc de campare aici. " +
            '<button type="button" class="btn btn-warning" data-poi = "camping" data-latlng="' + latlng + '" >Salvezi?</button>').openPopup();
    });
    $(document).on('click', '#colonii_btn', function () {
        console.log("click");
        L.marker(latlng, {icon: coloniePasariMarker}).addTo(map).bindPopup("Ai adaugat o colonie de păsări aici. " +
            '<button type="button" class="btn btn-warning" data-poi = "colonie" >Salvezi?</button>').openPopup();
    });
    $(document).on('click', '#pescuit_btn', function () {
        console.log("click");
        L.marker(latlng, {icon: locDePescuitMarker}).addTo(map).bindPopup("Ai adaugat un loc de pescuit aici. " +
            '<button type="button" class="btn btn-warning" data-poi = "locpescuit" >Salvezi?</button>').openPopup();
    });
    $(document).on('click', '#vegetatie_btn', function () {
        console.log("click");
        L.marker(latlng, {icon: vegetatieMarker}).addTo(map).bindPopup("Ai adaugat un marcaj de vegetație abundenta aici. " +
            '<button type="button" class="btn btn-warning" data-poi = "vegetatie" >Salvezi?</button>').openPopup();
    });
    $(document).on('click', '#colmatat_btn', function () {
        console.log("click");
        L.marker(latlng, {icon: colmatatMarker}).addTo(map).bindPopup("Ai adaugat o zonă colmatată aici. " +
            '<button type="button" class="btn btn-warning" data-poi = "colmatat" >Salvezi?</button>').openPopup();
    });
    $(document).on('click', '#apascazuta_btn', function () {
        console.log("click");
        L.marker(latlng, {icon: apaScazutaMarker}).addTo(map).bindPopup("Ai adaugat un loc cu apa scazută aici. " +
            '<button type="button" class="btn btn-warning" data-poi = "apascazuta" >Salvezi?</button>').openPopup();
    });
    $(document).on('click', '#blocaj_btn', function () {
        console.log("click");
        L.marker(latlng, {icon: arboreCazutMarker}).addTo(map).bindPopup("Ai adaugat o zona blocată de arbori aici. " +
            '<button type="button" class="btn btn-warning" data-poi = "blocaj" >Salvezi?</button>').openPopup();
    });

    $(document).on("click", '[data-poi=camping]', function () {
        var latlong = $(this).attr("data-latlng");
        var tippoi = $(this).attr("data-poi");
        console.log("Salvezi " + tippoi + " in locatia: " + latlong)
        console.log("lat: ", lat);
        console.log("long: ", long)
        $.ajax({
            type: 'POST',
            url: 'pois/create/',
            cache: 'false',
            dataType: 'json',
            data: {
                location: latlong,
                lat:lat,
                long:long,
                poi_type: tippoi,
            },
            success: function () {
                console.log("success");
            }

        });
    });


});