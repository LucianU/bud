{ config, pkgs, ... }:
let
  postgres = import /{{cookiecutter.project_slug}}/postgres.nix;
  redis = import /{{cookiecutter.project_slug}}/redis.nix;
in
{
  imports = [
    /etc/nixos/vagrant.nix
  ];

  fileSystems."/{{cookiecutter.project_slug}}" = {
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
