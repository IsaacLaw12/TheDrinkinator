import time
import sys
import json
from keychain import keychain
from drink_helper import Recipe, State

sys.path.insert(0, './python/')

from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub


pnconfig = PNConfiguration()


# Networking setings
pnconfig.subscribe_key = keychain["pn_subscribe_key"]
pnconfig.publish_key = keychain["pn_publish_key"]

serverChannel = "TestChannel"
# Change to client or server depending on deployment location



class Message_Handler():
    
    # Static class variable to hold incoming messages until processed
    #   format: list of (sender, data) tuples.
    message_queue = []
    local_id = "server"
    
    def __init__(self, localId, intendedReceiver):
        Message_Handler.local_id = localId
        self.intended_receiver = intendedReceiver
        self.pubnub = PubNub(pnconfig)
        self.pubnub.add_listener(DrinkMachineSubscribeCallback())
        self.pubnub.subscribe().channels(serverChannel).execute()
    
    def __del(self):
        self.pubnub.remove_listener(DrinkMachinePublishCallback())
        self.pubnub.unsubscribe_all()

    def fireMessage(self, request_type, receiver=None, jsonable_obj="Test Message"):
        '''
        Format: jsonable_obj should be a python object that can be turned into a JSON format
        Send the object passed to jsonable_obj to receiver.
        Default to the stored intended_receiver
        '''
        if not receiver:
            receiver = self.intended_receiver
            
        json_content = json.dumps(jsonable_obj)
        self.pubnub.publish().channel(serverChannel).message({'sender': Message_Handler.local_id, 'id': receiver, 'request_type':request_type, 'data': json_content}).async(self.DrinkMachinePublishCallback)

    def DrinkMachinePublishCallback(self, envelope, status):
        if not status.is_error():
            pass
        else:
            print("PubNub networking error")


class DrinkMachineSubscribeCallback(SubscribeCallback):
    def presence(self, pubnub, presence):
        pass

    def status(self, pubnub, status):
        if status.category == PNStatusCategory.PNUnexpectedDisconnectCategory:
            pass
        elif status.category == PNStatusCategory.PNConnectedCategory:
            pass
        elif status.category == PNStatusCategory.PNReconnectedCategory:
            pass
        elif status.category == PNStatusCategory.PNDecryptionErrorCategory:
            pass

    def message(self, pubnub, message):
        idValue = message.message.get('id')
        if (idValue == Message_Handler.local_id):
            # Add tuple of format (sender, request_type, data) to message_queue, The sender parameter allows
            #   us to send information back.
            Message_Handler.message_queue.append( (message.message.get('sender'), message.message.get('request_type'), json.loads(message.message.get('data'))) )


if __name__ == "__main__":
    ''' 
        This is a test to verify that sending State over pubnub is working.
        Assumed setup: Drink_server is running with name 'server'. State is currently
        cleared for both this client and server.
    '''
    mh = Message_Handler("client", "server")
    State.clear_state()
    print("Cleared state")
    print(State.to_string())
    
    print("Populating State")
    State.add_recipe(Recipe("Apple Juice", [("Water",5),("Apple",2)]))
    State.add_ingredient("Pineapple Juice")
    State.set_inventory("slot_one", "Orange Juice")
    print(State.to_string())
    
    print("Sending State to server")
    mh.fireMessage(request_type="add_ingredients",receiver='server', jsonable_obj=State.ingredients)
    jsonable_recipes = [recipe.dict_obj() for name, recipe in State.recipes.items()]
    mh.fireMessage(request_type="add_recipes", receiver='server', jsonable_obj=jsonable_recipes)
    mh.fireMessage(request_type="set_inventory", receiver='server', jsonable_obj=State.inventory)
    
    print("Deleting local state")
    State.clear_state()
    print(State.to_string())
    
    print("Restoring local state from server")
    mh.fireMessage(request_type="get_ingredients", receiver="server")
    mh.fireMessage(request_type="get_recipes", receiver="server")
    mh.fireMessage(request_type="get_inventory", receiver="server")
    
    time.sleep(5)
    for x in range(0,3):
        if Message_Handler.message_queue:
            if mh.message_queue:
                # Loop through the received messages and process each one
                while mh.message_queue:
                    data = mh.message_queue.pop(0)
                    State.process_request(data[1],data[2])
                    time.sleep(1)
                            
        time.sleep(10)
    
    print("State is now: ")
    print(State.to_string())
