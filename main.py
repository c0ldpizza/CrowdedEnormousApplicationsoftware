import discord
import os
import asyncio
import datetime
from collections.abc import Sequence


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    cmd = message.content

    if cmd.startswith('$hello'):
        await message.channel.send('Hello!')

    if cmd.startswith('$wheel'):
      #get system time
      #commandTime = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
      #print(commandTime)

      #get users
      author = message.author
      y = author
      userProfiles = [y]
      for member in message.mentions:
        userProfiles.append(member)

      try:
        for x in userProfiles:
          print(x.name)
          await x.send("Please respond with your chosen number")
          response = await client.wait_for('message', timeout=120.0,check=message_check(channel=x.dm_channel))
          print(response.content)
          #await message.channel.send(x.mention)
          

      except asyncio.TimeoutError:
        print('Responses timed out!')
        await message.channel.send('Responses timed out!')
        return
      except:
        print('Oops!')




def make_sequence(seq):
    if seq is None:
        return ()
    if isinstance(seq, Sequence) and not isinstance(seq, str):
        return seq
    else:
        return (seq,)

def message_check(channel=None, author=None, content=None, ignore_bot=True, lower=True):
  channel = make_sequence(channel)
  author = make_sequence(author)
  content = make_sequence(content)
  if lower:
      content = tuple(c.lower() for c in content)
  def check(message):
      if ignore_bot and message.author.bot:
          return False
      if channel and message.channel not in channel:
          return False
      if author and message.author not in author:
          return False
      actual_content = message.content.lower() if lower else message.content
      if content and actual_content not in content:
          return False
      return True
  return check

client.run(os.getenv('TOKEN'))