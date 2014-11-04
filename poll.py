from pusherclient import Pusher
import RPi.GPIO as GPIO
import time
import os
global pusher # ugh

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

try:
  def buzz(data):
    GPIO.output(11, True)
    print 'Door open'
    time.sleep(3)
    GPIO.output(11, False)
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
  GPIO.cleanup()
