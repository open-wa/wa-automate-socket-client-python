# Remote Socket Client

## How to:

1. Run the EASY API

```bash
> npx @open-wa/wa-automate --socket -p 8085 -k api_key
```

Note: `--socket` flag is required!!

2. Sample code:

```python
from wa_automate_socket_client import Client

NUMBER = 'TEST_PHONE_NUMBER@c.us'

client = Client('http://localhost:8085/')


def newMessageHandler(message):
    print(message)


client.onMessage(newMessageHandler)
client.sendText(NUMBER, "this is a text")
message_id = client.sendAudio(NUMBER, "https://download.samplelib.com/mp3/sample-3s.mp3")
print(message_id)
print(client.getHostNumber())
```