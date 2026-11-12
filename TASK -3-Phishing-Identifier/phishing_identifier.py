
print("=" * 55)
print("          LIVE PHISHING EMAIL IDENTIFIER")
print("=" * 55)

sender = input("\nEnter sender email: ")
subject = input("Enter email subject: ")
message = input("Enter email message: ")
link = input("Enter email link (if any): ")
attachment = input("Enter attachment name (if any): ")

score = 0
warnings = []

# Check sender
if "@" not in sender or sender.endswith("@"):
    score += 2
    warnings.append("Invalid sender email address")

if any(word in sender.lower() for word in
       ["unknown", "verify", "secure", "alert"]):
    score += 1
    warnings.append("Suspicious sender name")

# Check urgent language
urgent_words = [
    "urgent", "immediately", "suspended",
    "blocked", "expire", "act now", "24 hours"
]

for word in urgent_words:
    if word in subject.lower() or word in message.lower():
        score += 1
        warnings.append("Urgent or threatening language detected")
        break

# Check sensitive information requests
sensitive_words = [
    "password", "otp", "bank details",
    "credit card", "pin"
]

for word in sensitive_words:
    if word in message.lower():
        score += 2
        warnings.append("Request for sensitive information")
        break

# Check suspicious links
if link != "":
    if not link.startswith("https://"):
        score += 2
        warnings.append("Link does not use HTTPS")

    if any(word in link.lower() for word in
           ["login", "verify", "claim", "secure"]):
        score += 1
        warnings.append("Link contains suspicious keywords")

# Check attachment
if attachment.lower().endswith(
    (".exe", ".bat", ".scr", ".js", ".vbs")
):
    score += 3
    warnings.append("Potentially dangerous attachment")

# Display report
print("\n" + "=" * 55)
print("              ANALYSIS REPORT")
print("=" * 55)

if warnings:
    for warning in warnings:
        print("[!] " + warning)
else:
    print("[+] No obvious phishing indicators detected")

print("\nRisk Score:", score)

if score >= 5:
    print("RESULT: LIKELY PHISHING")
elif score >= 2:
    print("RESULT: SUSPICIOUS EMAIL")
else:
    print("RESULT: NO OBVIOUS RED FLAGS")

print("=" * 55)
print("Note: This is a basic educational heuristic.")
