import time
from mailjet_rest import Client
import psutil
from dotenv import load_dotenv
import os

# Load variables from the .env file
load_dotenv()

# Define mail credentials
api_key = os.getenv('api_key')
api_secret = os.getenv('api_secret')

# Define system time
current_time = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",current_time)

# Define System thresholds ( 10% RAM, 50% free disk space, 10% CPU )
CPU_THRESHOLD = 2
RAM_THRESHOLD = 10
DISK_THRESHOLD = 50

# Function to send email
def send_alert(subject, message):
    # instantiate mailjet client
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
        {
            "From": {
            "Email": "layke@gmail.com",
            "Name": "Layke"
        },
        "To": [
            {
            "Email": "yawmintah1@gmail.com",
            "Name": "Admin"
        }
        ],
        "Subject": subject,
        "HTMLPart": f"<h3>{message}</h3>"
        }
        ]
        }
    try:
        result = mailjet.send.create(data=data)
        print(f"Email sent: {result.status_code}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")


# Check system metrics
# print(cpu_usage)
cpu_usage = psutil.cpu_percent(interval=1)
# print(ram_usage)
ram_usage = psutil.virtual_memory().percent
# print(disk_usage)
disk_usage = psutil.disk_usage('/').percent

# Create alert message based on threshold breaches
alert_message = ""

if cpu_usage > CPU_THRESHOLD:
    alert_message += f"CPU usage is high: {cpu_usage}% (Threshold: {CPU_THRESHOLD}%)\n"
if ram_usage > RAM_THRESHOLD:
    alert_message += f"RAM usage is high: {ram_usage}% (Threshold: {RAM_THRESHOLD}%)\n"
if disk_usage > DISK_THRESHOLD:
    alert_message += f"Disk space is low: {100 - disk_usage}% free (Threshold: {DISK_THRESHOLD}% free)\n"

# If any threshold is breached, send an email alert
if alert_message:
    send_alert(f"Python Monitoring Alert Alert-{formatted_time}", alert_message)
else:
    print("All system metrics are within normal limits.")


