import logging
import sys
import os
import unittest
from testCase.testPC import PC
suite = unittest.TestSuite()
import unittest
from htmltestreport import HTMLTestReport
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import common.HTMLTestReportEN

#测试用例执行结果保存路径
report_path = "/Volumes/bytenew/dm/api/apitest/banniuApiTest/testReport/bytenew_api_report.html"

#添加邮件配置
def send_email(smtpserver, port, sender, psw, receiver):
    # 写信模板
    msg = MIMEMultipart()
    msg['Subject'] = "这是班牛项目的自动化测试报告"
    msg['From'] = sender
    msg['to'] = ', '.join(receiver)






    # 读取报告
    annex = open(report_path, 'rb')
    mail_body = annex.read()
    annex.close()

    # 通过os获取文件路径
    annex = open(report_path, "r", encoding="utf-8").read()  # 附件内容的路径，打开并且读取测试报告
    main_body = '<pre><h1>这是班牛项目的自动化测试报告，请查阅！`</h1></pre>'  # 正文的内容

    # 添加正文到容器
    body = MIMEText(main_body, "html", "utf-8")
    body1 = MIMEText(annex,"html","utf-8")
    #body = MIMEText(main_body, "html", "utf-8")
    msg.attach(body)
    msg.attach(body1)

    # 添加附件到容器
    att = MIMEText(annex, "base64", "utf-8")
    att["Content-Type"] = "application/octet-sream"
    att["Content-Disposition"] = 'attachment;filename="api_test_report.html"'  # 附件名称
    msg.attach(att)

    # 连接发送邮件
    smtp = smtplib.SMTP_SSL(smtpserver, port)
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

def case():
    # 添加测试用例
    suite.addTest(PC('test_search'))
    # 实例化运行对象
    runner = unittest.TextTestRunner()
    report = HTMLTestReport(report_path, title='自动化测试报告', description='bytenew接口自动化测试报告')
    report.run(suite)



if __name__ == '__main__':
    #执行测试用例
    case()
    #发送邮箱
    send_email("smtp.163.com", 465, "ll17681827772@163.com", "TZWVUJIQCAODPCVN", ["1144767408@qq.com","ll17681827772@163.com"])
    print("发送成功")
