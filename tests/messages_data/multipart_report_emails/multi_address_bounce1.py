import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Undelivered Mail Returned to Sender',
    from_='MAILER-DAEMON@lvmail01.LL.com',
    to=('rahul.chaudhari@LL.com',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2010, 2, 23, 22, 16, 41, tzinfo=datetime.timezone(datetime.timedelta(-1, 57600))),
    date_str='Tue, 23 Feb 2010 22:16:41 -0800 (PST)',
    text="This is the mail system at host lvmail01.LL.com.\r\n\r\nI'm sorry to have to inform you that your message could not\r\nbe delivered to one or more recipients. It's attached below.\r\n\r\nFor further assistance, please send mail to postmaster.\r\n\r\nIf you do so, please include this problem report. You can\r\ndelete your own text from the attached returned message.\r\n\r\n                   The mail system\r\n\r\n<bbbbvhvbbvkjbhfbvbvjhb@gmail.com>: host\r\n    gmail-smtp-in.l.google.com[209.85.223.33] said: 550-5.1.1 The email account\r\n    that you tried to reach does not exist. Please try 550-5.1.1\r\n    double-checking the recipient's email address for typos or 550-5.1.1\r\n    unnecessary spaces. Learn more at                              550 5.1.1\r\n    http://mail.google.com/support/bin/answer.py?answer=6596 41si5422799iwn.27\r\n    (in reply to RCPT TO command)\r\n\r\n<bscdbcjhasbcjhbdscbhbsdhcbj@gmail.com>: host\r\n    gmail-smtp-in.l.google.com[209.85.223.33] said: 550-5.1.1 The email account\r\n    that you tried to reach does not exist. Please try 550-5.1.1\r\n    double-checking the recipient's email address for typos or 550-5.1.1\r\n    unnecessary spaces. Learn more at                              550 5.1.1\r\n    http://mail.google.com/support/bin/answer.py?answer=6596 41si5422799iwn.27\r\n    (in reply to RCPT TO command)\r\n\r\n<egyfefsdvsfvvhjsd@gmail.com>: host gmail-smtp-in.l.google.com[209.85.223.33]\r\n    said: 550-5.1.1 The email account that you tried to reach does not exist.\r\n    Please try 550-5.1.1 double-checking the recipient's email address for\r\n    typos or 550-5.1.1 unnecessary spaces. Learn more at\r\n    550 5.1.1 http://mail.google.com/support/bin/answer.py?answer=6596\r\n    41si5422799iwn.27 (in reply to RCPT TO command)\r\n\r\n<kfhejkfbsjkjsbhds@gmail.com>: host gmail-smtp-in.l.google.com[209.85.223.33]\r\n    said: 550-5.1.1 The email account that you tried to reach does not exist.\r\n    Please try 550-5.1.1 double-checking the recipient's email address for\r\n    typos or 550-5.1.1 unnecessary spaces. Learn more at\r\n    550 5.1.1 http://mail.google.com/support/bin/answer.py?answer=6596\r\n    41si5422799iwn.27 (in reply to RCPT TO command)\r\n\r\n<qfvhgsvhgsduiohncdhcvhsdfvsfygusd@gmail.com>: host\r\n    gmail-smtp-in.l.google.com[209.85.223.33] said: 550-5.1.1 The email account\r\n    that you tried to reach does not exist. Please try 550-5.1.1\r\n    double-checking the recipient's email address for typos or 550-5.1.1\r\n    unnecessary spaces. Learn more at                              550 5.1.1\r\n    http://mail.google.com/support/bin/answer.py?answer=6596 41si5422799iwn.27\r\n    (in reply to RCPT TO command)\r\n",
    html='',
    headers={'received': ('from lvmail01.LL.com (LHLO lvmail01.LL.com)\r\n (10.60.6.3) by lvmail01.LL.com with LMTP; Tue, 23 Feb 2010 22:16:41\r\n -0800 (PST)', 'by lvmail01.LL.com (Postfix)\r\n\tid 3E47A1BC025; Tue, 23 Feb 2010 22:16:41 -0800 (PST)'), 'date': ('Tue, 23 Feb 2010 22:16:41 -0800 (PST)',), 'from': ('MAILER-DAEMON@lvmail01.LL.com (Mail Delivery System)',), 'subject': ('Undelivered Mail Returned to Sender',), 'to': ('rahul.chaudhari@LL.com',), 'auto-submitted': ('auto-replied',), 'mime-version': ('1.0',), 'content-type': ('multipart/report; report-type=delivery-status;\r\n\tboundary="9B7841BC027.1266992201/lvmail01.LL.com"',), 'content-transfer-encoding': ('7bit',), 'message-id': ('<20100224061641.3E47A1BC025@lvmail01.LL.com>',)},
    attachments=[
        dict(
            filename='',
            content_id='',
            content_disposition='',
            content_type='message/rfc822',
            payload=b'Return-Path: <rahul.chaudhari@LL.com>\nReceived: from localhost (localhost [127.0.0.1])\n\tby lvmail01.LL.com (Postfix) with ESMTP id 9B7841BC027;\n\tTue, 23 Feb 2010 22:16:15 -0800 (PST)\nX-Virus-Scanned: amavisd-new at LL.com\nReceived: from lvmail01.LL.com ([127.0.0.1])\n\tby localhost (lvmail01.LL.com [127.0.0.1]) (amavisd-new, port 10024)\n\twith ESMTP id HXMOLJWXGcFK; Tue, 23 Feb 2010 22:16:15 -0800 (PST)\nReceived: from lvmail01.LL.com (lvmail01.LL.com [10.60.6.3])\n\tby lvmail01.LL.com (Postfix) with ESMTP id 12D311BC025;\n\tTue, 23 Feb 2010 22:16:15 -0800 (PST)\nDate: Tue, 23 Feb 2010 22:16:14 -0800 (PST)\nFrom: Rahul Chaudhari <rahul.chaudhari@LL.com>\nTo: egyfefsdvsfvvhjsd@gmail.com, kfhejkfbsjkjsbhds@gmail.com,\n\tbbbbvhvbbvkjbhfbvbvjhb@gmail.com,\n\tqfvhgsvhgsduiohncdhcvhsdfvsfygusd@gmail.com,\n\tbscdbcjhasbcjhbdscbhbsdhcbj@gmail.com\nMessage-ID: <118707422.15521266992174819.JavaMail.root@lvmail01>\nSubject: Test of bounce email\nMIME-Version: 1.0\nContent-Type: text/plain; charset=utf-8\nContent-Transfer-Encoding: 7bit\nX-Originating-IP: [10.50.4.44]\nX-Mailer: Zimbra 6.0.1_GA_1816.UBUNTU8_64 (ZimbraWebClient - FF3.0\n (Linux)/6.0.1_GA_1816.UBUNTU8_64)\n\nThis is just testing.\n\n\nThanks & Regards,\nRahul P. Chaudhari\nSoftware Developer\nLIVIA India Private Limited\n\nBoard Line - +91.22.6725 5100\nHand Phone - +91.809 783 3437\nWeb URL: www.LL.com \n',
        ),
        ],
    from_values=EmailAddress(name='Mail Delivery System', email='MAILER-DAEMON@lvmail01.LL.com'),
    to_values=(EmailAddress(name='', email='rahul.chaudhari@LL.com'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)