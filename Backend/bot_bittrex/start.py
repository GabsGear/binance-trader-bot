#!/usr/bin/python

import os
import psutil
import MySQLdb as mysql
import shlex, subprocess
import time as t

def main():
	while(True):
		startBots()
		t.sleep(60)

def startBots():
	data = getConfigBots()
	for d in data:
		if(verifyBot(d[1]) == False):
			if(d[2] =="bittrex"):
				command_line = "python /home/bittrex/main.py "+str(d[0])+" &>/dev/null &"
				os.system(command_line)
			else:
				command_line = "python3 /home/binance/src/main.py "+str(d[0])+" &>/dev/null &"
				os.system(command_line)

def verifyBot(pid):
	return psutil.pid_exists(pid)

def deleteLogs():
	files = os.listdir('/home/logs')
	for f in files:
		os.remove('/home/logs/'+str(f))


def getConfigBots():
	try:
		db = mysql.connect(host="localhost", user="root", passwd="libano252528", db="protrader")
		cursor = db.cursor()
		query = ("SELECT id, pid, exchange FROM bot")
		cursor.execute(query)
		data = cursor.fetchall()
		cursor.close()
		return data
	except:
		print("Erro getConfigBots.")


main()