# Discord-message-copier

## *How to use*
Export a channel with the [Discord Chat Exporter](https://github.com/Tyrrrz/DiscordChatExporter) and have the exported file in the same directory as main.py. Replace the file.json in the with open() statement on line 31 with your exported file. Then run main.py via terminal.
In discord, do !fetch_messages *ID* , where ID is the channel ID that you want the bot to send the messages to.

Due to limitations within discord, the bot can only send about 1 message per second, so it's gonna take a while lmao.
