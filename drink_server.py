'''
    This program should run on startup of the raspberry pi.  It monitors pubnub for drink requests and
    converts these requests into hardware commands for the raspberry pi.  The raspberry pi is connected
    to pumps which will dispense drinks when activated
'''
from pubnub_interface import Message_Handler
import time
import pickle
import json
from drink_helper import State, Recipe


class Drink_Server:
    def __init__(self):
        # Should load saved settings which are stored in the static State class
        State.load_state()
        
        self.message_handle = Message_Handler(localId='server', intendedReceiver='client')
        self.run()

    def run(self):
        # Continually check to see if a request has been received, then process it.
        while (True):
            if self.message_handle.message_queue:
                # Loop through the received messages and process each one
                while self.message_handle.message_queue:
                    self.process_request(self.message_handle.message_queue.pop(0))
            
        # TODO READ INPUT FROM RASPBERRY PI
            print("server running")
            print("State ingredients are " + str(State.ingredients))
            print("State recipes are " + str(State.recipes))
            print("State inventory is " + str(State.inventory))
            time.sleep(3)

    def process_request(self, data):
        
        request_sender = data[0]  # Sender is first element of tuple
        request_type = data[1]  # Request_type is second element of tuple
        request_data = data[2]  # Data is third element of tuple, should already be json decoded
        
        
        # Getter methods that return the current State values to the requester
        if request_type == "get_inventory":
            self.message_handle.fireMessage(request_type="set_inventory",receiver=request_sender, jsonable_obj=State.inventory)
            
        elif request_type == "get_ingredients":
            self.message_handle.fireMessage(request_type="set_ingredients",receiver=request_sender, jsonable_obj=State.ingredients)
            
        elif request_type == "get_recipes":
            jsonable_recipes = [recipe.dict_obj() for name, recipe in State.recipes.items()]
            self.message_handle.fireMessage(request_type="set_recipes", receiver=request_sender, jsonable_obj=jsonable_recipes)
        
        elif request_type == "make_drink":
            pass
        # These should be the setter methods such as set_ingredients, set_inventory, set_recipes
        else:
            State.process_request(request_type, request_data)
        
        
        
        if request_type == "make_drink":
            pass
        
    def send_request(request_type, receiver, data_object):
        self.message_handle.fireMessage(request_type=request_type, receiver=receiver, jsonable_obj=data_object)
    def send_drink_signals():
        pass
    def populate_lcd_screen():
        pass
    def receive_lcd_inputs():
        pass

if __name__ == "__main__":
    server_instance = Drink_Server()
