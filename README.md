## Project Description

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)


### pyteleprint

pyteleprint is a package for remote prints, notification and alerts for python programs. The notification mechanism is done via Telegram.

### Why should I use this?

This is meant for users who want print() to be a remote notification and alert mechanism if they are not present at their workstation when the program is being executed or for a persisting python application.

### Features

* Remote alerts
* Remote print
* Remote notification

### Requirements

* Requires Python -v >= 3.4.0 
* Telegram App

### Installation

```python
$ pip install pyteleprint
```

### Initial Preparations

The Telegram app must be installed into your mobile system.

First, create a personal bot using (@BotFather). Once the creation process is done, you will receive an API token. Note this API Token for further use.


### Using pyteleprint

Create a new script or use shell to execute the following code

```python
from pyteleprint.printer.chat_extract import ChatIDExtractor

API_TOKEN = "YOUR_NEW_BOT_API_TOKEN" # Obtained from creating a bot through BotFather
ChatIDExtractor(API_TOKEN).start()
```

Once the script is executed, the program would start polling for messages to get chat id. Send a message to your new bot. This will help the program extract the chat id. Use this chat id to send notifications and alerts.

If in future, you delete or lose the chat thread, you can redo the above process to get the new chat id.

This chat id can be used statically in any application at any point in time iff the chat thread with the bot exists. But, if the user deletes the chat with their bot then they have to re-extract the chat id since there would be a new chat thread to communicate with the bot.

Now, you have the API Token and the chat id with you, use them to create a Printer object in your scripts and use the print() method to send notifications,prints and alerts.

```python
from pyteleprint.printer.printer import Printer

API_TOKEN = "YOUR_BOT_API_TOKEN"
CHAT_ID = 12345 # Chat id obtained from ChatIDExtractor().start()
p = Printer(API_TOKEN,CHAT_ID)

p.print("Hello World")
```