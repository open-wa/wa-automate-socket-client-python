from src import Client

if __name__ == '__main__':
    NUMBER = 'TEST_PHONE_NUMBER@c.us'

    client = Client('http://localhost:8085/')


    def newMessageHandler(message):
        print(message)


    client.onMessage(newMessageHandler)
    client.sendText(NUMBER, "this is a text")
    message_id = client.sendAudio(NUMBER, "https://download.samplelib.com/mp3/sample-3s.mp3")
    print(message_id)
    print(client.getHostNumber())
