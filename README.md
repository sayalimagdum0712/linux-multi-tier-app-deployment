# Linux Multi-Tier Web Application Deployment

A hands-on Linux deployment and operations project demonstrating how to deploy, secure, monitor, and troubleshoot a web application on a bare Ubuntu server without Docker.

## Architecture

Internet
   |
   v
Nginx Reverse Proxy :80
   |
   v
Flask Application :5000
   |
   v
Ubuntu Linux Server

## Technologies

- Ubuntu Linux
- Python
- Flask
- Nginx
- systemd
- UFW
- Fail2ban
- Cron
- Logrotate
- Bash
- Git

## Linux Concepts Demonstrated

### Users & Permissions
- Created dedicated non-root `appuser`
- Configured application ownership and permissions
- Application runs without root privileges

### Process Management
- Managed Flask application using systemd
- Configured automatic restart
- Enabled service to start automatically at boot
- Used `systemctl` and `journalctl`

### Networking
- Flask runs internally on port 5000
- Nginx acts as a reverse proxy
- Public traffic is handled through port 80

### Security
- Configured UFW firewall
- Allowed SSH, HTTP and HTTPS
- Disabled password-based SSH authentication
- Configured Fail2ban for SSH protection

### Backup & Automation
- Automated application/configuration backups
- Scheduled backups using cron
- Removed backups older than 7 days

### Logging
- Used systemd journal logs
- Configured logrotate
- Inspected Nginx access and error logs

### Monitoring
- Created application health-check script
- Verified application availability
- Tested automatic recovery

## Failure Testing

The deployment was intentionally tested by:

1. Killing the Flask process
2. Verifying systemd automatically restarted it
3. Stopping Nginx
4. Diagnosing the failure using systemctl and journalctl
5. Restarting Nginx and verifying recovery
6. Testing disk usage and cleanup

## Project Structure

```text
linux-multi-tier-app-deployment/
├── app/
│   └── app.py
├── scripts/
│   ├── backup-myapp.sh
│   └── myapp-health.sh
├── systemd/
│   └── myapp.service
├── nginx/
│   └── myapp
├── logrotate/
│   └── myapp
└── README.md
