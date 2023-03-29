import paho.mqtt.client as mqtt
import time


def main(ip: str, port: int, protocol:str) -> None:
    """
    ip: The ip of the broker.
    port: The port on the broker to connect to.
    protocol: If using websockets pass `websockets`. To use `tcp` leave empty.
    """
    if protocol not in ("websockets", None):
        raise Exception("Only allowed `websockets` for protocol.")
    client = mqtt.Client(transport=protocol)
    client.connect(ip, port)
    
    for i in range(2):
        if i %2 ==0:
            client.publish("getReal3D/wandButtonDown", True)
        else:
            client.publish("getReal3D/wandButtonUp", True)
            
        print("published", i)
        time.sleep(1)


if __name__ == '__main__':
    main("127.0.0.1", 80, "websockets")
