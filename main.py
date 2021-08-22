import os
import sys
import serial
import serial.tools.list_ports

def cleanPrint(): #Limpiar pantalla / Clear print
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def searchPortCom():#Busca el puerto COM / Search port COM
    ports = list(serial.tools.list_ports.comports())
    if ports:
        for port in ports:
            print ("-> Puertos encontrados:", port)
            number_port = port[0]
            readDataPortSerie(number_port)
    else:
        print("-> No se encontraron puertos COM.")
        return False

def readDataPortSerie(port):#Lee los datos recibidos desde el puerto COM / Read data from port serie 
    print("-> Recibiendo datos desde", port,":")
    ser = serial.Serial(port, 9600) #Cambiar de acuerdos a los baudios establecidos en la placa
    ser.flushInput()
    while True:
        try:
            lineBytes = ser.readline()
            linea = lineBytes.decode('utf-8').strip()
            print(linea)
        except KeyboardInterrupt:
            break 


def main():

    cleanPrint()
    print("----- EJECUTANDO SCRIPT -----")
    searchPortCom()
        
main()
    
