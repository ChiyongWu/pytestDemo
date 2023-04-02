import yagmail


class mail_util:
    def __init__(self, sender: str, password: str, smtp_host: str):
        self.sender = sender
        self.password = password
        self.smtp_host = smtp_host
        self.mail = yagmail.SMTP(sender, password, smtp_host)

    def send_email(self, receivers: list, subject: str, content: str, cc: list = None, attachments=None) -> None:
        self.mail.send(receivers, subject, content, cc=cc, attachments=attachments)


mail = mail_util('745195581@qq.com', 'llyiwspwstvabdjd', 'smtp.qq.com')

if __name__ == '__main__':
    mail.send_email(['1152777494@qq.com'], '测试邮件', 'ABBBBBBBBCCCC', ['wuchiyong@yaowutech.com'],
                    attachments='./0401pic.jpg')