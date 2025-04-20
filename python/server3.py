from bottle import route, run
from random import randint
import serial  # bibliothèque permettant la communication série
import time    # pour le délai d'attente entre les messages


ser = serial.Serial('/dev/ttyACM0', 9600)


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

@route('/')
def hello():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Station metéo </title>
</head>
<body>
    <h2>Infomations reçues par la station météo :</h2>
    <table>
        <tbody>
          <tr>
            <th scope="row">Humidité(%) = </th>
            <td>"""+str(GetHum(ser)) +"""</td>
          </tr>
          <tr>
            <th scope="row">Température(°C) =</th>
            <td>"""+str(GetTemp(ser))+""" </td>
          </tr>
        </tbody>
      </table>
      
</body>
</html>

"""
run(host='0.0.0.0', port=8585, debug=True)
