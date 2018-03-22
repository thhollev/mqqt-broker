# mqqt-broker    
A python mosquitto(mqqt) broker.        

## INSTALL
```
sudo pip install -r requirements.txt && sudo pacman -S mosquitto
```

## USAGE     
`./get.py <ip> <topic>`

This will start the broker and listen for incoming messages.

`./send.py <ip> <topic> <message>`

This wil send a message.
