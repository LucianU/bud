let
  nixpkgs = builtins.fetchTarball {
     name = "nixos-19.03";
     url = "https://github.com/nixos/nixpkgs/archive/67135fbcc5d5d28390c127ef519b09a362ef2466.tar.gz";
     sha256 = "00591607zmn1hfjs4959ksh164b0gjqwkvbrc4anx6da8xmhfcc2" ;
  };

in
  import "${nixpkgs}/nixos" {
    configuration = {
      imports = [
        ./prod-config.nix
      ];
    };

    system = "x86_64-linux";
  }
