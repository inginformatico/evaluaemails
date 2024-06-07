# Codigo de ejemplo de parseo de resumen de cabeceras de correo con libreria mail
# JTorres 2024

import os # manejo sistema operativo
import email # parseo de emails
import argparse # manejo parametros
from email.policy import default

#Leo el fichero del correo como parametro 
parser = argparse.ArgumentParser()

parser.add_argument('-f', '--file',
                        help="""Fichero con el correo""")
args = parser.parse_args()

#Abro el fichero
#Creo el objeto mail a partir del fichero de texto
with open(args.file, 'r') as fp:
        msg2 = email.message_from_file(fp, policy=default)


#borro pantalla
os.system("cls")

print('--------------------------------------------------------------------')
print('Resumen de etiquetas del correo')
print('--------------------------------------------------------------------')
print('Remitente:' + msg2['from'])
print('Destino: ' + msg2['To'])
print('Fecha: ' + msg2['Date'])
print('Asunto: ' + msg2['Subject'])
print('Id del _Mensaje: ' + msg2['Message-ID'])


