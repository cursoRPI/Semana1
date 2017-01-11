import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
def parpadea():
	print("Inicia parpadeo...")
	i=1
	while i<=10:
		GPIO.output(7,False)
		time.sleep(1)
		GPIO.output(7,True)
		time.sleep(1)
		print(i)
		i=i+1
	print("Termina parpadeo")
	GPIO.cleanup()
parpadea()
