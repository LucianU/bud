with import ./nixpkgs.nix;

let
  {{cookiecutter.project_slug}} = pkgs.callPackage ./package.nix {
    inherit pkgs;
    pyPackages = python37Packages;
  };
in
  python37.withPackages (_: [ {{cookiecutter.project_slug}} ])
