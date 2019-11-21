{ user, database, pkgs }:
  let initScript = ''
          CREATE USER ${user};
          CREATE DATABASE ${database};
          GRANT ALL PRIVILEGES ON DATABASE ${database} TO ${user};
          ALTER DATABASE ${database} OWNER TO ${user};
          \c ${database}
          CREATE EXTENSION IF NOT EXISTS postgis;
          CREATE EXTENSION IF NOT EXISTS btree_gist;
      '';
  in
    {
      enable = true;
      package = pkgs.postgresql_11;
      extraPlugins = with pkgs.postgresql_11.pkgs; [ postgis ];
      initialScript = pkgs.writeText "backend-initScript" initScript;
    }
