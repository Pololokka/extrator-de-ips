import re

with open(r"C:\Users\vitor\Desktop\mentoria\extrator-ip\ip-mockado.txt") as ipDoc:
    ipRaw = ipDoc.readlines()
    
txtFile = open("listaIPs.txt","w+")
    
schema = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})') 

for line in ipRaw:
    ip = re.findall( schema, line )
    if ip:
        for i in ip:
            txtFile.write(i + "\n")