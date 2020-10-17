import paho.mqtt.client as mqtt
import time

broker_address = "localhost"
port = 8883
keep_alive_time = 60
topic = "new/temp"


#path to CA crt
CA_CERT = "ca.crt"
#CLIENT_CERT = ""
#CLIENT_KEY = "" 
#CIPHERS = "" 


def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc) )
    if client._clean_session == False:
        print("session present flag: " + str(flags['session present']) )

    else:
        print("Starting  a clean session")
 


def on_publish(client, userdata, mid):
    print("Successfully published!!!")


def on_message(client, userdata, msg):
    print("topic: " + msg.topic )
    print("payload: " + str(msg.payload) )
    print("qos: " + str(msg.qos) )
    print("retain: " + str(msg.retain))


def on_disconnect(client, userdata, rc):
    print("Disconnected with result code: " + str(rc) )


def on_log(client, userdata, level, buf):
    print("log: " + buf)


client = mqtt.Client("client_test1", True, None )
client.on_connect = on_connect
client.on_publish = on_publish
client.on_message = on_message
client.on_disconnect = on_disconnect
client.on_log = on_log





client.tls_set(CA_CERT)
#username_pw_set(username, password=None)
#will_set(topic, payload=None, qos=0, retain=False)


client.connect(broker_address, port, keep_alive_time)

client.loop_start()

i=0
while i < 10:    
    client.publish(topic, "Hello", 2, False)
    time.sleep(4)
    i+=1
    


client.disconnect()
client.loop_stop()