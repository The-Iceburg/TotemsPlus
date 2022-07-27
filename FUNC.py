###################################################################
#                             Totems+                             #
# A new and unique way to integrate custom totems into Minecraft! #
#    Learn More here:https://github.com/The-Iceburg/TotemsPlus    #
#        Created By The Totems+ Team - Ormatist + Dockuin         #
###################################################################

# imports the libaries used within totems+
import os
import getpass

# defines the function function
def FUN():

    # grabs nessesary info from the funconfig file
    funconfig = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/funconfig.txt", "r")
    funconfigread = funconfig.readlines()
    funconfig.close()

    # sorts info to appropriate variables
    worldLocation = funconfigread[0]
    nameList = funconfigread[1]
    loreList = funconfigread[4]
    inGameName = funconfigread[2]
    inGameLore = funconfigread[3]

    # changes some variables into lists
    worldLocation = worldLocation.replace('\n','')
    nameList = nameList.split(';')
    loreList = loreList.split(';')
    inGameLore = inGameLore.split(';')
    inGameName = inGameName.split(';')

    # creates the function directory
    os.mkdir(worldLocation + "/datapacks/Totems+ CMD/data/totemsplus")
    os.mkdir(worldLocation + "/datapacks/Totems+ CMD/data/totemsplus/functions")

    # creates the totem load function
    mcfunction = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/functions/totemload.mcfunction', 'x')
    mcfunction.close()

    mcfunction = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/functions/totemload.mcfunction', 'a')

    # sests the counter to 0
    counter = 0

    # cycles throught the name list
    while len(nameList) != counter + 1:

        # writes univerasal start to command
        mcfunction.write('give @s minecraft:totem_of_undying{')
        
        # writes the rest of the command dependent on if the in-game box was checked for lore or name
        if inGameName[counter] == "True" and inGameLore[counter] == "True":

            mcfunction.write('''display:{Name:'[{"text":"''' + nameList[counter] + '''"}]',Lore:['[{"text":"''' + loreList[counter]+ '''"}]']},CustomModelData:''' + str(910340 + counter) +'} 1\n')

        elif inGameName[counter] == "True":

            mcfunction.write('''display:{Name:'[{"text":"''' + nameList[counter] + '''"}]'},CustomModelData:''' + str(910340 + counter) +'} 1\n')

        elif inGameLore[counter] == "True":

            mcfunction.write('''display:{Lore:['[{"text":"''' + loreList[counter] + '''"}]']},CustomModelData:''' + str(910340 + counter) +'} 1\n')

        else:
            mcfunction.write('CustomModelData:' + str(910340 + counter) +'} 1\n')

        # increases the counter by 1
        counter += 1
    
    # closes the file
    mcfunction.close()
    
    # re-sets the counter to 0
    counter = 0

    # cycles throught the name list
    while len(nameList) != counter + 1:

        # creates the totems own file
        mcfunction = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/functions/summon' + nameList[counter].lower().replace(" ","_") + '.mcfunction', 'x')
        mcfunction.close()

        mcfunction = open(worldLocation + '/datapacks/Totems+ CMD/data/totemsplus/functions/summon' + nameList[counter].lower().replace(" ","_") + '.mcfunction', 'a')

        # writes the universal info
        mcfunction.write('give @s minecraft:totem_of_undying{')
        
        # writes the rest of the command dependent on if the in-game box was checked for lore or name
        if inGameName[counter] == "True" and inGameLore[counter] == "True":

            mcfunction.write('''display:{Name:'[{"text":"''' + nameList[counter] + '''"}]',Lore:['[{"text":"''' + loreList[counter]+ '''"}]']},CustomModelData:''' + str(910340 + counter) +'} 1\n')

        elif inGameName[counter] == "True":

            mcfunction.write('''display:{Name:'[{"text":"''' + nameList[counter] + '''"}]'},CustomModelData:''' + str(910340 + counter) +'} 1\n')

        elif inGameLore[counter] == "True":

            mcfunction.write('''display:{Lore:['[{"text":"''' + loreList[counter] + '''"}]']},CustomModelData:''' + str(910340 + counter) +'} 1\n')

        else:
            mcfunction.write('CustomModelData:' + str(910340 + counter) +'} 1\n')

        # closes / saves the file
        mcfunction.close()

        # increases the counter by 1
        counter += 1