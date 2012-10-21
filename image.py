'''
OUT OF TIME - Image Retrieval
Windows-only
Code by Jacob Turner, released under the MIT license
'''

import imaplib
import smtplib
import os
import time
import win32gui
import win32ui
import win32con
import email

emailaddress = "**REPLACE**"
password = "**REPLACE**"
imapserver = "**REPLACE**"
smtpserver = "**REPLACE**"

def retrieve():
    acct = imaplib.IMAP4_SSL(imapserver)
    acct.login(emailaddress, password)
    acct.select()
    typ, data = acct.search(None, 'UNSEEN')
    del typ
    data = str(data).strip("'[]").split(" ")
    msgs = []
    if data != ['']:
        for x in range(len(data)):
            typ, msg = acct.fetch(data[x], '(RFC822)')
            del typ
            a = email.message_from_string(msg[0][1])
            b = a["Return-Path"].strip("<>")
            a = a.get_payload()
            if type(a) is not str:
                a = a[0].get_payload()
            a = a.split("--", 1)[0]
            msgs.append((a.replace('\n', ' ').replace('\r', ' '), b))
            acct.store(data[x], '+FLAGS', '\\Seen')
        acct.close()
        acct.logout()
        return msgs
    else:
        acct.close()
        acct.logout()
        return None

def send(toea, subject, text):
    msg = email.MIMEText.MIMEText(text)
    msg['Subject'] = subject
    msg['From'] = emailaddress
    msg['To'] = toea
    mail = smtplib.SMTP_SSL(smtpserver)
    mail.login(emailaddress, password)
    mail.sendmail(emailaddress, toea, msg.as_string())
    mail.close()

def sendpic(toea, subject, text, f):
    msg = email.MIMEMultipart.MIMEMultipart()
    msg['From'] = emailaddress
    msg['To'] = toea
    msg['Date'] = email.Utils.formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(email.MIMEText.MIMEText(text))
    part = email.MIMEBase.MIMEBase('application', "octet-stream")
    part.set_payload( open(f,"rb").read() )
    email.Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
    msg.attach(part)
    mail = smtplib.SMTP_SSL(smtpserver)
    mail.login(emailaddress, password)
    mail.sendmail(emailaddress, toea, msg.as_string())
    mail.close()

def takepic(groupnum):
    try:
        os.remove("%s.bmp" % groupnum)
    except:
        pass
    hwnd = win32gui.FindWindow(None, "RACE AGAINST TIME - GROUP %s" % groupnum)
    if not hwnd:
        return 'Window not found'
    win32gui.SendMessage(hwnd, win32con.WM_SETFOCUS, None, None)
    time.sleep(0.1)
    l,t,r,b=win32gui.GetWindowRect(hwnd)
    h=b-t
    w=r-l
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    bmpname = '%s.bmp' % groupnum
    saveBitMap.SaveBitmapFile(saveDC, bmpname)
    return bmpname

if __name__ == "__main__":
    while True:
        msgs = retrieve()
        if msgs != None:
            for x in range(len(msgs)):
                pic = takepic(msgs[x][0].split(" ")[2])
                if pic == 'Window not found':
                    send(msgs[x][1], "Window not found", "Your group's window couldn't be found. Are you out of time?")
                else:
                    sendpic(msgs[x][1], "Current standing of Group %s" % msgs[x][0].split(" ")[2], "Current standing of Group %s" % msgs[x][0].split(" ")[2], pic)
                    print "%s: Picture of Group %s sent to %s." % (time.time(), msgs[x][0].split(" ")[2], msgs[x][1])
                    os.remove(pic)