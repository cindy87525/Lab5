import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import RPi.GPIO as GPIO 
import time

#SPI Hardware Configuration
SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
GPIO.setmode(GPIO.BCM) 
GPIO.setup(17,GPIO.OUT)
while True:
	t = 0
	for t in range(0, 5): #Blink the LED 5 times with on/off intervals of 500ms
		time.sleep(0.5) #interval of 0.5 sec
		GPIO.output(17,1) #turn on
		time.sleep(0.5) #interval of 0.5 sec
		GPIO.output(17,0) #turn off
		t = t + 1
	print("LED sensor:")
	for x in range(0, 50):
		values = mcp.read_adc(0)
		print(values)
		if values > 400:
			print("bright")
		else:
			print("dark")
		time.sleep(0.1)
		x = x + 1

	y = 0

	for y in range(0, 4):
	        time.sleep(0.2)
	        GPIO.output(17,1)
	        time.sleep(0.2)
	        GPIO.output(17,0)
	        y = y + 1
	x = 0
	print("Sound sensor")
	for x in range(0, 25):
		values = mcp.read_adc(1)
		print(values)
		if values > 600:
			GPIO.output(17,1)
			time.sleep(0.1)
			GPIO.output(17,0)
		time.sleep(0.1)

	t = 0
	for t in range(0, 4):
	        time.sleep(0.2)
	        GPIO.output(17,1)
	        time.sleep(0.2)
	        GPIO.output(17,0)
	        t = t + 1
