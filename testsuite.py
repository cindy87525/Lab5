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
	print("step one starts now:")
	t = 0
	for t in range(0, 5): #Blink the LED 5 times with on/off intervals of 500ms
		time.sleep(0.5) #interval of 0.5 sec
		GPIO.output(17,1) #turn on
		time.sleep(0.5) #interval of 0.5 sec
		GPIO.output(17,0) #turn off
		t = t + 1
	print("LED sensor:")
	for x in range(0, 50): #50 times 0.1 sec = 5 seconds
		values = mcp.read_adc(0) #read the output of the Grove light sensor
		print(values)
		if values > 400: #threshold value
			print("bright")
		else:
			print("dark")
		time.sleep(0.1) #interval of 0.1sec
		x = x + 1

	y = 0

	for y in range(0, 4): #step 3: Blink the LED 4 times with on/off intervals of 200ms.
	        time.sleep(0.2) #intervals of 200ms
	        GPIO.output(17,1) #turn on
	        time.sleep(0.2) #intervals of 200ms
	        GPIO.output(17,0) #turn on
	        y = y + 1
	x = 0
	print("Sound sensor") #step 4
	for x in range(0, 25): #if we keep tabbing the sound sensor, the entire duration of this step will be 25*0.2 = 5sec
		values = mcp.read_adc(1) #read the output of the Grove sound sensor
		print(values)
		if values > 600: #threshold value
			GPIO.output(17,1) #turn on
			time.sleep(0.1)
			GPIO.output(17,0) #turn off
		time.sleep(0.1)
		x = x + 1

	t = 0
	for t in range(0, 4): #step 5: Blink the LED 4 times with on/off intervals of 200ms
	        time.sleep(0.2)
	        GPIO.output(17,1) #turn on
	        time.sleep(0.2)
	        GPIO.output(17,0) #turn off
	        t = t + 1
