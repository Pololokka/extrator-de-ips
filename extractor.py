import re
import os
from tkinter import messagebox

if(os.path.exists(r".\lista-ips.txt")):
    with open(r".\lista-ips.txt") as ipDoc:
        ipRaw = ipDoc.readlines()
        
    if(os.path.exists(r".\IPs-tratados.txt")):
        os.remove("IPs-tratados.txt")    

    txtFile = open("IPs-tratados.txt","w+")
    
    IParray = []
        
    schema = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})') 

    for line in ipRaw:
        ip = re.findall( schema, line )
        if ip:
            for i in ip:
                IParray.append(i)
    
    IParray = list( dict.fromkeys(IParray) )
    
    for item in IParray:
        txtFile.write(item + "\n")
    
else:
    messagebox.showerror("Erro", "Favor criar um arquivo de texto(.txt) chamado 'lista-ips' no mesmo diretório deste aplicativo")
    