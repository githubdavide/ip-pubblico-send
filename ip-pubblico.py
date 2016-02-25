#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request,smtplib,time

# Tempo di attesa in secondi tra due controlli
attesa = 600

# Parametri per invio email
destinatario = "email_destinataio@gmail.com"
mittente = 'email_mittente@gmail.com'
username = 'email_mittente@gmail.com'
password = 'password'

# Altre variabili
MemoriaIp=""
conta = 0

while True:
	conta += 1
	print ("**********************************")
	print ("Controllo n. %i" % conta)


# Legge IP pubblico
	socks = urllib.request.urlopen("http://ipecho.net/plain")
	ReadIP = socks.read()
	ReadIP.decode("utf-8")
	IP = ReadIP.decode("utf-8")
	socks.close()    
	print ("Indirizzo ip assegnato :",MemoriaIp)
	if IP != MemoriaIp:
	
# Comunica nuovo IP a video
		print ("Rilevato nuovo IP %s" % IP)
	elif IP == MemoriaIp: 
		break	
	  
# Ricorda IP per verifica cambiamento
	MemoriaIp = IP
  
# Prepara variabili per email
oggetto = 'Notifica IP %s' % ReadIP
testo = 'Il tuo IP: %s' % ReadIP
header  = 'From: %s\n' % mittente
header += 'To: %s\n' % destinatario 
header += 'Subject: %s\n\n' % oggetto
msg = header + testo

# Invia email 
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.ehlo()
server.login(username,password)
server.sendmail(mittente, destinatario, msg)
server.quit()
time.sleep(attesa)
