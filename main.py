import discord
import os
import asyncio
from collections.abc import Sequence
from keep_alive import keep_alive
from StapleLands import StapleLands
#https://uptimerobot.com/dashboard#786868655

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    cmd = message.content.casefold()

    if cmd.startswith('$hello'):
        await message.channel.send('Hello!')

    if cmd.startswith('$help'):
        await message.channel.send(
            '''Wheel of Misfortune Bot supports the following commands:
$hello
$wheel @Player2 @Player3 @Player4
$wheelhelp
$manabase WUBRG
$manabasehelp''')

    if cmd.startswith('$wheelhelp'):
        await message.channel.send(
            '''Enter command as follows to spin the wheel:\n
			$wheel @Player2 @Player3 @Player4''')

    if cmd.startswith('$manabasehelp'):
        await message.channel.send(
            '''Enter command as follows: $manabase WUBRG\n
			example: $manabase WRG''')

    if cmd.startswith('$manabase') or cmd.startswith('$mb'):
        x = manabaseSuggestion(cmd)

        await message.channel.send(x)

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
                await x.send(
                    'Please respond with your chosen number. Channel will remain open until a valid response is submitted.'
                )

                response = ''
                responseIsValid = False
                i = 0

                while responseIsValid == False:
                    i += 1
                    print('Sending message # {} to {}'.format(str(i), x.name))

                    response = await client.wait_for(
                        'message',
                        timeout=120.0,
                        check=message_check(channel=x.dm_channel))
                    response = sanitizeResponse(response.content)
                    responseIsValid = checkIfResponseIsValid(response)
                    if responseIsValid:
                        print('{0} responds with: {1}'.format(
                            x.name, str(response)))
                        responseDict.update({x.mention: response})
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
        return (seq, )


def message_check(channel=None,
                  author=None,
                  content=None,
                  ignore_bot=True,
                  lower=True):
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


def manabaseSuggestion(cmd=None):

    cmdList = cmd.split(' ', 5)
    try:
      cmdColors = cmdList[1]
    except:
      output = "Please format your request like: $manabase WUBRG"
      return output

    deckColors = split(cmdColors)

    if len(deckColors) == 1:
      output = "Idk...basics?"
      return output
			
    stapleLands = StapleLands.getStapleLands(deckColors)
    
    output = '\n'.join(x.name for x in stapleLands)

    return output


def split(word):
    return list(word)


keep_alive()
client.run(os.getenv('TOKEN'))
