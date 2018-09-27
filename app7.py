import qrcode
from PIL import  ImageDraw, Image, ImageFont

'''
    version 表示生成二维码的尺寸大小，取值范围是 1 至 40，
    最小尺寸 1 会生成 21 * 21 的二维码，version 每增加 1，
    生成的二维码就会添加 4 尺寸，例如 version 是 2，则生成 25 * 25 的二维码

    参数 box_size 表示二维码里每个格子的像素大小。 
    参数 border 表示边框的格子厚度是多少（默认是4）
'''

qr = qrcode.QRCode(
    version=7,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr.add_data("Hellofjkshfjkhsjkdfhdskjhjhjkhfjksdhfkjdshkj")

qr.make(fit=True)

img = qr.make_image()
img = img.convert("RGBA")

# ico

icon = Image.open("fav.png")

img_w, img_h = img.size

factor = 4
size_w = int(img_w / factor)
size_h = int(img_h / factor)

icon_w, icon_h = icon.size

if icon_w > size_w:
    icon_w = size_w
if icon_h > size_h:
    icon_h = size_h

icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

w = int((img_w - icon_w) / 2)
h = int((img_h - icon_h) / 2)
icon = icon.convert("RGBA")
img.paste(icon, (w, h), icon)

# two
draw = ImageDraw.Draw(img)

ft = ImageFont.truetype("/Library/Fonts/Arial.ttf", 24)
draw.text((50,495), "123243434433442231321332",font = ft, fill = '#000')

img.save("6_new.png")

