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
from pump_driver import DrivePump
from lcd_driver import DriveLCD

SECONDS_PER_TIME_UNIT = 10


class Drink_Server:
    def __init__(self):
        # Should load saved settings which are stored in the static State class
        State.load_state()
        # Start listener for drinks being sent to the pump
        self.DP = DrivePump()
        self.DP.start()
        
        self.message_handle = Message_Handler(localId='server', intendedReceiver='client')
        # Start listener for lcd requests
        self.LD = DriveLCD()
        self.LD.start()
        # Listen for requests and button inputs
        self.run()

    def run(self):
        # Continually check to see if a request has been received, then process it.
        print("server running")
        print("State ingredients are " + str(State.ingredients))
        print("State recipes are " + str(State.recipes))
        print("State inventory is " + str(State.inventory))
        while (True):
            if self.message_handle.message_queue:
                # Loop through the received messages and process each one
                while self.message_handle.message_queue:
                    self.process_request(self.message_handle.message_queue.pop(0))
            
        # TODO READ INPUT FROM RASPBERRY PI
            if self.LD.make_drink_queue:
                # Remove the recipe dict and send it 
                drink_obj = self.LD.make_drink_queue.pop(0)
                self.send_drink_signals(drink_obj)
                
            time.sleep(3)

    def process_request(self, data):
        
        request_sender = data[0]  # Sender is first element of tuple
        request_type = data[1]  # Request_type is second element of tuple
        request_data = data[2]  # Data is third element of tuple, should already be json decoded
        print("received " + str(request_type))
        print("from " + str(request_sender))
        print("data " + str(request_data))
        
        # Getter methods that return the current State values to the requester
        if request_type == "get_inventory":
            # Returns a JSON object of the slot information in the inventory dictionary
            self.message_handle.fireMessage(request_type="set_inventory",receiver=request_sender, jsonable_obj=State.inventory)
            
        elif request_type == "get_ingredients":
            # Returns a JSON object of the ingredients list
            self.message_handle.fireMessage(request_type="set_ingredients",receiver=request_sender, jsonable_obj=State.ingredients)
            
        elif request_type == "get_recipes":
            # Returns a JSON object of the recipes list
            # The recipe class is first converted into a dictionary
            jsonable_recipes = [recipe.dict_obj() for name, recipe in State.recipes.items()]
            self.message_handle.fireMessage(request_type="set_recipes", receiver=request_sender, jsonable_obj=jsonable_recipes)
        
        elif request_type == "make_drink":
            # request_data should contain a recipe_dict object
            self.send_drink_signals(request_data)
        # These should be the setter methods such as set_ingredients, set_inventory, set_recipes
        else:
            State.process_request(request_type, request_data)
        
        
    def send_request(self, request_type, receiver, data_object):
        self.message_handle.fireMessage(request_type=request_type, receiver=receiver, jsonable_obj=data_object)
        
    def send_drink_signals(self, recipe_obj):
        '''
        recipe_obj: Should be a dictionary produced from a Recipe with the recipe_dict method.
        The ingredient names will be converted to slot names based off of the current State.inventory
        settings.  The time units will be multiplied by their conversion constant.  The finished
        dictionary will be added to the drink pump queue where it will be processed when the pumps
        are free.
        '''
        print("Making drink: " + recipe_obj['recipe_name'])
        # Converted should have format "slot_name" : pump time in seconds when done
        converted = {}
        # Iterate through ingredients and convert ingredient name to slot name
        for slot, ingredient in State.inventory.items():
            if ingredient in recipe_obj:
                converted[slot] = recipe_obj[ingredient] * SECONDS_PER_TIME_UNIT
        self.DP.pump_queue.append(converted)
             
    def populate_lcd_screen():
        pass
    def receive_lcd_inputs():
        pass

if __name__ == "__main__":
    server_instance = Drink_Server()
