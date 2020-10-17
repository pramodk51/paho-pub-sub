import paho.mqtt.client as mqtt
import time

broker_address = "localhost"
port = 8883
keep_alive_time = 60
topic = "new/temp"

#path to CA crt
CA_CERT = 'ca.crt'
#CLIENT_CERT = ""
#CLIENT_KEY = "" 
#CIPHERS = "" 



def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc) )
    if client._clean_session == False:
        print("session present flag: " + str(flags['session present']) )

    else:
        print("Starting  a clean session")

    #if connected then subscribe
    client.subscribe(topic,0)   



def on_subscribe(client, userdata, mid, granted_qos):
    print("qos granted for the subscription: " + str(granted_qos) )


def on_message(client, userdata, msg):
    print("Message received!!!!!")
    print("topic: " + msg.topic )
    print("payload: " + str(msg.payload) )
    print("qos: " + str(msg.qos) )
    print("retain: " + str(msg.retain))


def on_disconnect(client, userdata, rc):
    print("Disconnected with result code: " + str(rc) )



def on_unsubscribe(client, userdata, mid):
    print("unsubcribed!!!!!!")


def on_log(client, userdata, level, buf):
    print("log: " + buf)


client = mqtt.Client("client_test3", True, None )
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_disconnect = on_disconnect
client.on_unsubscribe = on_unsubscribe
client.on_log = on_log





client.tls_set(CA_CERT,tls_version=2) 
#username_pw_set(username, password=None)
#will_set(topic, payload=None, qos=0, retain=False)


client.connect(broker_address, port, keep_alive_time)
#loop_forever automatically handles reconnection
client.loop_forever()