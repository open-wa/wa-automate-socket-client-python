# Remote Socket Client

## How to:

1. Run the EASY API. Note: `--socket` flag is required!!

```bash
> npx @open-wa/wa-automate --socket -p 8085 -k secure_api_key

# OR use docker

> docker run openwa/wa-automate --socket -p 8085 -k secure_api_key
```

2. Install 

```bash
> pip install wa-automate-socket-client
```

3. Sample code:

```python
from wa_automate_socket_client import Client

NUMBER = 'TEST_PHONE_NUMBER@c.us'

client = Client('http://localhost:8085/', 'secure_api_key')


def printResponse(message):
    print(message)


# Listening for events
client.onMessage(printResponse)

# Executing commands
client.sendText(NUMBER, "this is a text")

# Sync/Async support
print(client.getHostNumber())  # Sync request
client.sendAudio(NUMBER,
                 "https://download.samplelib.com/mp3/sample-3s.mp3",
                 sync=False,
                 callback=printResponse)  # Async request. Callback is optional
```
