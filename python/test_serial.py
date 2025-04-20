#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Le Raspbery Pi demande une information à l'Arduino,
# puis il affiche la réponse à l'écran

import serial  # bibliothèque permettant la communication série
import time    # pour le délai d'attente entre les messages



def GetTemp(ser):
   ser.write(b'T\n')
   line = ser.readline() # lire la ligne recue
   t = float(line)
   return t
def GetHum(ser):
   ser.write(b'H\n')
   line = ser.readline() # lire la ligne recue
   h = float(line)
   return h

if __name__ == "__main__":
   ser = serial.Serial('/dev/ttyACM0', 9600)
   time.sleep(3)   #on attend un peu, pour que l'Arduino soit prêt.
   print("Température = ",GetTemp(ser))
   print("Humidité    = ",GetHum(ser))