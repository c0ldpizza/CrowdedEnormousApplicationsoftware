import discord
import os
import asyncio
from collections.abc import Sequence
from keep_alive import keep_alive

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

		if cmd.startswith('$wheelhelp'):
			await message.channel.send('Hello!')

		if cmd.startswith('$wheel'):

			#get users
			author = message.author
			y = author
			userProfiles = [y]
			for member in message.mentions:
				userProfiles.append(member)

			try:
				responseDict = {}
				for x in userProfiles:
					print(x.name)
					await x.send('Please respond with your chosen number. Channel will remain open until a valid response is submitted.')

					response = ''
					responseIsValid = False
					i = 0

					while responseIsValid == False:
						i += 1
						print('Sending message # {} to {}'.format(str(i), x.name))

						response = await client.wait_for('message', timeout=120.0,check=message_check(channel=x.dm_channel))
						response = sanitizeResponse(response.content)
						responseIsValid = checkIfResponseIsValid(response)
						if responseIsValid:
							print('{0} responds with: {1}'.format(x.name, str(response)))
							responseDict.update({x.mention : response})
							break
						else:
							continue
					
				if len(responseDict) >= len(userProfiles):
					#format responseDict
					results = 'Results:\n'
					for x, y in responseDict.items():
						results += x + ' : ' + str(y) + '\n'
						
					await message.channel.send(results)
					return

			except asyncio.TimeoutError:
				print('Responses timed out!')
				await message.channel.send('Responses timed out!')
				return
			#except:
				#print('Oops!')
				#return
			finally:
				print("wheeling complete")



def sanitizeResponse(response):
		try:
			response = response.strip()
			response = response.split()[0]
			response = int(response)
		finally:
			return response

def checkIfResponseIsValid(response):		

		if isinstance(response, int):
			if response >= 0:
				print("is valid")
				return True
		return False			


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

keep_alive()
client.run(os.getenv('TOKEN'))