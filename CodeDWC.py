import RPi.GPIO as GPIO
import smbus
import time
#Datenbanken importieren

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIOS einstellen



def read(control):
	bus = smbus.SMBus(1)
	adresse = 0x48
	write = bus.write_byte_data(adresse, control, 0)
	read = bus.read_byte(adresse)
	return read
	#Temp und Licht Sensor abfragen

if True:
	licht = read(0x41)
	temperatur = read(0x42)
	poti = read(0x00)
	if temperatur <= 160:
		GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
		time.sleep(200)
		GPIO.output(10, GPIO.HIGH)
		#Pumpe anstellen und nach 200 Sekunden ausstellen falls die Temperatur zu hoch ist (So kann Wärme besser gepuffert werden da Wasser gleichmässig erwärmt wird, nicht nur obere Schichten)
	else:
		print("3", temperatur)
		#Pumpe nicht anstellen

def water():
	GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
	time.sleep(10)
	GPIO.output(10, GPIO.HIGH)
	#Pumpe anstellen und nach 10 Sekunden ausstellen um Duenger zu verteilen und damit Duenger sich nicht festsetzt

water()
#Pumpe wird bei jedem Durchgang des Programmes fuer 10 Sekunden angestellt, wenn es Warm ist, bleibt Pumpe fuer 200 Sekunden an