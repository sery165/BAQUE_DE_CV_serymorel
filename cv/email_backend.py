import ssl
from django.core.mail.backends.smtp import EmailBackend

class MyEmailBackend(EmailBackend):
    def open(self):
        self.connection = super().open()
        if self.connection:
            self.connection.starttls(context=ssl._create_unverified_context())
        return self.connection
