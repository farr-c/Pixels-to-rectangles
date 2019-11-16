from PIL import Image


im = Image.open('i.png')
im = im.convert("RGB")
img = im.load()

myColors = []

maxX, maxY = im.size

resultImage = []

correctShape = {}

shapes = {}

allShapes = []

printAbleShape = []



def selectPixels(theColor, offset=80):

    for x in range(maxX):
        for y in range(maxY):
                
            if abs(img[x, y][0] - theColor[0]) < offset and abs(img[x, y][1] - theColor[1]) < offset and abs(img[x, y][2] - theColor[2]) < offset:
                correctShape[str([x,y])] = theColor


edges = {}

def newSelectShape(x, y, c):
    if not str([x, y]) in correctShape:
        print("Return me!") 
        return
    brandNewShape = {}
    shapeLength = 0
    shapeHeight = -10
    startX = x
    startY = y
    while str([x, y]) in correctShape:
        x+= 1
        print(str([x, y]))
    shapeLength = x - startX
    x = startX

    forceEnd = False

    while str([x,y ]) in correctShape and not forceEnd:
        y += 1
        for i in range(shapeLength):
            if not str([x+i,y ]) in correctShape and shapeHeight == -10:
                forceEnd = True
                break
    
    shapeHeight = y - startY


    #shapes[str([startX, startY])] = c
    #randNewShape[str([startX, startY])] = True
    #print(correctShape[str([startX, startY])])
   # del correctShape[str([startX, startY])]

    
    printAbleShape.append((startX, startY, shapeLength, shapeHeight))

    for sY in range(0, shapeHeight):
       for sX in range(0, shapeLength):
    #if str([sX + startX, sY + startY]) in correctShape:
            shapes[str([sX + startX, sY + startY])] = c
            brandNewShape[str([sX + startX, sY + startY])] = True
            print("Started at : " + str(startX) + "," + str(startY) + " Length " + str(shapeLength))
            del correctShape[str([sX + startX, sY + startY])]
    
    allShapes.append(brandNewShape)

    return brandNewShape

selectPixels((255,255,255))

import random

for y1 in range(maxY):
    for x1 in range(maxX):
        if str([x1, y1]) in correctShape:
            print(x1, y1)
            s = newSelectShape(x1, y1, (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))

    
print(len(correctShape))
#newSelectShape(0,0)
print(len(correctShape))
#selectEdges(0,0, (255,255,255))
#selectShape(0, 0)



for y in range(maxY):
    for x in range(maxX):
        if str([x, y]) in edges:
            resultImage.append((0,0,0))
        elif str([x,y]) in shapes:
            resultImage.append(shapes[str([x,y])])
        else:
            resultImage.append((0,0,0))
print("Completed!")

print(len(resultImage))

newImg = Image.new('RGB', (maxX, maxY))
newImg.putdata(resultImage)
newImg.save('image.png')

outputMessage = ""

for i in printAbleShape:
    x = str(i[0])
    y = str(i[1])
    xScale = str(i[2])
    yScale = str(i[3])

    addon = "(("+x+"*s)+oX,("+y+"*s)+oY,"+xScale+"*s,"+yScale+"*s)\n"  

    outputMessage = outputMessage + "rect" + addon

print(outputMessage)
outputFile = open("output.txt", "w")
outputFile.write(outputMessage)
outputFile.close()
