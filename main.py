# Importing the class libraries needed for the disord bot
import discord
import os
import random
import discord.errors
from ec2_metadata import ec2_metadata
# Importing the class library dotenv in order to access our discord bot token. This is a way we can use the token securely.
from dotenv import load_dotenv

# We are just printing the ec2_metadata for region, instance, and public ip address
print(ec2_metadata.region)
print(ec2_metadata.instance_id)
print(ec2_metadata.public_ipv4)


load_dotenv()

# Creating an object named client and calling the dicord library and the Client attribute
client = discord.Client()
# Creating an object named token and channging the context of the TOKEN into a string.
token = str(os.getenv('TOKEN'))

# event is used for the client to listen to an event. An event is when something takes place.


@client.event
# This on_ready() function will log 'Logged in as a bot ...' after the client has gotten the data from discord and the login is successful
async def on_ready():
    print('Logged in as a bot {0.user}'.format(client))

@client.event
# The on_message function is used when the bot receives a message
# Here we are passing through an attribute named message
async def on_message(message):
    # Here we are creating an object named username and converting the authors name into a string and splitting the # and the 0 index off of the string.
    username = str(message.author).split("#")[0]
    # Here we are creating an object named channel and changing the entire context to a string. And getting the channel that the user is sending the message in.
    channel = str(message.channel.name)
    # Here we are creating an object named user_message and changing the entire context to a string. And getting the message that the user sent in the channel.
    user_message = str(message.content)
    # This will print the users message, username, and what channel the user is using in the linux console with EC2 instance
    print(f'Message {user_message} by {username} on {channel}')

    # Created an object named all_channels in order to store all the channel names in an array (list)
    all_channels = ["random", "general", "chat"]

    if message.author == client.user:
        return

    # If statement of the channel is listed in the all_channels object then  you can run the code in this block.
    if channel in all_channels:
        # A nested if statement changing the user message to all lowercase and saying if the users message is hello or hi return the message
        try:

            if user_message.lower() == "hello" or user_message.lower() == "hi":
                # This part of the code is waiting to see what the user says and will respond with this block of code. It includes a formatted string that will return the users username and their ec2_metadata region
                await message.channel.send(f"Hello {username} Your EC2 Data: {ec2_metadata.region}")
                return
                # else if statement, that will change the user's message to all lowercase. If they message "hello world" the discord bot will respond with "hello"
            elif user_message.lower() == "hello world":
                await message.channel.send("hello")
                return
                # else if statement, that will change the user's message to all lowercase and then check if the message is "bye". If it is it will respind with a formatted string including the user's username and their ec2 region
            elif user_message.lower() == "bye":
                await message.channel.send(f"Bye {username} Your EC2 Data: {ec2_metadata.region}")
                return
                # else if statement, this will change the user's essage to all lowercase. If the message is "tell me about your server" then the discord bot will respond witb a formatted string including the user's ec2 public ip address, ec2 region, and ec2 instance id
            elif user_message.lower() == "tell me about my server!":
                await message.channel.send(f"Here is you IP Address: {ec2_metadata.public_ipv4}, Your EC2 Region: {ec2_metadata.region}, and Availability Zone: {ec2_metadata.availability_zone}")
                return
                # else if statement, this will change the user's message to all lowercase. If the message is "how are you doing" the discord bot will respond with "I'm doing well"
            elif user_message.lower() == "how are you doing":
                await message.channel.send("I'm doing well")
                return
                # else if statement, this will change the user's message to all lowercase. If the message is "tell me a joke" then the discord bot will randomly respond with one of the jokes in the list.
            elif user_message.lower() == "tell me a joke":
                jokes = [
                    "Why do programmers prefer dark mode?\nBecause light attracts bugs",
                    "How do you comfort a JavaScript Bug?\nYou console it.",
                    "Why don't scientists trust atoms?\nBecause they make up everything!"
                ]
                await message.channel.send(random.choice(jokes))
                return
                # Else statement if the user doesn't send in one of the prompts it will return this message.
            else:
                await message.channel.send("I don't understand. Please respond with one of the prompts.")
      
        # Except to catch any errors from the discord bot. It will also print the errors.      
        except Exception as e:
            print(f"Error: {e}")
            await message.channel.send("Unable to respond due to an error!")
   
# Running the bot with token
client.run(token)
