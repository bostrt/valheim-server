# Valheim Dedicated Server - Manual Setup

## Prereqs for steamcmd
```bash
$ dnf install glibc.i686 libstdc++.i686
```

## User setup
```
# useradd -d /valheim valheim
# sudo su - valheim
# mkdir Game

# semanage fcontext -a -t usr_t '/valheim(/.*)?'
# restorecon -RFv /valheim/
```

# Configure services

- Sysconfig `valheim-sysconfig -> /etc/sysconfig/valheim`
- Systemd unit `valheim.service`
- Systemd backup unit `valheim-backup.service`
- Systemd backup timer `valheim-backup.timer`
- Create Update and Install script `/valheim/update.sh`
- Create backup script `/valheim/backup.sh`.
- Create `start_valheim.sh`
- Add, reload, start
```
# systemctl daemon-reload
# systemctl start valheim.service
# systemctl start valheim-backup.timer
# systemctl enable valheim-backup.timer
```

- Open ports
```
# firewall-cmd --add-port=2456/udp --add-port=2457/udp --add-port=2458/udp --add-port=2456/tcp --add-port=2457/tcp --add-port=2458/tcp --permanent
# firewall-cmd --reload 
```

- Port forward on Router

# Start daemon and stuff

This will automatically update Valheim.

```
# systemctl start valheim
```