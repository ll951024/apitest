# coding:utf-8
import unittest
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import HTMLTestReportEN

current_path = os.path.realpath(__file__)[0]
#current_path = os.getcwd()  # 当前文件路径
report_path = os.path.join(current_path, "testReport")
# 测试报告为result.html
result_path = os.path.join(report_path, "bytenew_api_report.html")
print(result_path)


# 加载全部用例
def all_case():
    case_path = os.path.join(current_path, "case")  # 用例路径
    discover = unittest.defaultTestLoader.discover(case_path,pattern="test*.py")
    return discover


def send_email(smtpserver, port, sender, psw, receiver):
    # 写信模板
    msg = MIMEMultipart()
    msg['Subject'] = "这是班牛项目的自动化测试报告"
    msg['From'] = sender
    msg['to'] = receiver

    # 通过os获取文件路径
    annex = open(result_path, "r", encoding="utf-8").read()  # 附件，打开并且读取测试报告

    main_body = '<pre><h1>这是opa项目的自动化测试报告，请查阅！`</h1></pre>'  # 正文的内容

    # 添加正文到容器
    body = MIMEText(main_body, "html", "utf-8")
    msg.attach(body)

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

if __name__ == "__main__":

    # 打开文件，把结果写进文件中，w，有内容的话，清空了再写进去
    fp = open(result_path, "wb")  # 打开result.html，把测试结果写进去
    runner = HTMLTestReportEN.HTMLTestRunner(stream=fp, title="测试报告",description="用例执行情况")

    # 调用all_case函数返回值
  #  runner.run(all_case())
    # 有开有闭，关闭刚才打开的文件
    fp.close()

    # 发送邮件
    #1111
    send_email("smtp.163.com", 465, "ll17681827772@163.com", "TZWVUJIQCAODPCVN", "1144767408@qq.com")