from PIL import Image
  
# open method used to open different extension image file
im = Image.open("pixel_194.png") 
pixelMap = im.load()

img = Image.new(im.mode, im.size)
img = im
px = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        if px[i,j][0] >= px[i,j][1] and px[i,j][1] <= px[i,j][2]:
            px[i,j]=(255,255,255)
        else:
            px[i,j]=(0,0,0)
        #print(px[i,j])

img = img.save("img.png")
#img.show()
# This method will show image in any image viewer 
#im.show() 