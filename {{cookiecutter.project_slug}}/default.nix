with import ./nixpkgs.nix;

let
  {{cookiecutter.project_slug}} = pkgs.callPackage ./project.nix {
    inherit pkgs;
    pyPackages = python37Packages;
    buildPythonPackage = python37Packages.buildPythonPackage;
  };
in
  python37.withPackages (_: [ {{cookiecutter.project_slug}} ])
