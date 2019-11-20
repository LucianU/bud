# Edit this configuration file to define what should be installed on
# your system.  Help is available in the configuration.nix(5) man page
# and in the NixOS manual (accessible by running ‘nixos-help’).

{ config, pkgs, ... }:
let
  postgres = import ./services/postgres.nix;
in
{
  imports =
    [ # Include the results of the hardware scan.
      ./hardware-configuration.nix
      ./service.nix
    ];

  # Use the GRUB 2 boot loader.
  boot.loader.grub.enable = true;
  boot.loader.grub.version = 2;
  boot.loader.grub.device = "/dev/vda"; # or "nodev" for efi only

  # networking.hostName = "nixos"; # Define your hostname.
  # networking.wireless.enable = true;  # Enables wireless support via wpa_supplicant.

  # Configure network proxy if necessary
  # networking.proxy.default = "http://user:password@proxy:port/";
  # networking.proxy.noProxy = "127.0.0.1,localhost,internal.domain";

  # Select internationalisation properties.
  # i18n = {
  #   consoleFont = "Lat2-Terminus16";
  #   consoleKeyMap = "us";
  #   defaultLocale = "en_US.UTF-8";
  # };

  # Set your time zone.
  # time.timeZone = "Europe/Amsterdam";

  # List packages installed in system profile. To search, run:
  # $ nix search wget
  environment.systemPackages = with pkgs; [
    vim
  ];

  # List services that you want to enable:

  # Enable the OpenSSH daemon.
  services.openssh.enable = true;
  services.openssh.permitRootLogin = "no";
  services.openssh.passwordAuthentication = false;

  # Open ports in the firewall.
  networking.firewall.allowedTCPPorts = [ 443 ];

  # Define a user account. Don't forget to set a password with ‘passwd’.
  users.users.nixos = {
    isNormalUser = true;
    uid = 1000;
    useDefaultShell = true;
    extraGroups = [ "wheel" ];
    openssh.authorizedKeys.keys = [ "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDmwaAp4qlc4HCE4TEmJE+F1iH7Chbk390JzFo7l+TPdGgR+12l45AO9HI4SAhB6/lxHDJ1yT/Aj/lHV4exvRt97M14leT6FQIEiQ1hnezaz/NxZqFP1RBuqqGzjRohdE7IFSv+/RV9ZGfK639c4BZg2p/eAtXG1DYUwIlDH740w1mBO0k+Wu935T7swYaiSiP9znQvO8QdrZcE1crnqshgcMbQVYIlVYmssAEJtdJZjb7GhPIWj9omIKgbWX2p5tnv0xFk6eH9DbCuwg+dK9aENduTj+Ce223wJZetPzcy4WXo5OnULRwc1xg/pZFMbdLjS9DUtRXPFU/cr9apAClMUG8JMKJ3vjgAumbWG9FYQdKn25EfPVbuy5RyF1YEsyNhyHxYLbzU7h3Ge9/hJS4eKkzkSOFLw9XypeRJ8fZwvLn1BNYFEMJgiR4oGmuSYx/797XumWUZoMdU/9K7D1QXu0juRs3hgLDGhQnLu5qtWdBXtGPn/+JbEPmrmw8vsPvRG9ldZCWzeYEA/9MHhJxQuufmmtruVnu222PnCoAaEtvaMOqqypV3swSr7KNak/eUGfEsXTWvVYA3z/+08sksS3V0hEcqBZ0vVcWUKcB+ujCECt/7e50CUVRYlZvBVuo7ZrsVbFiVZVMCXFRlAKl9zdfWwTfjYmiXWy5WPXGNcQ== nixos-box" ];
  };

  users.mutableUsers = false;

  security.sudo.wheelNeedsPassword = false;

  # Services
  services.{{cookiecutter.project_slug}}.enable = true;

  services.postgresql = postgres {
    user = "nixos";
    database = "nixos";
    inherit pkgs;
  };

  services.nginx = {
    enable = true;
    recommendedGzipSettings = true;
    recommendedOptimisation = true;
    recommendedProxySettings = true;

    virtualHosts."map.mowiti.com" = {
      forceSSL = true;
      enableACME = true;
      locations = {
        "/" = {
          proxyPass = "http://127.0.0.1:8000/";
        };
        "/static" = {
          alias = "${config.services.{{cookiecutter.project_slug}}.package.static}";
        };
      };
    };
  };

  nix.trustedUsers = [ "root" "@wheel" ];

  # This value determines the NixOS release with which your system is to be
  # compatible, in order to avoid breaking some software such as database
  # servers. You should change this only after NixOS release notes say you
  # should.
  system.stateVersion = "19.03"; # Did you read the comment?
}
