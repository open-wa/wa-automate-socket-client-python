# Remote Socket Client

## How to:

1. Run the EASY API

```bash
> npx @open-wa/wa-automate --socket -p 8085
```

Note: `--socket` flag is required!!

2. Sample code:

```python
from wa_automate_socket_client import Client

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
client.sendAudio(NUMBER,
                 "https://download.samplelib.com/mp3/sample-3s.mp3",
                 sync=False,
                 callback=printResponse)  # Async request. Callback is optional
```