###################################################################
#                             Totems+                             #
# A new and unique way to integrate custom totems into Minecraft! #
#    Learn More here:https://github.com/The-Iceburg/TotemsPlus    #
#        Created By The Totems+ Team - Ormatist + Dockuin         #
###################################################################

# imports the libaries used within totems+
from PIL import Image

# defines the texture convereter subroutine
def animatedConverter(imageLocation):

    # opens the image as an object python/PIL can interact with
    imageObject = Image.open(imageLocation)
    
    # calculates the height for the new image
    height = imageObject.size[1] * imageObject.n_frames

    # creates the new image using the calacuated height
    new = Image.new(mode="RGB", size=(imageObject.size[1], height), color='#ffffff')

    # calacuates the buffer zone required for the image to be centeral
    buffer = imageObject.size[0] - imageObject.size[1]
    buffer = round(buffer/2)

    # for each frame in the gif
    for frame in range(0,imageObject.n_frames):

        # selects said frame
        imageObject.seek(frame)

        # calacutes the height at which the image needs to be pasted 
        # depends on how far down the new image you are
        height2 = frame * imageObject.size[1]

        # pastes the image using the calculated buffer and height
        new.paste(imageObject, (-buffer, height2))

    # saves the new image
    new.save("img/test2.png")

# runs the subroutine for testing purposes
animatedConverter("img/test.gif")