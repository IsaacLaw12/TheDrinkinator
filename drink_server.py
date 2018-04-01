'''
    This program should run on startup of the raspberry pi.  It monitors pubnub for drink requests and
    converts these requests into hardware commands for the raspberry pi.  The raspberry pi is connected
    to pumps which will dispense drinks when activated
'''
from pubnub_interface import Message_Handler
import time
import pickle
import json


class Drink_Server:
    def __init__(self):
        # Should load saved settings which are stored in the static State class
        State.load_state()
        
        self.message_handle = Message_Handler(intendedReceiver='client')
        self.run()

    def run(self):
        # Continually check to see if a request has been received, then process it.
        while (True):
            if self.message_handle.message_queue:
                # Loop through the received messages and process each one
                while self.message_handle.message_queue:
                    process_request(self.message_handle.message_queue.pop(0))
                    time.sleep(5)
        # TODO READ INPUT FROM RASPBERRY PI
        time.sleep(5)

    def process_request(data):
        # Assume data is a python dictionary in JSON format
        message = json.loads(data)
        request_type = message['request_type']
        request_data = message['request_data']
        if request_type == "set_slot_data":
            pass
        if request_type == "get_slot_data":
            pass
        if request_type == "set_recipes":
            pass
        if request_type == "get_recipes":
            pass
        if request_type == "set_ingredients":
            pass
        if request_type == "get_ingredients":
            pass
        if request_type == "make_drink":
            pass
        
    def send_request():
        pass
    def send_drink_signals():
        pass
    def populate_lcd_screen():
        pass
    def receive_lcd_inputs():
        pass

if __name__ == "__main__":
    server_instance = Drink_Server()
