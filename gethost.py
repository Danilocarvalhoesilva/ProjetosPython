#!/usr/bin/python3
# -*- coding: utf-8 -*-
import paramiko
import sys

ip = sys.argv[1]

ssh_client =paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip,username='adm_dsilva',password='samuca2013')

print("#"*20, "INFORMAÇÕES DE MEMÓRIA", "#"*20)
stdin,stdout,stderr=ssh_client.exec_command("free -h | grep 'Mem:' | awk '{print $2}'")
outlines=stdout.readlines()
resp=''.join(outlines)
print(f"➤ Memóia Total: {resp}")

stdin,stdout,stderr=ssh_client.exec_command("free -h | grep 'Mem:' | awk '{print $3}'")
outlines=stdout.readlines()
resp=''.join(outlines)
print(f"➤ Memóia Usada: {resp}")

stdin,stdout,stderr=ssh_client.exec_command("free -h | grep 'Mem:' | awk '{print $4}'")
outlines=stdout.readlines()
resp=''.join(outlines)
print(f"➤ Memóia Disponível: {resp}")







