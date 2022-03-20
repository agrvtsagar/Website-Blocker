import time
from datetime import datetime as dt

hosts_temp = r"C:\Users\Sagar\PycharmProjects\Website-Blocker\hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "bolly4u.yoga", "www.bolly4u.yoga"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        print("Working Hours")
        with open(hosts_temp, 'r+') as files:
            content = files.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    files.write(redirect + " " + website + "\n")
    else:
        with open(hosts_temp, "r+") as files:
            content = files.readline()
            files.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    files.write(line)
        files.truncate()
        print("Free Hours")
    time.sleep(5)
