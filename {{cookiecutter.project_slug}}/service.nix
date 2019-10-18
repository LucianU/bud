{ config, lib, pkgs, ... }:

let
  pyPackages = pkgs.python37Packages;
  {{cookiecutter.project_slug}} = import ./default.nix;
  cfg = config.services.{{cookiecutter.project_slug}};
  {{cookiecutter.project_slug}}env = pkgs.writeText "{{cookiecutter.project_slug}}-env" ''
    PYTHONPATH="${ {{cookiecutter.project_slug}} }/lib/python3.7/site-packages/"
    DJANGO_SETTINGS_MODULE="{{cookiecutter.project_slug}}.settings"
    DJANGO_CONFIGURATION="Dev"
    DJANGO_SECRET_KEY="*8e+^@x8rs%4jp1blufis93um_1a=k%(63p%6i*6o((6xr6^5@"
    DJANGO_GDAL_LIBRARY_PATH="${pkgs.gdal}/lib/libgdal.so"
    DJANGO_GEOS_LIBRARY_PATH="${pkgs.geos}/lib/libgeos_c.so"
  '';
in {
  options.services.{{cookiecutter.project_slug}}.enable = lib.mkEnableOption "{{cookiecutter.project_slug}}";
  options.services.{{cookiecutter.project_slug}}.port = lib.mkOption {
    default = 8000;
    type = lib.types.int;
  };

  config = lib.mkIf cfg.enable {
    networking.firewall.allowedTCPPorts = [ cfg.port ];

    systemd.services.{{cookiecutter.project_slug}} = {
      description = "{{cookiecutter.project_slug}}";
      after = [ "network.target" "postgresql.target" "redis.target" ];
      wantedBy = [ "multi-user.target" ];
      serviceConfig = {
        User = "vagrant";
        EnvironmentFile = "${ {{cookiecutter.project_slug}}env}";
        ExecStart = "${pyPackages.gunicorn}/bin/gunicorn {{cookiecutter.project_slug}}.wsgi -b 0.0.0.0:${toString cfg.port}";
        Restart = "always";
        KillMode = "process";
      };
      preStart = ''
        source ${ {{cookiecutter.project_slug}}env}
        ${ {{cookiecutter.project_slug}} }/bin/manage.py collectstatic --no-input
        ${ {{cookiecutter.project_slug}} }/bin/manage.py migrate
      '';
    };
  };
}
