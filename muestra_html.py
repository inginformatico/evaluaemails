# Codigo de ejemplo de parseo de cabeceras de correo con libreria mail y muestra el mensaje como html
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

#Muestro el contenido de los objetos mail
print('--------------------------------------------------------------------')
print('Muestra todo el contenido del mensaje en formato html')
print('--------------------------------------------------------------------')
print( msg2.get_body(preferencelist=('html', 'html')))
