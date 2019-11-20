let
  {{cookiecutter.project_slug}} = import ./release.nix;
in
  {{cookiecutter.project_slug}}.devel.env
