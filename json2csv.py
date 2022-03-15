#!/usr/bin/python3
import json
import csv
import os
import subprocess
from time import sleep

abicom_str = """
{
    "mode": "api-generate",
    "export-api-headers-dirs": ".",
    "api-generate": {
        "output": "api-standard.json",
        "is_go": "0",
        "macros": [

        ],
        "is_contain_include": "1",
        "dir": "."
    },
    "api-compare": {
        "is_go": "0",
        "src": ".",
        "is_contain_include": "1",
        "standard_api_json": "api-standard.json",
        "current_api_json": "api-current.json"
    },
    "api-fast-compare": {
        "baseDir": "baseCodeDir",
        "compareDir": "currentCodeDir",
        "macros": [

        ],
        "languages": "all",
        "exDirs": [
            ".git",
            ".pc",
            "patches"
        ]
    }
}
"""

pjcom_str = """
{
    "project": "dde-dock",
    "version": "5.5.13",
    "headers-dir": "/usr/include/dde-dock"
}
"""

pjcom_json = json.loads(pjcom_str)
abicom_json = json.loads(abicom_str)
abicom_json['api-generate']['dir'] = pjcom_json['headers-dir']

out_file = open('abicom.json', 'w')
json.dump(abicom_json, out_file)

# sleep(0.5)

# # 阻塞调用
# res = subprocess.Popen("deepin-abigail -c '/home/guo/Develop/python-demo/abicom.json'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) # 使用管道
# print(res.stdout.read())  # 标准输出

# res.stdout.close()


file = open("api-standard.json")
csv_file = open("{}.csv".format(pjcom_json['project']), 'w', newline='', encoding='utf-8-sig')  # 解决中文乱码问题
writer = csv.writer(csv_file)
writer.writerow(['Project', 'Version', 'Filepath', 'Uniquefunname', 'Funname', 'Returntype', 'Args'])
for line in file:
    dt = json.loads(line)
    if not dt["Functions"] is None:
        for data in dt["Functions"]:
            writer.writerow([pjcom_json['project'], pjcom_json['version'], dt["Filepath"], data['Uniquefunname'], data['Funname'], data['Returntype'], data['Args']])

csv_file.close()
