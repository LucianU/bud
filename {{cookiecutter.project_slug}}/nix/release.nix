with import ./nixpkgs.nix;

let
  {{cookiecutter.project_slug}} = pkgs.callPackage ./package.nix {
    inherit pkgs;
    pyPackages = python37Packages;
  };
  {{cookiecutter.project_slug}}-dev = python37.withPackages (pkgs: [
    {{cookiecutter.project_slug}}
    pkgs.black
    pkgs.flake8
    pkgs.pip
  ]);
  {{cookiecutter.project_slug}}-prod = python37.withPackages (_: [
    {{cookiecutter.project_slug}}
  ]);
in
  { devel = {{cookiecutter.project_slug}}-dev;
    prod = {{cookiecutter.project_slug}}-prod;
  }
