# Telegram Multi-Source Auto Forwarder (Userbot) Version 1.3

A powerful, asynchronous Telegram Userbot built with **Telethon** that monitors multiple source channels simultaneously and automatically forwards or copies posts (text, images, videos, and files) to a single target channel in real-time. 

It includes an intelligent **Content Protection Bypass** that automatically downloads and re-posts media if the source channel has forwarding restrictions enabled.

## ✨ Features

- **Multi-Source Monitoring:** Monitor as many source channels as you want by defining the count at startup.
- **Smart Input Validation:** User-friendly CLI that safely handles both `@usernames` and `Channel IDs` (with or without `-100`).
- **Restriction Bypass:** Automatically detects `ChatForwardsRestrictedError` (Protect Content) and switches from *Direct Forwarding* to *Copy & Re-post* (Download & Upload) automatically.
- **Full English Logging:** Clean, professional terminal logs with zero encoding/font issues.
- **Automatic Cleanup:** Temporary downloaded media files are instantly deleted after a successful upload to save disk space.

---

## 🚀 Getting Started

### 1. Prerequisites
Make sure you have Python 3.7+ installed on your system. You will also need to install the required dependency:

```bash
pip install telethon
```

2. Get Telegram API Credentials
Since this is a Userbot, you need to obtain your own API credentials:

Go to my.telegram.org and log in with your Telegram phone number.

Go to API development tools.

Create a new application (you can use any title and short name).

Copy your API_ID and API_HASH.

3. Setup the Script
Open the Python script and replace the placeholder values with your actual credentials:
# ======= CONFIGURATION ========
API_ID = 1234567                # Replace with your API ID (Integer)
API_HASH = 'your_api_hash_here'  # Replace with your API Hash (String)

🛠️ How to Use
Run the script from your terminal or command prompt:

```Bash
python reposter_v1.3.py
```
Step-by-Step Interactive Setup:
Authentication: On the very first run, the script will ask for your phone number. Enter it in the international format (e.g., +959xxxxxxxxx). Then, enter the 5-digit login code sent to your official Telegram app.

Define Sources Count: The script will ask how many channels you want to clone from.

Enter Channels: Input the source and target channels. You can use public usernames or private IDs.

Example Input Session:
--- Telegram Controlled Input Auto Forwarder ---
How many Source Channels do you want to add? (Enter a number): 2
Enter Source Channel #1 (Username @ or ID): @public_news_channel
Enter Source Channel #2 (Username @ or ID): -1001987654321

Enter Target Channel (Only One): @my_destination_channel

⚠️ Important Notes & Permissions
Source Channels: Your Telegram account does NOT need to be an admin in the source channels. You only need to be a member (if it's a private channel) or just know the username (if it's public).

Target Channel: Your Telegram account MUST be an Admin in the target channel with "Post Messages" permissions enabled.

Session File: The script creates a file named ultimate_forwarder_session.session. This file keeps you logged in. If you want to change your Telegram account or restart the configuration completely, simply delete this file and re-run the script.

📄 License
This project is open-source and available under the MIT License.
