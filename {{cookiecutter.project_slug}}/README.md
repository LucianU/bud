# About
{{cookiecutter.project_slug}} is a project .....

## With Nix
- Install [Vagrant](https://www.vagrantup.com/docs/installation/) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads) 
- In the project, run `vagrant up` 
- Once the machine is ready, login with `vagrant ssh`.
- Go to the shared folder: `cd /{{cookiecutter.project_slug}}`.
- Enter the nix-shell. Run `nix-shell nix/shell.nix`.
- Start the development server: `./runserver.sh`

- To exit shell run `exit`
- To exit the machine run `exit`
- To suspend the machine run `vagrant suspend`. This will save the state of the machine.
- To regenerate the machine run `vagrant provision`
- To delete the machine run `vagrant destroy`
