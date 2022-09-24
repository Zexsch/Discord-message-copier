import discord, json, threading, time
from discord.ext import commands

# Need to declare bot intents and prefix
intents = discord.Intents.default()
client = commands.Bot(command_prefix='!', intents=intents)

# Shows how much time has passed. Keep in mind print() sends to console.
def count_process():
    count = 0
    while True:
        time.sleep(60)
        count += 60
        print(f'{count} seconds have passed.')

cth = threading.Thread(target=count_process, daemon=True)

# In discord, do !fetch_messages ID
# Where ID is the ID of the channel you want to SEND it to.
# It will error out if you don't give a valid ID.

@client.command()
async def fetch_messages(ctx, channel_ID):
    cth.start()
    
    # You will NEED to replace the file in with open('file.json'...)
    # Example file 'Text channel content.json', just the exported file name.
    # The file HAS to be in the EXACT current directory. This also means the main.py file HAS to be run via terminal,
    # and not through an IDE like VSCode.
    
    with open('file.json', 'r', errors="ignore") as f:
        data = json.load(f)
        messages = data['messages']
        channel = client.get_channel(int(channel_ID))

        for i in range(len(messages)):
            content = messages[i]['content']
            author = f"<@{messages[i]['author']['id']}>"
            attachments = messages[i]['attachments']
            sticker = messages[i]['stickers']
            mentions = messages[i]['mentions']

            # Finds any mention and replaces it with the person being @'ed. This is because in the usual content
            # the mention is for example @carl-bot, and it won't ping the user.
            
            if mentions:
                for i in range(len(mentions)):
                    mentioned_name= f"@{mentions[i]['name']}"
                    mentioned_ID = f"<@{mentions[i]['id']}>"
                    content = content.replace(mentioned_name, mentioned_ID)

            # Since you can't send a sticker with a message, if a sticker is found it'll just send that and ignore the rest.
            if sticker:
                await channel.send(sticker[0]['sourceUrl'])
            else:
                await channel.send(f'{author} : {content}')
                if attachments:
                    for j in range(len(attachments)):
                        await channel.send(attachments[j]['url'])

    print('Finished sending!')
    
    # Get rid of this last bit if you don't want the bot to close whenever it's finished sending.
    # That would make it so that the thread that's counting the time wouldn't stop, so basically don't delete this
    try:
        await client.close()
    except:
        print("EnvironmentError")
        client.clear()

# This bot will HEAVILY spam ping.
# Change out 'TOKEN' for your discord bot token.
# Keep in mind that you will have to enable 'Message content intent' under the Bot panel.
# Also just give the bots admin perms on whatever server it's in.
client.run('TOKEN')