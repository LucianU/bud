# About
MowitiGIS is a project aimed to show you routes through the Danube Delta.

# Setup
## With Docker
- Install Docker and docker-compose.
- Create an .env file from .env.example: `cp .env.example .env`
- Generate a secret key and put it in the .env file.
- Go inside the project and run `docker-compose up`.
- If it's the first time you setup the project locally, you need to run the
 migrations (open another tab to run the command):
 
        docker-compose run web python3 manage.py migrate
- You should be able to access the site at http://0.0.0.0:8000

## With Nix
- Install [Vagrant](https://www.vagrantup.com/docs/installation/) and [Nix
](https://nixos.org/nix/download.html).
- In the project, run `vagrant up` 
- Once the machine is ready, login with `vagrant ssh`.
- Go to the shared folder: `cd /mowitigis`.
- Enter the nix-shell. Run `nix-shell`.
- Start the development server: `./runserver.sh`
