'''
Created on Apr 3, 2014
 
@author: Kevin
'''
import RPi.GPIO as GPIO
import time
 
class Joystick(object):
     
    def __init__(self):
        self.SPICLK = 18
        self.SPIMISO = 23
        self.SPIMOSI = 24
        self.SPICS = 25
        self.LEDBLUE = 3
        self.LEDRED = 4
                                
    def readadc(self, adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
            return -1
        GPIO.output(cspin, True)
          
        GPIO.output(clockpin, False) # start clock low
        GPIO.output(cspin, False) # bring CS low
          
        commandout = adcnum
        commandout |= 0x18 # start bit + single-ended bit
        commandout <<= 3 # we only need to send 5 bits here
        for i in range(5):
            if (commandout & 0x80):
                GPIO.output(mosipin, True)
            else:
                GPIO.output(mosipin, False)
            commandout <<= 1
            GPIO.output(clockpin, True)
            GPIO.output(clockpin, False)
          
        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
            GPIO.output(clockpin, True)
            GPIO.output(clockpin, False)
            adcout <<= 1
            if (GPIO.input(misopin)):
                adcout |= 0x1
          
        GPIO.output(cspin, True)
        adcout >>= 1 # first bit is 'null' so drop it
        return adcout
     
    def main(self):         
        GPIO.setmode(GPIO.BCM)
              
        # set up the SPI interface pins
        GPIO.setup(self.SPIMOSI, GPIO.OUT)
        GPIO.setup(self.SPIMISO, GPIO.IN)
        GPIO.setup(self.SPICLK, GPIO.OUT)
        GPIO.setup(self.SPICS, GPIO.OUT)
        
        GPIO.setup(self.LEDBLUE, GPIO.OUT)    
        GPIO.output(self.LEDBLUE, False)
        GPIO.setup(self.LEDRED, GPIO.OUT)    
        GPIO.output(self.LEDRED, False)
     
    def setLED(self, led, val):
        if(led == 1):
            GPIO.output(self.LEDBLUE, val)
        elif(led == 2):
            GPIO.output(self.LEDRED, val)
    def deactivateLED(self):
        self.setLED(1, False)
        self.setLED(2, False) 