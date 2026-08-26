"""Shared black-and-white schematic preview helpers."""
from PIL import Image, ImageDraw

def place_artwork(canvas, artwork, box):
    image=artwork.convert('RGB').copy(); image.thumbnail((box[2]-box[0],box[3]-box[1]),Image.Resampling.LANCZOS)
    x=box[0]+((box[2]-box[0])-image.width)//2; y=box[1]+((box[3]-box[1])-image.height)//2; canvas.paste(image,(x,y))

def draw_phone_outline(canvas, box, width=12):
    d=ImageDraw.Draw(canvas); d.rounded_rectangle(box,radius=70,outline='black',width=width); d.rounded_rectangle((box[0]+35,box[1]+80,box[2]-35,box[3]-45),radius=38,outline='black',width=width); cx=(box[0]+box[2])//2; d.rounded_rectangle((cx-45,box[1]+28,cx+45,box[1]+40),radius=6,fill='black')
    return (box[0]+45,box[1]+95,box[2]-45,box[3]-55)

def draw_lighter_outline(canvas, box, width=12):
    d=ImageDraw.Draw(canvas)
    x1,y1,x2,y2=box
    body_top=y1+205
    d.rounded_rectangle((x1,body_top,x2,y2),radius=80,outline='black',width=width)
    d.line((x1+8,body_top+20,x2-8,body_top+20),fill='black',width=width)
    d.rounded_rectangle((x1+95,y1+25,x1+625,y1+215),radius=72,outline='black',width=width)
    d.line((x1+145,y1+45,x1+145,y1+190),fill='black',width=width)
    d.ellipse((x1+555,y1+18,x1+735,y1+188),outline='black',width=width)
    d.ellipse((x1+605,y1+68,x1+665,y1+128),outline='black',width=width)
    d.rounded_rectangle((x1+665,y1+112,x2-55,y1+165),radius=12,outline='black',width=width)
    d.line((x1+690,y1+138,x2-85,y1+115),fill='black',width=width)
    d.rounded_rectangle((x1-18,y1+125,x1+55,y1+178),radius=10,outline='black',width=width)
    return (x1+55,body_top+65,x2-55,y2-55)

def draw_luggage_tag_outline(canvas, box, width=12):
    d=ImageDraw.Draw(canvas); d.rounded_rectangle(box,radius=55,outline='black',width=width); cx=(box[0]+box[2])//2; d.ellipse((cx-45,box[1]+45,cx+45,box[1]+135),outline='black',width=width)
    return (box[0]+40,box[1]+165,box[2]-40,box[3]-40)
