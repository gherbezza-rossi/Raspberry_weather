from paho.mqtt import client as mqtt
import logging
from serial_to_arduino import light_regulation, soil1_regulation, soil2_regulation, windows_regulation

root = "weather/"


def on_subscribe(client, userdata, mid, reason_code_list, properties):
    if reason_code_list[0].is_failure:
        print("errore ", reason_code_list[0])
    else:
        print("riuscito ", reason_code_list[0])


def on_connect(client, userdata, flags, reason_code, properties):
    print("connected ", reason_code)
    client_mqtt.subscribe(root + "#")


def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()

    print(f"received: \n\ttopic: {topic},\tpayload: {payload}")
    
    if topic == root + "Light":
        light_regulation(payload)
    elif topic == root + "SOILMOISTURE1":
        soil1_regulation(payload)
    elif topic == root + "SOILMOISTURE2":
        soil2_regulation(payload)
    elif topic == root + "PM25_CH1":
        windows_regulation(payload)


client_mqtt = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

logger = logging.getLogger(__name__)
client_mqtt.enable_logger(logger)

client_mqtt.on_connect = on_connect
client_mqtt.on_subscribe = on_subscribe
client_mqtt.on_message = on_message

client_mqtt.user_data_set([])
client_mqtt.connect("192.168.0.107", 1883, 60)

client_mqtt.loop_forever()
