#!/bin/bash

# Validate vars
if [ -z "$BACKUP_KEEP_DAYS" ]; then
    echo "BACKUP_KEEP_DAYS must be configured in /etc/sysconfig/valheim"
    exit 1
fi

if [ ! -d /valheim/.config/unity3d/IronGate/Valheim/worlds ]; then
    echo "No Valheim worlds to backup."
    exit 0
fi

echo "Backing up Valheim"
mkdir -p /valheim/backups
dest="/valheim/backups/backup-$(date +%s).tar"
tar cf $dest /valheim/.config/unity3d/IronGate/Valheim/worlds
echo "Valheim worlds backed up to $dest"

# Remove backups older than set days
find /valheim/backups -type f -mtime +"$BACKUP_KEEP_DAYS" -name '*.tar' -exec rm -- {} \;

