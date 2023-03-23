import imaplib
import email
from email.header import decode_header

# login credentials
username = "vishal641984@gmail.com"
password = "pythonvishal"

# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL("imap.gmail.com")

# authenticate
imap.login(username, password)

# select mailbox
# if you want to select a specific mailbox, you can do so like this:
# imap.select("Inbox")
imap.select("Inbox")

# search for all emails in inbox
status, messages = imap.search(None, 'ALL')

# iterate through messages
for msg in messages[0].split(b' '):
    try:
        # fetch message
        res, msg = imap.fetch(msg, "(RFC822)")
        
        # decode message
        msg = email.message_from_bytes(msg[0][1])
        
        # extract sender email address
        sender = msg['From']
        print(sender)
    except Exception as e:
        print(e)

# close the mailbox and logout
imap.close()
imap.logout()