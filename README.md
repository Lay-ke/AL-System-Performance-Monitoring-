# Documentation for System Monitoring and Alert Script

This script monitors system metrics (CPU, RAM, and disk usage) and sends email alerts using the Mailjet API if predefined thresholds are breached. It demonstrates best practices for system monitoring and notification via email.

---

## Overview

This Python script:
1. Monitors system metrics:
   - **CPU usage**
   - **RAM usage**
   - **Disk space usage**
2. Sends an email alert when:
   - CPU usage exceeds 10%.
   - RAM usage exceeds 10%.
   - Free disk space falls below 50%.

---

## Features

- **System Monitoring**: Uses the `psutil` library to gather CPU, RAM, and disk usage statistics.
- **Alert Notifications**: Sends email alerts through the Mailjet API.
- **Configurable Thresholds**: Thresholds for system metrics can be customized in the script.
- **Time-stamped Alerts**: Email subject includes the current timestamp.

---

## Requirements

1. **Python Installation**:
   - Ensure Python 3.x is installed on your system.
   - Check your Python version:
     ```bash
     python --version
     ```

2. **Install Required Libraries**:
   - Install the following Python packages using pip:
     ```bash
     pip install psutil python-dotenv mailjet-rest
     ```

3. **Mailjet Account**:
   - Create a Mailjet account if you don’t already have one.
   - Obtain your API Key and API Secret from the Mailjet dashboard.

4. **Environment File**:
   - Create a `.env` file in the same directory as the script and add your Mailjet credentials:
     ```plaintext
     api_key=your_mailjet_api_key
     api_secret=your_mailjet_api_secret
     ```

## How It Works

This section explains the step-by-step workflow of the script and how the monitoring and alert system operates.

---

### 1. Initialization
1. **Environment Variables**:
   - The script uses `dotenv` to load Mailjet API credentials (`api_key` and `api_secret`) from a `.env` file.
   - This ensures sensitive information is not hardcoded in the script.

2. **Thresholds**:
   - The script defines thresholds for:
     - **CPU usage**: Maximum 10%.
     - **RAM usage**: Maximum 10%.
     - **Disk free space**: Minimum 50%.
   - These thresholds can be adjusted within the script.

---

### 2. System Metrics Monitoring
1. **CPU Usage**:
   - Uses `psutil.cpu_percent(interval=1)` to calculate CPU usage over a one-second interval.

2. **RAM Usage**:
   - Uses `psutil.virtual_memory().percent` to get the percentage of RAM currently in use.

3. **Disk Usage**:
   - Uses `psutil.disk_usage('/').percent` to calculate the percentage of disk space used on the root partition.

---

### 3. Alert Message Construction
1. The script evaluates the monitored metrics against their thresholds.
2. If a metric exceeds its threshold:
   - A corresponding message is added to the `alert_message` string.
   - For example:
     - If CPU usage is 15% (threshold is 10%), the message will be:
       ```
       CPU usage is high: 15% (Threshold: 10%)
       ```

---

### 4. Sending Email Alerts
1. If `alert_message` contains any threshold breaches:
   - The script invokes the `send_alert` function.
   - The function:
     - Constructs an email with:
       - **Subject**: Includes the timestamp (e.g., `Python Monitoring Alert Alert-2024-11-25 12:00:00`).
       - **Message**: Lists the breached metrics.
     - Sends the email using the Mailjet API.

2. If no thresholds are breached:
   - The script prints:
     ```
     All system metrics are within normal limits.
     ```

---

### 5. Email Delivery
- The Mailjet API is used to deliver the alert email to the specified recipient.
- If the email fails to send, an error message is printed to the console.

---

### Summary of Workflow
1. Load Mailjet credentials from `.env` file.
2. Monitor system metrics (CPU, RAM, disk).
3. Compare metrics against predefined thresholds.
4. If thresholds are breached:
   - Construct an alert message.

## How to Run

Follow these steps to run the system monitoring and alert script:

---

### 1. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script.
   - Run the script using the following command:
     ```bash
     python monitor.py
     ```

---

### 2. **Monitor the Output**:
   - If system thresholds are breached, an alert email will be sent, and a message will be displayed in the terminal:
     ```plaintext
     Email sent: 200
     ```
   - If all system metrics are within normal limits, the following message will appear:
     ```plaintext
     All system metrics are within normal limits.
     ```

---

### 3. Verifying Alerts

1. **Check Email**:
   - Verify that the recipient email address specified in the script has received the alert.

2. **Debugging Email Failures**:
   - If the email fails to send, the terminal will display an error message:
     ```plaintext
     Failed to send email: <error_description>
     ```
   - Ensure your Mailjet credentials are correct and that your network allows outgoing connections.

---
