with import ./nixpkgs.nix;

let
  mowitigis = pkgs.callPackage ./project.nix {
    inherit pkgs;
    pyPackages = python37Packages;
    buildPythonPackage = python37Packages.buildPythonPackage;
  };
in
  python37.withPackages (_: [ mowitigis ])
