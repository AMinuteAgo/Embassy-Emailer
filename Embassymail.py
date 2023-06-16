import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk

# Email configuration
smtp_server = 'your_smtp_server'
smtp_port = 587
sender_email = 'your_email@example.com'
sender_password = os.environ.get('EMAIL_PASSWORD')  # Retrieve password from environment variable

# Function to send emails
def send_emails():
    # Retrieve email addresses from the textbox
    email_addresses = textbox.get("1.0", "end-1c").split('\n')

    # Connect to the SMTP server
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
    except smtplib.SMTPException as e:
        print('Error connecting to the SMTP server:', e)
        return

    # Email content
    subject = 'Your Subject'
    message = 'Your Message'

    for recipient_email in email_addresses:
        if recipient_email.strip() == "":
            continue

        try:
            # Create a multipart message
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject

            # Add the message body
            msg.attach(MIMEText(message, 'plain'))

            # Send the email
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print('Email sent to', recipient_email)
        except smtplib.SMTPException as e:
            print('Error sending email to', recipient_email, ':', e)

    # Disconnect from the server
    server.quit()

# Create a GUI window using tkinter
window = tk.Tk()
window.title("Email Sender")

# Create a textbox for entering email addresses
textbox = tk.Text(window, height=10, width=40)
textbox.pack(pady=10)

# Create a button to send emails
send_button = tk.Button(window, text="Send Emails", command=send_emails)
send_button.pack()

# Start the GUI event loop
window.mainloop()
