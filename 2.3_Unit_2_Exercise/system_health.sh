#!/bin/bash

# ===== Configuration =====
EMAIL="mbucktow@gmail.com"
HOSTNAME=$(hostname)
DATE=$(date +"%Y-%m-%d %H:%M:%S")
REPORT="/tmp/system_health_report.txt"

# ===== Send Email with msmtp =====
if command -v msmtp >/dev/null 2>&1; then
    (
      echo "Subject: System Health Report - $HOSTNAME ($DATE)"
      echo "From: $EMAIL"
      echo "To: $EMAIL"
      echo "MIME-Version: 1.0"
      echo "Content-Type: text/html; charset=UTF-8"
      echo ""
      echo "<html><body>"
      echo "<h2>System Health Report - $HOSTNAME</h2>"
      echo "<p><b>Date:</b> $DATE</p>"
      echo "<hr>"
      echo "<h3> Disk Usage</h3><pre>$(df -h --output=source,fstype,size,used,avail,pcent,target)</pre>"
      echo "<h3> CPU Usage</h3><pre>$(mpstat 1 1 | awk '/Average:/ {print "User: "$3"%  System: "$5"%  Idle: "$12"%"}')</pre>"
      echo "<h3> Memory Usage</h3><pre>$(free -h)</pre>"
      echo "<h3> Top 5 Memory-Consuming Processes</h3><pre>$(ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -n 6)</pre>"
      echo "<h3> Top 5 CPU-Consuming Processes</h3><pre>$(ps -eo pid,ppid,cmd,%cpu,%mem --sort=-%cpu | head -n 6)</pre>"
      echo "</body></html>"
    ) | tee $REPORT | msmtp "$EMAIL"
    echo "HTML report emailed to $EMAIL"
else
    echo "msmtp not found. Please install it with: brew install msmtp"
    echo "Report saved at $REPORT"
fi
