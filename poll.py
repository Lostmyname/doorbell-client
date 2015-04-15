from pusherclient import Pusher
import RPi.GPIO as GPIO
import time
import os
import sys
global pusher # ugh

pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

try:
  def buzz(data):
    GPIO.output(pin, True)
    print 'Door open'
    time.sleep(3)
    GPIO.output(pin, False)
    print 'Door shut!'

  def bind_to_channel(data):
    channel = pusher.subscribe('doorbell')
    channel.bind('buzz', buzz)

  pusher = Pusher(os.environ['PUSHER_KEY'])
  pusher.connection.bind('pusher:connection_established', bind_to_channel)
  pusher.connect()

  while True:
    time.sleep(1)

except:
  print sys.exc_info()[0]
  GPIO.cleanup()
