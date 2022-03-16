from src import Client

if __name__ == '__main__':
    NUMBER = 'TEST_PHONE_NUMBER@c.us'

    client = Client('http://localhost:8085/')


    def printResponse(message):
        print(message)


    # Listening for events
    client.onMessage(printResponse)

    # Executing commands
    client.sendText(NUMBER, "this is a text")

    # Sync/Async support
    print(client.getHostNumber())  # Sync request
    client.sendAudio(NUMBER, "https://download.samplelib.com/mp3/sample-3s.mp3", sync=False, callback=printResponse)  # Async request. Callback is optional
