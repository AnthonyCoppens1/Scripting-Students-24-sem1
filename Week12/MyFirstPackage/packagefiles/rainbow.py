from PIL import Image

def rainbowgenerator(x, y):
    """Generating a rainbow image
    Parameters:
        int --> x
        int --> y
    Return:
        none
    """
    img = Image.new('RGBA', (x,y), 'white') #200, 200

    red = Image.new('RGBA', (int(x/7),y), 'red')
    img.paste(red, (0,0))

    orange = Image.new('RGBA', (int(x/7),y), 'orange')
    img.paste(orange, (int(x/7),0))

    yellow = Image.new('RGBA', (int(x/7),y), 'yellow')
    img.paste(yellow, (int((x/7)*2),0))

    green = Image.new('RGBA', (int(x/7),y), 'green')
    img.paste(green, (int((x/7)*3),0))

    blue = Image.new('RGBA', (int(x/7),y), 'blue')
    img.paste(blue, (int((x/7)*4),0))

    indigo = Image.new('RGBA', (int(x/7),y), 'indigo')
    img.paste(indigo, (int((x/7)*5),0))

    violet = Image.new('RGBA', (int(x/7),y), 'violet')
    img.paste(violet, (int((x/7)*6),0))

    img.save('rainbow.png')
    img.show()
    

    #red / orange / yellow / green / blue /indigo / violet


