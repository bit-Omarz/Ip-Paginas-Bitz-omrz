import socket

def get_hostname_IP(): #Aquí escribireis la direccion host que querais.
    hostname = input("Ingrese la dirección del sitio web(URL):") 
    try:
        print (f'Hostname: {hostname}')
        print (f'IP: {socket.gethostbyname(hostname)}')
    except socket.gaierror as error:
        print (f'Nombre de host no válido, el error generado es {error}')

get_hostname_IP()
