###################################################################
#                             Totems+                             #
# A new and unique way to integrate custom totems into Minecraft! #
#    Learn More here:https://github.com/The-Iceburg/TotemsPlus    #
#        Created By The Totems+ Team - Ormatist + Dockuin         #
###################################################################

# imports the libaries used within totems+
from PIL import Image
import os, shutil, getpass

# defines the texture convereter subroutine
def ANI(imageLocation, packName, integrationType, rename):

    
    # opens the image as an object python/PIL can interact with
    imageObject = Image.open(imageLocation)
    

    # if the gif width and height are equal then
    if imageObject.size[1] == imageObject.size[0]:

        # sets the location of the copied
        width = 0

        # sets the height of the new image to the height of the original x the no. of frames
        height2 = imageObject.size[1] * imageObject.n_frames

        # creates the new image using the calacuated height
        new = Image.new(mode="RGB", size=(imageObject.size[0], height2), color='#ffffff')

    # if the width of the gif is greater than the height then
    if imageObject.size[0] > imageObject.size[1]:

        # calacuates the buffer zone required for the image to be centeral
        width = -abs(round((imageObject.size[0] - imageObject.size[1]) / 2))

        # calculates the height of the new image to the height of the original x no. of frames
        height2 = imageObject.size[1] * imageObject.n_frames

        # creates the new image using the calacuated height
        new = Image.new(mode="RGB", size=(imageObject.size[1], height2), color='#ffffff')

    # if the width of the gif is less than the height then
    if imageObject.size[0] < imageObject.size[1]:
        
        # sets the location of the copied
        width = 0

        # calculates the height of the new image to the height of the original x no. of frames
        height2 = imageObject.size[0] * imageObject.n_frames

        # creates the new image using the calacuated height
        new = Image.new(mode="RGB", size=(imageObject.size[0], height2), color='#ffffff')

    # for each frame in the gif
    for frame in range(0,imageObject.n_frames):

        # selects said frame
        imageObject.seek(frame)

        # if the gif width and height are equal then
        if imageObject.size[1] == imageObject.size[0]:

            # calacutes the height at which the image needs to be pasted 
            # depends on how far down the new image you are
            height = frame * imageObject.size[1]

        # if the width of the gif is greater than the height then
        elif imageObject.size[0] > imageObject.size[1]:

            # calacutes the height at which the image needs to be pasted 
            # depends on how far down the new image you are
            height = frame * imageObject.size[1]

        # if the width of the gif is less than the height then
        elif imageObject.size[0] < imageObject.size[1]:

            # if its the first frame then
            if frame == 0:
                
                # sets the height of the copied image to an appropriate place for a mc texture
                height = frame * imageObject.size[1] - round(imageObject.size[0] - imageObject.size[1] / 2)
            
            # else / otherwise
            else:
                
                # sets the height of the copied image to an appropriate place for a mc texture
                height = frame * imageObject.size[1] - ( 2 * round(imageObject.size[0] - imageObject.size[1] / 2))

        # pastes the image using the calculated buffer and height
        new.paste(imageObject, (width, height))

     # if the directory resized already exists, then delete it
    if os.path.exists('C:/Users/' + getpass.getuser() + '/AppData/Roaming/Totems+/giftexture'):
        shutil.rmtree('C:/Users/' + getpass.getuser() + '/AppData/Roaming/Totems+/giftexture')

    # make the giftexture folder
    os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/giftexture")

    # derrives the file name ([-1])
    locationList = imageLocation.split("/")
    llfilename = locationList[-1].replace(".gif", ".png")
    
    # saves the new image in the appropraite location
    new.save("C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/giftexture/" + llfilename)

    # sets frametime to a temporary constant (it will be variable in the future)
    FRAMETIME = 1

    # if the integration type is MCCMD
    if integrationType == "MCCMD":

        # creates the .mcmeta in the appropriate location for the integration type (MCCMD)
        file = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + packName + "/assets/minecraft/textures/totems/" + llfilename + ".mcmeta", "w+")

        # writes the appropriate data to the file
        file.writelines(['{\n',
        '  "animation": {\n'])
        file.write('    "frametime": ' + str(FRAMETIME) + '\n')
        file.writelines(['  }\n',
        '}'])

        # saves / closes the file
        file.close()

    # if the integration type is OFCIT
    elif integrationType == "OFCIT":

        # creates the .mcmeta in the appropriate location for the integration type (OFCIT)
        file = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + packName + "/assets/minecraft/optifine/cit/totems/" + str(rename.lower()) + "/" + llfilename + ".mcmeta", "w+")

        # writes the appropriate data to the file
        file.writelines(['{\n',
        '  "animation": {\n'])
        file.write('    "frametime": ' + str(FRAMETIME) + '\n')
        file.writelines(['  }\n',
        '}'])

        # saves / closes the file
        file.close()

    # if the integration type is OFCIT
    elif integrationType == "MCRTX":

        # creates the .mcmeta in the appropriate location for the integration type (OFCIT)
        file = open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + packName + "/assets/minecraft/textures/item/totem_of_undying.png.mcmeta", "w+")

        # writes the appropriate data to the file
        file.writelines(['{\n',
        '  "animation": {\n'])
        file.write('    "frametime": ' + str(FRAMETIME) + '\n')
        file.writelines(['  }\n',
        '}'])

        # saves / closes the file
        file.close()

    # returns the new / appropriate location for the gif texture
    return "C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/giftexture/" + llfilename
