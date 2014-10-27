from pusherclient import Pusher
import time
global pusher # ugh

def buzz(data):
  print 'bzzzzzz'

def bind_to_channel(data):
  channel = pusher.subscribe('doorbell')
  channel.bind('buzz', buzz)
  
pusher = Pusher('157ecece8ea69c91ccc6')
pusher.connection.bind('pusher:connection_established', bind_to_channel)
pusher.connect()

while True:
  time.sleep(1)
