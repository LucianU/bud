let
  {{cookiecutter.project_slug}} = import ./default.nix;
in
  {{cookiecutter.project_slug}}.env
