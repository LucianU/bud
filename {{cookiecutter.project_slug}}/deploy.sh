#!/usr/bin/env bash

set -euxo pipefail

TARGET="nixos@108.61.117.242"

STATIC_DIR="${PWD}/{{cookiecutter.project_slug}}/static_all"

NIX_SSHOPTS="-o IdentityFile=~/.ssh/id_rsa_nixos"

if [ ! -d "$STATIC_DIR" ];
then
  nix-shell --pure --run "source .env; ./manage.py collectstatic --no-input"
fi

PROFILE_PATH="$(nix-build --no-out-link -A system ./nix/prod-system.nix)"
nix-copy-closure --to --use-substitutes $TARGET $PROFILE_PATH
ssh $TARGET -- "sudo nix-env --profile /nix/var/nix/profiles/system --set $PROFILE_PATH && sudo /nix/var/nix/profiles/system/bin/switch-to-configuration switch"
