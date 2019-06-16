from proxybroker import Broker
import asyncio
import yaml
import os


def serve():
    loop = asyncio.get_event_loop()
    input_broker = {k: v for k, v in config["broker"].items() if v != "Default"}
    broker = Broker(**input_broker, loop=loop)

    input_serve = {k: v for k, v in config["serve"].items() if v != "Default"}
    broker.serve(**input_serve)

    print("Server started at http://%s:%d" % (input_serve["host"], input_serve["port"]))

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        broker.stop()
    finally:
        loop.stop()
        loop.close()


if __name__ == "__main__":
    file = "../config.yml" if os.path.isfile("../config.yml") else "config.yml"
    with open(file, "r") as ymlfile:
        config = yaml.safe_load(ymlfile)

    serve()
