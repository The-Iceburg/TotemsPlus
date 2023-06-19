###################################################################
#                             Totems+                             #
# A new and unique way to integrate custom totems into Minecraft! #
#    Learn More here:https://github.com/The-Iceburg/TotemsPlus    #
#        Created By The Totems+ Team - Ormatist + Dockuin         #
###################################################################

# imports the libaries used within totems+
from PIL import Image
import os, shutil, getpass, json

# outlines the mcmeta file
mcMeta = {"animation": {"frametime" : 0 }}

# defines the texture convereter subroutine
def ANI(imageLocation, packName, integrationType, rename):

    # opens the image as an object python/PIL can interact with
    imageObject = Image.open(imageLocation)

     # derrives the file name ([-1])
    locationList = imageLocation.split("/")
    llfilename = locationList[-1].replace(".gif", ".png")

     # if the directory resized already exists, then delete it
    if os.path.exists('C:/Users/' + getpass.getuser() + '/AppData/Roaming/Totems+/giftexture'):
        shutil.rmtree('C:/Users/' + getpass.getuser() + '/AppData/Roaming/Totems+/giftexture')

    # make the giftexture folder
    os.mkdir("C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/giftexture")
    
    # if the gif width and height are equal then
    if imageObject.size[1] == imageObject.size[0]:

        # sets the location of the copied
        width = 0

        # sets the height of the new image to the height of the original x the no. of frames
        height2 = imageObject.size[1] * imageObject.n_frames

        # creates the new image using the calacuated height
        new = Image.new(mode="RGB", size=(imageObject.size[0], height2), color='#ffffff')

        # for each frame
        for frame in range(0,imageObject.n_frames):

            # selects the frame
            imageObject.seek(frame)

            # calculates the height at which to paste into the new image
            height = frame * imageObject.size[1]

            # pastes the image
            new.paste(imageObject, (width, height))

    # if the width of the gif is greater than the height then
    if imageObject.size[0] > imageObject.size[1]:

        # calacuates the buffer zone required for the image to be centeral
        width = -abs(round((imageObject.size[0] - imageObject.size[1]) / 2))

        # calculates the height of the new image to the height of the original x no. of frames
        height2 = imageObject.size[1] * imageObject.n_frames

        # creates the new image using the calacuated height
        new = Image.new(mode="RGB", size=(imageObject.size[1], height2), color='#ffffff')

        # for each frame
        for frame in range(0,imageObject.n_frames):

            # selects the frame
            imageObject.seek(frame)

            # calculates the height at which to paste into the new image
            height = frame * imageObject.size[1]

            # pastes the image
            new.paste(imageObject, (width, height))

    # if the width of the gif is less than the height then
    if imageObject.size[0] < imageObject.size[1]:
        
        # sets the location of the copied
        width = 0

        # calculates the height of the new image to the height of the original x no. of frames
        height2 = imageObject.size[0] * imageObject.n_frames

        # creates the new image using the calacuated height
        new = Image.new(mode="RGB", size=(imageObject.size[0], height2), color='#ffffff')

        # for each frame
        for frame in range(0,imageObject.n_frames):

            # gets the first frame
            imageObject.seek(frame)

            # calculates the buffer space
            buffer = (imageObject.size[1] - imageObject.size[0]) / 2

            # calculates the height to paste the new image at
            height = frame * imageObject.size[0]

            # pastes the cropped image to the new image
            new.paste(imageObject.crop((0, buffer, imageObject.size[0], imageObject.size[1] - buffer)), (width, height))
    
    # saves the new image in the appropraite location
    new.save("C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/giftexture/" + llfilename)

    # sets frametime to a temporary constant (it will be variable in the future)
    FRAMETIME = 1

    # if the integration type is MCCMD
    if integrationType == "MCCMD":

        # creates the .mcmeta in the appropriate location for the integration type (MCCMD)
        with open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + packName + "/assets/minecraft/textures/totems/" + llfilename + ".mcmeta", "w+") as mcMetaFile:
            
            # writes nessesary info to the file
            mcMeta["animation"]["frametime"] = FRAMETIME
            mcMetaFile.write(json.dumps(mcMeta))

    # if the integration type is OFCIT
    elif integrationType == "OFCIT":

        # creates the .mcmeta in the appropriate location for the integration type (OFCIT)
        with open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + packName + "/assets/minecraft/optifine/cit/totems/" + str(rename.lower()) + "/" + llfilename + ".mcmeta", "w+") as mcMetaFile:
            
            # writes nessesary info to the file
            mcMeta["animation"]["frametime"] = FRAMETIME
            mcMetaFile.write(json.dumps(mcMeta))

    # if the integration type is MCRTX
    elif integrationType == "MCRTX":

        # creates the .mcmeta in the appropriate location for the integration type (MCRTX)
        with open("C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/resourcepacks/" + packName + "/assets/minecraft/textures/item/totem_of_undying.png.mcmeta", "w+") as mcMetaFile:

            # writes nessesary info to the file
            mcMeta["animation"]["frametime"] = FRAMETIME
            mcMetaFile.write(json.dumps(mcMeta))

    # returns the new / appropriate location for the gif texture
    return "C:/Users/" + getpass.getuser() + "/AppData/Roaming/Totems+/giftexture/" + llfilename