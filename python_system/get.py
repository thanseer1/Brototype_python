import requests as req
import shutil
import psutil

p=req.get("https://www.google.com")

print(p)

path="D:\\bootcamp1c"

du=shutil.disk_usage(path)
print(du)

s=(du.free/du.total)*100

print(s)
sn=psutil.cpu_percent(1)
print(sn)
