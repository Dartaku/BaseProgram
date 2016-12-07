from flask_mail import Message

__author__ = 'Dartaku'


class Email(object):
    def __init__(self, subject, sender, recipients, text_body, html_body):
        self.subject = subject
        self.sender = sender
        self.recipients = recipients
        self.text_body = text_body
        self.html_body = html_body

    def create_email(self):
        msg = Message(self.subject, sender=self.sender, recipients=self.recipients)
        msg.body = self.text_body
        msg.html = self.html_body