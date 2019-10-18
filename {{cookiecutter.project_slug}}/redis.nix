{ bind }:
{
  enable = true;
  inherit bind;
  appendOnly = true;
  extraConfig = ''
    maxclients 4000
  '';
}
