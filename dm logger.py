import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import pystyle





print(pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_purple, """                                                                                                                 
      :::::::::    :::   :::          :::        ::::::::   ::::::::   ::::::::  :::::::::: ::::::::: 
     :+:    :+:  :+:+: :+:+:         :+:       :+:    :+: :+:    :+: :+:    :+: :+:        :+:    :+: 
    +:+    +:+ +:+ +:+:+ +:+        +:+       +:+    +:+ +:+        +:+        +:+        +:+    +:+  
   +#+    +:+ +#+  +:+  +#+        +#+       +#+    +:+ :#:        :#:        +#++:++#   +#++:++#:    
  +#+    +#+ +#+       +#+        +#+       +#+    +#+ +#+   +#+# +#+   +#+# +#+        +#+    +#+    
 #+#    #+# #+#       #+#        #+#       #+#    #+# #+#    #+# #+#    #+# #+#        #+#    #+#     
#########  ###       ###        ########## ########   ########   ########  ########## ###    ###      


     made by improve#0001 (interspec/kxtOnYT on github)       
""", 2))





#TOKEN
TOKEN = "TOKEN"

client = discord.Client()
b = commands.Bot(command_prefix = "not needed dw")


@b.event
async def on_message(message):
    if message.channel.type == discord.ChannelType.private:
        print(message.author, "|", message.content)
    

b.run(TOKEN, bot = False)
