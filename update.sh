#!/bin/bash
if [[ ! -f /run/valheim/valheim.pid ]]; then
    echo "Checking for Valheim updates from Steam. This will take a few moments..."

    # TODO: make all this shit better

    # Download steamcmd
    steamcmd=$(mktemp -d)
    curl -sqL "https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" --output "${steamcmd}/steamcmd_linux.tar.gz"
    tar xf "${steamcmd}/steamcmd_linux.tar.gz" -C "${steamcmd}"

    if [[ ! -f "${steamcmd}/steamcmd.sh" ]]; then
        echo "Failure fetching steamcmd to update Valheim."
        exit 1
    fi
    # Perform update
    "${steamcmd}/steamcmd.sh" +login anonymous +force_install_dir /valheim/Game +app_update 896660 validate +exit | grep 'Success!'
    result=$?

    # Cleanup steamcmd no matter wut
    rm -r "${steamcmd}"

    if [ $result -ne 0 ]; then
        echo "Failure when running updates for Valheim."
        exit 1
    fi
else
  echo "Valheim server is running. Skipping update check."
fi
