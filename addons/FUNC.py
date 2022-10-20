###################################################################
#                             Totems+                             #
# A new and unique way to integrate custom totems into Minecraft! #
#    Learn More here:https://github.com/The-Iceburg/TotemsPlus    #
#        Created By The Totems+ Team - Ormatist + Dockuin         #
###################################################################

# imports the libaries used within totems+
import os

# defines the function function
def FUN(worldLocation, nameList, inGameName, inGameLore, loreList):

    # creates the function directory
    os.mkdir(worldLocation + "/datapacks/Totems+ CMD/data/totemsplus")
    os.mkdir(worldLocation + "/datapacks/Totems+ CMD/data/totemsplus/functions")

    # creates the totem load function
    mcfunction = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/functions/totemload.mcfunction', 'w+')

    # cycles throught the name list
    for i in range(len(nameList)):

        # writes univerasal start to command
        mcfunction.write('give @s minecraft:totem_of_undying{')
        
        # writes the rest of the command dependent on if the in-game box was checked for lore or name
        if inGameName[i] == True and loreList[i] != None:

            mcfunction.write('''display:{Name:'[{"text":"''' + nameList[i] + '''"}]',Lore:['[{"text":"''' + loreList[i]+ '''"}]']},CustomModelData:''' + str(910340 + i) +'} 1\n')

        elif inGameName[i] == True:

            mcfunction.write('''display:{Name:'[{"text":"''' + nameList[i] + '''"}]'},CustomModelData:''' + str(910340 + i) +'} 1\n')

        elif loreList[i] != None:

            mcfunction.write('''display:{Lore:['[{"text":"''' + loreList[i] + '''"}]']},CustomModelData:''' + str(910340 + i) +'} 1\n')

        else:

            mcfunction.write('CustomModelData:' + str(910340 + i) +'} 1\n')

    # closes the file
    mcfunction.close()

    # cycles throught the name list
    for i in range(len(nameList)):

        # creates the totems own file
        mcfunction = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/functions/summon' + nameList[i].lower().replace(" ","_") + '.mcfunction', 'w+')

        # writes the universal info
        mcfunction.write('give @s minecraft:totem_of_undying{')
        
        # writes the rest of the command dependent on if the in-game box was checked for lore or name
        if inGameName[i] == "True" and inGameLore[i] == "True":

            mcfunction.write('''display:{Name:'[{"text":"''' + nameList[i] + '''"}]',Lore:['[{"text":"''' + loreList[i]+ '''"}]']},CustomModelData:''' + str(910340 + i) +'} 1\n')

        elif inGameName[i] == "True":

            mcfunction.write('''display:{Name:'[{"text":"''' + nameList[i] + '''"}]'},CustomModelData:''' + str(910340 + i) +'} 1\n')

        elif inGameLore[i] == "True":

            mcfunction.write('''display:{Lore:['[{"text":"''' + loreList[i] + '''"}]']},CustomModelData:''' + str(910340 + i) +'} 1\n')

        else:

            mcfunction.write('CustomModelData:' + str(910340 + i) +'} 1\n')

        # closes / saves the file
        mcfunction.close()