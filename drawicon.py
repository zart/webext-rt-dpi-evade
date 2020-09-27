from PIL import Image, ImageDraw, ImageFont

transparent = 0, 0, 0, 0
white = 255, 255, 255, 255
black = 0, 0, 0, 255
red = 255, 0, 0, 255

if __name__ == '__main__':
    w, h = 128, 128
    t = w // 10
    img = Image.new('RGBA', (w, h), transparent)
    font = ImageFont.truetype('arial.ttf', 32)
    draw = ImageDraw.Draw(img)
    draw.ellipse([0, 0, w, h], fill=white, outline=red, width=t)
    tw, th = draw.textsize("RT.RU", font=font)
    draw.text(((w-tw) // 2, (h-th) // 2), "RT.RU", font=font, fill=black)
    draw.line([w-8*t//5, 8*t//5, 8*t//5, w-8*t//5], fill=red, width=t)
    img.save('icon.png')
