import discord
import responses


def run_discord_bot():
    TOKEN = "MTExNTU2Mzk2MDE1NDk4MDM3Mw.GCnIjE.6LG88x5SsexQcxYqvjY55Xjn1sVU-6zKTxWIw4"
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        try:
            response = responses.handle_response(user_message)
            await message.channel.send(response)
        except Exception as e:
            print(e)

        print(f"{username} said:'{user_message}'({channel} )")

    client.run(TOKEN)
