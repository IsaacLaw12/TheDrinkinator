from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from keychain import keychain
import time
import sys
from config import local_id
pnconfig = PNConfiguration()


# Networking setings
pnconfig.subscribe_key = keychain["pn_subscribe_key"]
pnconfig.publish_key = keychain["pn_publish_key"]

serverChannel = "TestChannel"
# Change to client or server depending on deployment location
localId = "server"


class Message_Handler():
    
    # Static class variable to hold incoming messages until processed
    message_queue = []
    
    def __init__(self, intendedReciver, localId):
        self.intended_receiver = intendedReciver
        self.pubnub = PubNub(pnconfig)
        self.pubnub.add_listener(DrinkMachineSubscribeCallback())
        self.pubnub.subscribe().channels(serverChannel).execute()

    def fireMessage(self, receiver=self.intended_receiver, dictionary):
        '''
        Send the object passed to dictionary to receiver.
        Default to the stored intended_receiver
        '''
        self.pubnub.publish().channel(serverChannel).message({'id': receiver, 'data': dictionary}).async(self.DrinkMachinePublishCallback)

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
        if (idValue == localId):
            Message_Handler.message_queue.append(message.message.get('data'))


if __name__ == "__main__":
    mh = Message_Handler()
    mh.fireMessage('server', {'type': 'request_drink_data'})
    while True:
        if Message_Handler.message_queue:
            print(Message_Handler.message_queue)
            sys.exit(0)
        time.sleep(10)
