import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
left_led=29
right_led=31
left_in=33
right_in=35
GPIO.setup(left_led,GPIO.OUT)
GPIO.setup(right_led,GPIO.OUT)
GPIO.setup(left_in,GPIO.IN)
GPIO.setup(right_in,GPIO.IN)
while(True):
    val=GPIO.input(left_in)
    if(val==GPIO.LOW):
        GPIO.output(left_led,True)
    else:
        GPIO.output(left_led,False)
    val=GPIO.input(right_in)
    if(val==GPIO.LOW):
        GPIO.output(right_led,True)
    else:
        GPIO.output(right_led,False)
        

