# Lost My Doorbell - Client
A Python script, running on a Raspberry Pi, which eats WebSocket events from Pusher and converts them into door openings.

## Getting Started
- `pip install https://github.com/ekulyk/PythonPusherClient/archive/master.zip` (may require `sudo`)
- `PUSHER_KEY=XXX python poll.py`

## Circuitry
You're going to need a relay sitting on GPIO pin 11 of your Raspberry Pi. This will be switched for 3 seconds whenever we get an event from Pusher.
