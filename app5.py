from PIL import  Image, ImageFont, ImageDraw

im02 = Image.open("base.png")
draw = ImageDraw.Draw(im02)

ft = ImageFont.truetype("/Library/Fonts/Farisi.ttf", 20)
draw.text((30,30), "123232322332",font = ft, fill = '#000')
# ft = ImageFont.truetype("C:\\WINDOWS\\Fonts\\SIMYOU.TTF", 40)
# draw.text((30,100), u"Python图像处理库PIL从入门到精通",font = ft, fill = 'green')
# ft = ImageFont.truetype("C:\\WINDOWS\\Fonts\\SIMYOU.TTF", 60)
# draw.text((30,200), u"Python图像处理库PIL从入门到精通",font = ft, fill = 'blue')
# ft = ImageFont.truetype("C:\\WINDOWS\\Fonts\\SIMLI.TTF", 40)
# draw.text((30,300), u"Python图像处理库PIL从入门到精通",font = ft, fill = 'red')
# ft = ImageFont.truetype("C:\\WINDOWS\\Fonts\\STXINGKA.TTF", 40)
# draw.text((30,400), u"Python图像处理库PIL从入门到精通",font = ft, fill = 'yellow')

# im02.show()

im02.save('base_new.png')