import os
import sys
import logging
from telethon import TelegramClient, events
from telethon.errors import ChatForwardsRestrictedError

# Setup logging configuration
logging.basicConfig(
    format='[%(levelname)s/%(asctime)s] %(name)s: %(message)s', 
    level=logging.INFO,
    stream=sys.stdout
)
logger = logging.getLogger("AutoPoster")

# ==================== CONFIGURATION ====================
API_ID = 34819220               # ပြောင်းလဲရန်မလို - ကိုယ့် API ID (Integer)
API_HASH = '5085e66a3f993c21841dff14f0c88469' # ပြောင်းလဲရန်မလို - ကိုယ့် API Hash (String)
# =======================================================

print("--- Telegram Controlled Input Auto Forwarder ---")

# ၁။ Source ဘယ်နှစ်ခုထည့်မလဲ အရင်မေးခြင်း
while True:
    try:
        num_sources = int(input("How many Source Channels do you want to add? (Enter a number): "))
        if num_sources > 0:
            break
        print("Please enter a number greater than 0.")
    except ValueError:
        print("Invalid input! Please enter a valid number (e.g., 3).")

# စာသားတွေကို ID သို့မဟုတ် Username ခွဲထုတ်ပေးမည့် Function
def parse_chat_id(chat_input):
    chat_input = chat_input.strip()
    if chat_input.startswith('-') and chat_input[1:].isdigit():
        return int(chat_input)
    elif chat_input.isdigit():
        return int(chat_input)
    return chat_input

# ၂။ သတ်မှတ်ထားတဲ့ အရေအတွက်အတိုင်း တစ်ခုချင်းစီ တောင်းခြင်း
SOURCE_CHANNELS = []
for i in range(1, num_sources + 1):
    while True:
        src = input(f"Enter Source Channel #{i} (Username @ or ID): ").strip()
        if src:
            SOURCE_CHANNELS.append(parse_chat_id(src))
            break
        print("Input cannot be empty.")

# ၃။ Target Channel ကို တောင်းခြင်း
while True:
    TARGET_INPUT = input("\nEnter Target Channel (Only One): ").strip()
    if TARGET_INPUT:
        TARGET_CHANNEL = parse_chat_id(TARGET_INPUT)
        break
    print("Input cannot be empty.")

logger.info("Initializing Telegram Client...")
client = TelegramClient('ultimate_forwarder_session', API_ID, API_HASH)

# chats=SOURCE_CHANNELS ထဲက ချန်နယ်အားလုံးကို စောင့်ဖတ်မှာပါ
@client.on(events.NewMessage(chats=SOURCE_CHANNELS))
async def handler(event):
    message = event.message
    caption = message.text or ""
    
    chat_from = event.chat.title if event.chat else "Unknown"
    logger.info(f"New post detected from [{chat_from}]! (Message ID: {message.id})")
    
    try:
        # Method 1: Try Direct Forwarding
        await client.send_message(TARGET_CHANNEL, message)
        logger.info("Method 1: Direct Forwarding Successful!")
        
    except ChatForwardsRestrictedError:
        logger.warning("Forwarding restricted. Switching to Method 2 (Copy & Re-post)...")
        
        if message.media:
            try:
                logger.info("Downloading media...")
                file_path = await client.download_media(message, timeout=600)
                
                logger.info("Uploading media to target channel...")
                await client.send_file(TARGET_CHANNEL, file_path, caption=caption)
                logger.info("Method 2: Media Copy & Re-post Successful!")
                
                if os.path.exists(file_path):
                    os.remove(file_path)
                    
            except Exception as download_error:
                logger.error(f"Failed to download media: {download_error}")
                if caption:
                    await client.send_message(TARGET_CHANNEL, caption)
        else:
            await client.send_message(TARGET_CHANNEL, caption)
            logger.info("Method 2: Text-only post copied successfully!")
            
    except Exception as e:
        logger.error(f"Unexpected General Error: {e}")

async def main():
    await client.start()
    logger.info(f"Connected! Monitoring {len(SOURCE_CHANNELS)} sources to Target...")

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
        client.run_until_disconnected()