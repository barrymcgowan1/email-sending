import smtplib

# Set up the SMTP server
server = smtplib.SMTP('smtp.example.com', 587)
server.starttls()
server.login("YOUR_EMAIL_ADDRESS", "YOUR_EMAIL_PASSWORD")

# Create the message
msg = "Subject: Test Email\n\nThis is a test email sent from Python."

# Send the email
server.sendmail("SENDER_EMAIL_ADDRESS", "RECIPIENT_EMAIL_ADDRESS", msg)

# Close the server
server.quit()

print("Email sent successfully!")
