"""Shared black-and-white schematic preview helpers."""
from PIL import Image, ImageDraw

def place_artwork(canvas, artwork, box):
    image=artwork.convert('RGB').copy(); image.thumbnail((box[2]-box[0],box[3]-box[1]),Image.Resampling.LANCZOS)
    x=box[0]+((box[2]-box[0])-image.width)//2; y=box[1]+((box[3]-box[1])-image.height)//2; canvas.paste(image,(x,y))

def draw_phone_outline(canvas, box, width=12):
    d=ImageDraw.Draw(canvas); d.rounded_rectangle(box,radius=70,outline='black',width=width); d.rounded_rectangle((box[0]+35,box[1]+80,box[2]-35,box[3]-45),radius=38,outline='black',width=width); cx=(box[0]+box[2])//2; d.rounded_rectangle((cx-45,box[1]+28,cx+45,box[1]+40),radius=6,fill='black')
    return (box[0]+45,box[1]+95,box[2]-45,box[3]-55)

def draw_luggage_tag_outline(canvas, box, width=12):
    d=ImageDraw.Draw(canvas); d.rounded_rectangle(box,radius=55,outline='black',width=width); cx=(box[0]+box[2])//2; d.ellipse((cx-45,box[1]+45,cx+45,box[1]+135),outline='black',width=width)
    return (box[0]+40,box[1]+165,box[2]-40,box[3]-40)
