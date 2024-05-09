import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoProject.settings.development'

if __name__ == '__main__':

    subject, from_email, to = '测试邮件', 'xxx@163.com', 'xxx@163.com'
    text_content = '测试邮件'
    html_content = '<p>测试邮件</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()