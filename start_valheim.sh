#!/bin/bash
export LD_LIBRARY_PATH=./linux64:$LD_LIBRARY_PATH
export SteamAppId=892970

# Validate vars
if [ -z "$NAME" ] || [ -z "$WORLD" ] || [ -z "$PASSWORD" ]; then
    echo "NAME, WORLD, and PASSWORD must all be configured in /etc/sysconfig/valheim"
    exit 1
fi

/valheim/update.sh  # Will fail and exit if issue during update

echo "Starting Valheim server"

# NOTE: Minimum password length is 5 characters & Password cant be in the server name.
# NOTE: You need to make sure the ports 2456-2458 is being forwarded to your server through your local router & firewall.

# TODO: Move name, world, and password into environment variables.
./valheim_server.x86_64 -name "$NAME" -port 2456 -world "$WORLD" -password "$PASSWORD" &

echo $! > /var/run/valheim/valheim.pid

while ! lsof -Pn -p $(cat /var/run/valheim/valheim.pid) | grep :2457; do
  echo "Waiting for Valheim server to start..."
  sleep 1
done

echo "Valheim server started"
