{ pkgs, pyPackages, buildPythonPackage }:

with pkgs;
with pyPackages;

buildPythonPackage rec {
  pname = "MowitiGIS";
  version = "0.0.1";

  django = django_2_2;

  src = ../MowitiGIS;
  doCheck = false;
  "django-leaflet" = buildPythonPackage {
    name = "django-leaflet-0.24.0";
    doCheck = false;
    propagatedBuildInputs = [
      django
    ];
    src = builtins.fetchurl {
      url = "https://files.pythonhosted.org/packages/86/44/869968fdef933502a5268ef7ea695b5fb3f26902df4145235342a4da3ae8/django-leaflet-0.24.0.tar.gz";
      sha256 = "0yqicvmcqmzqhf86ldj0hcvmhsnwf2w21syw1xg1qbxm1fp9ipzg";
    };
  };
  "django-chartjs" = buildPythonPackage {
    name = "django-chartjs-1.5.0";
    doCheck = false;
    propagatedBuildInputs = [
      django six
    ];
    src = builtins.fetchurl {
      url = "https://files.pythonhosted.org/packages/3d/b0/1a9972f01f83f4f6471279c2f707bd3e36c1ad3697205dc9b4a5f539ec45/django-chartjs-1.5.0.tar.gz";
      sha256 = "68bab8cac770afc9b586db59f01295e9bf55198ec58557ca24acd20c0fea7500";
    };
  };
  "django-colorful" = buildPythonPackage {
    name = "django-colorful-1.3";
    doCheck = false;
    propagatedBuildInputs = [
      django
    ];
    src = builtins.fetchurl {
      url = "https://files.pythonhosted.org/packages/b7/9f/3e19b35b6d85ec5b6cffde8533b6a0fca5d435b278c6537428c32e1ab6b5/django-colorful-1.3.tar.gz";
      sha256 = "fd246f2fb297ed074dc4349966d33a1c82d0308b7fb0d6ef6e2e76b90cefffb7";
    }; 
  };

  propagatedBuildInputs = [ django django-leaflet django-configurations django-chartjs django-colorful gdal geos postgresql_11 postgresql_11.pkgs.postgis pillow psycopg2 pytz sqlparse ];
}

