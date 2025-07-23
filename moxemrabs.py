# List of domain variations with different capitalizations
base_user = "test1234"
domain_variations = [
    "gmail.com", "Gmail.com", "gMail.com", "gmaIl.com", "gmaiL.com", "GMAil.com", "GMaiL.com", "gMaIL.com",
    "GmAil.com", "GmAIL.com", "GmAiL.com", "gmAIl.com", "gMaIl.com", "gmAiL.com", "gmAIL.com", "gMaIL.com",
    "GMaiL.com", "GMAIL.com", "GmaiL.com", "GmAIL.com", "gmaIL.com", "gMail.COM", "GMail.Com", "GmAIl.CoM",
    "gmAIl.CoM", "gMAiL.CoM", "gmAiL.CoM", "gMaiL.CoM", "gMaIl.CoM", "GMaiL.CoM", "GMaiL.coM", "GmaIL.com",
    "gmAIL.CoM", "gmaIl.CoM", "gMAIL.CoM", "gMaiL.cOm", "gMaIL.cOM", "gmaIL.cOM", "GMAIL.cOM", "GMail.cOm",
    "gMAiL.cOM", "GmAiL.cOm", "gmAiL.cOm", "GmAIL.cOm", "gmAIL.cOm", "GMail.cOM", "GMaiL.cOm", "GmAil.CoM",
    "gMAil.CoM", "gmAil.Com", "gMAil.com", "gmaiL.Com", "gmAiL.Com", "gMaIl.Com", "gMaIL.Com", "gMail.CoM",
    "gMail.cOM", "gmAIl.cOm", "gmaiL.cOm", "gMail.coM", "GMaiL.Com", "GMAIL.CoM", "GmaIL.CoM", "gmaIL.CoM",
    "gMAIL.Com", "gmAIL.COM", "GMAIL.COM", "GMail.COM", "gMail.COM", "gMaiL.COM", "GMaiL.COM", "GmAIL.COM",
    "gMaIL.COM", "gmAiL.COM", "gmAIl.COM", "gmaIL.COM", "gmAil.COM", "GmAil.COM", "GmAiL.CoM", "gMAil.CoM",
    "gMAIL.coM", "Gmail.cOm", "gmaiL.cOm", "GMAIL.cOm", "GmAiL.Com", "gmAIL.CoM", "gMail.Com", "gmAIl.Com",
    "gmAiL.Com", "GmAIL.Com", "GMAIL.coM", "gmaIL.coM", "GMaiL.CoM", "GMail.cOm", "gMaIl.cOM", "GmAIL.cOM",
    "gmAiL.cOM", "gmaIL.cOm", "GMail.CoM", "GmAIl.cOM"
]

# Take the first 100 only
domain_variations = domain_variations[:100]

# Create the email addresses
emails = [f"{base_user}@{domain}" for domain in domain_variations]

# Write to a .txt file
file_name = "test_emails.txt"
with open(file_name, "w") as f:
    for email in emails:
        f.write(email + "\n")

print(f"File '{file_name}' has been created with 100 emails.")

