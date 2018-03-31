from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
 
pnconfig = PNConfiguration()


# Networking setings
pnconfig.subscribe_key = 'sub-c-2b45be56-316e-11e8-aaf1-0a34c056106f'
pnconfig.publish_key = 'pub-c-ffe97a87-aa34-43bd-98d9-b977d8a65148'

serverChannel = "TestChannel"
localId = "client"


pubnub = PubNub(pnconfig)

def fireMessage(intendedReciver, dictionary):
    pubnub.publish().channel(serverChannel).message({'id' : intendedReciver, 'data' : dictionary}).async(DrinkMachinePublishCallback)

def messageRecived(dictionary):
    if (dictionary['type'] == 'drink_data'):
        pass
    pass

 
def DrinkMachinePublishCallback(envelope, status):
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
            messageRecived(message.message.get('data'))
pubnub.add_listener(DrinkMachineSubscribeCallback())
pubnub.subscribe().channels(serverChannel).execute()


fireMessage('server', {'type' : 'request_drink_data'})
