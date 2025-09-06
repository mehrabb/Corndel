#!/bin/bash

# ===== Configuration =====
EMAIL="mbucktow@gmail.com"
HOSTNAME=$(hostname)
DATE=$(date +"%Y-%m-%d %H:%M:%S")
REPORT="/tmp/system_health_report.txt"
LOGFILE="$HOME/system_health_email.log"

# ===== Detect OS =====
OS=$(uname)

# ===== Collect System Info =====
if [ "$OS" = "Darwin" ]; then
    DISK_USAGE=$(df -h)
    CPU_USAGE=$(top -l 1 | grep "CPU usage")
    MEM_USAGE=$(top -l 1 | grep PhysMem)
    TOP_MEM=$(ps -axo pid,ppid,command,%mem,%cpu | head -n 6)
    TOP_CPU=$(ps -axo pid,ppid,command,%cpu,%mem | head -n 6)
else
    DISK_USAGE=$(df -h --output=source,fstype,size,used,avail,pcent,target)
    CPU_USAGE=$(mpstat 1 1 | awk '/Average:/ {print "User: "$3"%  System: "$5"%  Idle: "$12"%"}')
    MEM_USAGE=$(free -h)
    TOP_MEM=$(ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -n 6)
    TOP_CPU=$(ps -eo pid,ppid,cmd,%cpu,%mem --sort=-%cpu | head -n 6)
fi

# ===== Compose HTML Report =====
HTML_REPORT=$(cat <<EOF
<html><body>
<h2>System Health Report - $HOSTNAME</h2>
<p><b>Date:</b> $DATE</p>
<hr>
<h3> Disk Usage</h3><pre>$DISK_USAGE</pre>
<h3> CPU Usage</h3><pre>$CPU_USAGE</pre>
<h3> Memory Usage</h3><pre>$MEM_USAGE</pre>
<h3> Top 5 Memory-Consuming Processes</h3><pre>$TOP_MEM</pre>
<h3> Top 5 CPU-Consuming Processes</h3><pre>$TOP_CPU</pre>
</body></html>
EOF
)

# ===== Send Email =====
if command -v msmtp >/dev/null 2>&1; then
    #echo "$HTML_REPORT" | msmtp -a gmail "$EMAIL"
    (
    echo "Subject: System Health Report - $HOSTNAME ($DATE)"
    echo "From: $EMAIL"
    echo "To: $EMAIL"
    echo "MIME-Version: 1.0"
    echo "Content-Type: text/html; charset=UTF-8"
    echo ""
    echo "$HTML_REPORT"
    ) | msmtp -a gmail "$EMAIL"
    STATUS=$?
    if [ $STATUS -eq 0 ]; then
        echo "$(date +"%F %T") - Email sent successfully to $EMAIL" >> "$LOGFILE"
    else
        echo "$(date +"%F %T") - ERROR: Failed to send email (msmtp exited with code $STATUS)" >> "$LOGFILE"
    fi
else
    echo "$(date +"%F %T") - ERROR: msmtp not found. Please install it." >> "$LOGFILE"
fi

# ===== Save report locally =====
echo "$HTML_REPORT" > "$REPORT"
echo "Report saved to $REPORT"
