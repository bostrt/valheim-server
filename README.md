# Valheim Dedicated Server for Fedora/RHEL/Centos

# Installation and Initial Setup

### Package
```bash
$ dnf copr enable bostrt/valheim 
$ dnf install valheim-server
```

### Configure Your Server

```bash
$ vi /etc/sysconfig/valheim

NAME="my-server"
WORLD="valheim-rocks"
PASSWORD="t0psecret"
# Number of days to keep backups
BACKUP_KEEP_DAYS="5"
```

### Open Ports
```bash
# firewall-cmd --add-port=2456/udp --add-port=2457/udp --add-port=2458/udp --add-port=2456/tcp --add-port=2457/tcp --add-port=2458/tcp --permanent
# firewall-cmd --reload 
```

**NOTE**: Remember to forward ports on your router!

### Start the Server

```bash
$ systemctl start valheim
```

🚀 You are done! 

See below for more server management tips.



# Server Management

## Services

```bash
$ systemctl start valheim  # Start the dedicated game server
$ systemctl stop valheim   # Stop it
```

## Backups

Backups will start running automatically after package installation.  

```bash
$ systemctl status valheim-backup.timer  # Check the backups are active
$ ls -la /valheim/backups                # Check backups are present
```

## Steam Updates

Steam update checks are performed each time the service is started.