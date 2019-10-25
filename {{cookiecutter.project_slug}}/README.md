# About
{{cookiecutter.project_slug}} is a project .....

## With Nix
- Install [Vagrant](https://www.vagrantup.com/docs/installation/) and [Nix
](https://nixos.org/nix/download.html).
- In the project, run `vagrant up` 
- Once the machine is ready, login with `vagrant ssh`.
- Go to the shared folder: `cd /{{cookiecutter.project_slug}}`.
- Enter the nix-shell. Run `nix-shell`.
- Start the development server: `./runserver.sh`
