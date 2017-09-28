#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Librerias requeridas para correr aplicaciones basadas en Flask
from flask import Flask, jsonify, make_response
import subprocess

app = Flask(__name__)

# Web service que se invoca al momento de ejecutar el comando
# curl http://localhost:5000
@app.route('/',methods = ['GET'])
def index():
	return "Hola"

# Este metodo retorna la lista de sistemas operativos soportados por VirtualBox
# Los tipos de sistemas operativos soportados deben ser mostrados al ejecutar 
# el comando
# curl http://localhost:5000/vms/ostypes
# Este es el codigo del item 1
@app.route('/vms/ostypes',methods = ['GET'])
def ostypes():
	output = "Work to be done\n"
	# Tu codigo aqui
	return output

# Este metodo retorna la lista de maquinas asociadas con un usuario al ejecutar
# el comando
# curl http://localhost:5000/vms
# Este es el codigo del item 2a
@app.route('/vms',methods = ['GET'])
def listvms():
	output = subprocess.check_output(['VBoxManage','list','vms'])
	return output

# Este metodo retorna aquellas maquinas que se encuentran en ejecucion al 
# ejecutar el comando
# curl http://localhost:5000/vms/running
# Este es el codigo del item 2b
@app.route('/vms/running',methods = ['GET'])
def runninglistvms():
	output = "Work to be done\n"
	# Tu codigo aqui
	return output

# Este metodo retorna las caracteristica de una maquina virtual cuyo nombre es
# vmname 3.
@app.route('/vms/info/<vmname>', methods = ['GET'])
def vminfo(vmname):
	output = "Work to be done\n"
	# Tu codigo aqui
	return output

# Usted deberá realizar además los items 4 y 5 del enunciado del proyecto 
# considerando que:
# - El item 4 deberá usar el método POST del protocolo HTTP
# - El item 5 deberá usar el método DELETE del protocolo HTTP
	

if __name__ == '__main__':
        app.run(debug = True, host='0.0.0.0')
