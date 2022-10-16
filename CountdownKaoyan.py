import smtplib
from email.mime.text import MIMEText
import string
import datetime
import requests
import re
from bs4 import BeautifulSoup


sender_name = 'yaoyao'
receiver_name = 'nana'

kenenbi = '2022-12-24'  # 纪念日
name = 'liyao'  # 发件人名称
mail_title = '考研倒计时'  # 邮件名称

"""
mailto_list = ["liyao1119@mails.jlu.edu.cn"]  # 收件人
mail_host = "smtp.qq.com"  # 设置邮箱服务器
mail_user = "1979443072@qq.com"  # 用户名
mail_pass = "tfhuctdjonbecgbe"  # 密码
"""

mailto_list = ["***@***.***","***@***.***"]  # 收件人
mail_host = "smtp.qq.com"  # 发件服务器
mail_user = "*****@qq.com"  # 用户名
mail_pass = "******"  # 密码

def get_deltaDay():
    """
    计算日期差
    """
    d1 = datetime.datetime.strptime(kenenbi, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d')
    delta = d1 - d2
    return delta.days


def get_date():
    """
    获取今天的日期
    """
    i = datetime.datetime.now()
    date = "%s/%s/%s" % (i.year, i.month, i.day)
    return date




mail_content = """<!DOCTYPE html>
<html><head>
    <title>
    </title>
    <meta name="viewport" content="width=device-width,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no">
    <link rel="stylesheet" href="/stylesheets/style.css">
</head>
<body style="margin:0;padding:0;" class="vsc-initialized">
    <div style="width:100%; margin: 40px auto;font-size:20px; color:#5f5e5e;text-align:center">
        <span>距离考研只剩下</span>
        <span style="font-size:24px;color:rgb(221, 73, 73)">{0}</span>
        <span>天了哦</span>
    </div>

    <div style="width:60%;margin:40px auto;color:#5f5e5e;text-align:center">
       <span>今天也要努力学习呢</span>
        <img src="https://s1.ax1x.com/2022/04/16/LYkkVK.jpg" style="width:100%;margin-top:10px" alt="" class="CToWUd a6T" tabindex="0"><div class="a6S" dir="ltr" style="opacity: 0.01; left: 403.802px; top: 342px;"><div id=":nt" class="T-I J-J5-Ji aQv T-I-ax7 L3 a5q" role="button" tabindex="0" aria-label="下载附件“”" data-tooltip-class="a1V" data-tooltip="下载"><div class="akn"><div class="aSK J-J5-Ji aYr"></div></div></div></div>
    </div>


</body></html>""".format(str(get_deltaDay()))


def send_mail(to_list, sub, content):
    """
    发送邮件
    """
    me = name + "<" + mail_user + ">"
    msg = MIMEText(content, _subtype='html', _charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ",".join(mailto_list)
    try:
        server = smtplib.SMTP_SSL(mail_host, )
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(str(e))
        return False

#print(get_deltaDay())
#print(get_date())
#print(get_weathertips())
#print(get_tuwei())
#print(get_weather_cc())
#print(get_weather_hohhot())
#print(get_image())

if __name__ == '__main__':
    if send_mail(mailto_list, mail_title, mail_content):
        print("success!")
    else:
        print("failure!")




