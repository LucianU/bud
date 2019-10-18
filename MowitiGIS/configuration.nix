{ config, pkgs, ... }:
let
  postgres = import /MowitiGIS/postgres.nix;
  redis = import /MowitiGIS/redis.nix;
in
{
  imports = [
    /etc/nixos/vagrant.nix
  ];

  fileSystems."/MowitiGIS" = {
    fsType = "vboxsf";
    device = "Temp";
    options = [ "rw" ];
  };

  services.postgresql = postgres {
    user = "vagrant";
    database = "vagrant";
    inherit pkgs;
  };

  services.redis = redis {
    bind = "127.0.0.1";
  };

  environment.systemPackages = [ pkgs.git pkgs.vim ];
}
