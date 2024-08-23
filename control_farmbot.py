from farmbot import Farmbot, FarmbotToken


raw_token = FarmbotToken.download_token("jiroach@ucdavis.edu",
                                        "ebs170FB",
                                        "https://my.farm.bot")
fb = Farmbot(raw_token)

class MyHandler:
    # The `on_connect` event is called whenever the device
    # connects to the MQTT server. You can place initialization
    # logic here.
    #
    # The callback is passed a FarmBot instance, plus an MQTT
    # client object (see Paho MQTT docs to learn more).
    def on_connect(self, bot, mqtt_client):

        request_id1 = bot.find_home()
        print("MOVE_ABS REQUEST ID: " + request_id1)

        request_id2 = bot.send_message("Hello, world!")
        print("SEND_MESSAGE REQUEST ID: " + request_id2)

    def on_change(self, bot, state):
        print("NEW BOT STATE TREE AVAILABLE:")
        print(state)

        print("Current position: (%.2f, %.2f, %.2f)" % bot.position())

        pos = state["location_data"]["position"]
        xyz = (pos["x"], pos["y"], pos["z"])
        print("Same information as before: " + str(xyz))

    def on_log(self, bot, log):
        print("New message from FarmBot: " + log['message'])


    def on_response(self, bot, response):
        print("ID of successful request: " + response.id)


    def on_error(self, bot, response):

        print("ID of failed request: " + response.id)
        print("Reason(s) for failure: " + str(response.errors))



handler = MyHandler()
fb.connect(handler)

#FB operation
print(fb.device_id)
print(fb.position())
for i in range(5):
    fb.move_relative(100, 0 ,0 )
    fb.take_photo()
fb.find_home()