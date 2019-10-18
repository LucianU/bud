{ config, lib, pkgs, ... }:

let
  pyPackages = pkgs.python37Packages;
  mowitigis = import ./default.nix;
  cfg = config.services.mowitigis;
  mowitigisenv = pkgs.writeText "mowitigis-env" ''
    PYTHONPATH="${mowitigis}/lib/python3.7/site-packages/"
    DJANGO_SETTINGS_MODULE="MowitiGIS.settings"
    DJANGO_CONFIGURATION="Dev"
    DJANGO_SECRET_KEY="*8e+^@x8rs%4jp1blufis93um_1a=k%(63p%6i*6o((6xr6^5@"
    DJANGO_GDAL_LIBRARY_PATH="${pkgs.gdal}/lib/libgdal.so"
    DJANGO_GEOS_LIBRARY_PATH="${pkgs.geos}/lib/libgeos_c.so"
  '';
in {
  options.services.mowitigis.enable = lib.mkEnableOption "MowitiGIS";
  options.services.mowitigis.port = lib.mkOption {
    default = 8000;
    type = lib.types.int;
  };

  config = lib.mkIf cfg.enable {
    networking.firewall.allowedTCPPorts = [ cfg.port ];

    systemd.services.mowitigis = {
      description = "MowitiGIS";
      after = [ "network.target" "postgresql.target" "redis.target" ];
      wantedBy = [ "multi-user.target" ];
      serviceConfig = {
        User = "vagrant";
        EnvironmentFile = "${mowitigisenv}";
        ExecStart = "${pyPackages.gunicorn}/bin/gunicorn MowitiGIS.wsgi -b 0.0.0.0:${toString cfg.port}";
        Restart = "always";
        KillMode = "process";
      };
      preStart = ''
        source ${mowitigisenv}
        ${mowitigis}/bin/manage.py collectstatic --no-input
        ${mowitigis}/bin/manage.py migrate
      '';
    };
  };
}
