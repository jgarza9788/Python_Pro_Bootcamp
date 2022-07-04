from twilio.rest import Client


# TWILIO_SID = YOUR TWILIO ACCOUNT SID
# TWILIO_AUTH_TOKEN = YOUR TWILIO AUTH TOKEN
# TWILIO_VIRTUAL_NUMBER = YOUR TWILIO VIRTUAL NUMBER
# TWILIO_VERIFIED_NUMBER = YOUR TWILIO VERIFIED NUMBER


class NotificationManager:

    def __init__(self, config_data):
        
        self.TWILIO_SID = config_data["TWILIO"]["SID"]
        self.ACCOUNT = config_data["TWILIO"]["ACCOUNT"]
        self.AUTH_TOKEN = config_data["TWILIO"]["AUTH_TOKEN"]
        self.to = config_data["TWILIO"]["TO"]


        self.client = Client(self.ACCOUNT,self.AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            messaging_service_sid=self.TWILIO_SID, 
            body=message,
            to= self.to,
        )
        # Prints if successfully sent.
        print(message.sid)
    
    def create_sms_spam(self, phones,message):
        pass

        for i in range(len(phones)):
            try:
                twilio_message = self.client.messages.create(
                    messaging_service_sid=self.TWILIO_SID, 
                    body=message,
                    to= "+" + str(phones[i]),
                )
                # Prints if successfully sent.
                print(twilio_message.sid)
            except Exception as e:
                print(str(e))


        # try:
        #     message = self.client.messages.create(
        #         messaging_service_sid=self.TWILIO_SID, 
        #         body=message,
        #         to= to,
        #     )
        #     # Prints if successfully sent.
        #     print(message.sid)
        # except:
        #     print("unable to send message")
        #     return None