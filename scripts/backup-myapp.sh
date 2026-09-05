#!/bin/bash

BACKUP_DIR="/var/backups/myapp"
DATE=$(date +"%Y-%m-%d_%H-%M-%S")

mkdir -p "$BACKUP_DIR"

tar -czf "$BACKUP_DIR/myapp_$DATE.tar.gz" \
/srv/myapp/app.py \
/etc/systemd/system/myapp.service \
/etc/nginx/sites-available/myapp

find "$BACKUP_DIR" -type f -mtime +7 -delete
