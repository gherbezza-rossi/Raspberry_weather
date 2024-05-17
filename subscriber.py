from paho.mqtt import client as mqtt
import logging
from serial1 import maskOn, maskOff

def on_subscribe(client, userdata, mid, reason_code_list, properties):
    if reason_code_list[0].is_failure:
        print("errore ", reason_code_list[0])
    else:
        print("riuscito ", reason_code_list[0])

def on_connect(client, userdata, flags, reason_code, properties):
    print("connected ", reason_code)
    client_mqtt.subscribe("wee/#")

def on_message(client, userdata, msg):
    print(f"recived: \n\topic: {msg.topic},\tpayload: {msg.payload.decode()}")
    if msg.payload.decode() == "on":
        maskOn()
    else:
        maskOff()


client_mqtt = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

logger = logging.getLogger(__name__)
client_mqtt.enable_logger(logger)

client_mqtt.on_connect = on_connect
client_mqtt.on_subscribe = on_subscribe
client_mqtt.on_message = on_message

client_mqtt.user_data_set([])
client_mqtt.connect("localhost", 1883, 60)

client_mqtt.loop_forever()
