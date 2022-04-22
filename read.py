#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        while(True):
                #print("Waiting for you to scan an RFID sticker/card")
                id = reader.read_id()
                print("The ID for this card is:", id)
        
finally:
        GPIO.cleanup()