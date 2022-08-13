import PIL
from PIL import Image, GifImagePlugin
import png

def animatedConverter(imageLocation):

    imageObject = Image.open(imageLocation)

    height = imageObject.size[1] * imageObject.n_frames

    new = Image.new(mode="RGB", size=(imageObject.size[1], height), color='#ffffff')

    buffer = imageObject.size[0] - imageObject.size[1]

    buffer = round(buffer/2)

    for frame in range(0,imageObject.n_frames):

        imageObject.seek(frame)

        height2 = frame * imageObject.size[1]

        new.paste(imageObject, (-buffer, height2))

    new.save("img/test2.png")

animatedConverter("img/test.gif")