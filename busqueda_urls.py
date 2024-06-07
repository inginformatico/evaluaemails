# Codigo de ejemplo de parseo de cabeceras de correo con libreria mail y busqueda de urls
# JTorres 2024

import re # Expresiones regulares
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
print('Lista de urls encontradas')
print('--------------------------------------------------------------------')
texto = msg2.get_body(preferencelist=('html', 'html')).as_string()
patron = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
outs = re.findall(patron,texto)

for i in outs:
        print(i)


