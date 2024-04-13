from PIL import Image, ImageDraw, ImageFont
import os 
def add_watermark(input_path, output_path, watermark_text):
    '''add text watermark to image
    arguments: 
        input_path (str): path to original file
        output_path (str): path to place where image will be saved
        watermark_text (str): watermark text
    raises:
        FileNotFoundError: raises when input path wasnt found
        TypeError: raises when wrong file extension was inputed
    retrns:
        None
    '''
    if __name__=="__main__":
        if not os.path.exists(input_path):
            raise FileNotFoundError("this path doesnt exist")
        if os.path.splitext(input_path)[1] not in [".jpg", ".png"]:
            raise TypeError("wrong file extention on inputed path")
        if not isinstance(input_path, str) \
        or not isinstance(output_path, str) \
        or not isinstance(watermark_text, str):
            raise TypeError("at least one variable has wrong type")
        image = Image.open(input_path)
        font = ImageFont.truetype(r"G:\277477\programowanie\sem 2\lista 2\arial.ttf", 154) #czcionka i rozmiar
        # text_width, text_height = font.getsize(watermark_text) ??? nie działa
        color = (255,255,255)
        # if image.width < text_width or image.height < text_height:
        #     print("image is too small for watermark change size or lenght of text")
        #     return None
        position = (10 , image.height/2)
        draw = ImageDraw.Draw(image)
        draw.text(position, watermark_text, font=font, fill=color)
        image.save(output_path)
add_watermark(r"E:\277477\programowanie\sem 2\lista 2\obrazek.jpg", r"E:\277477\programowanie\sem 2\lista 2\obrazek_wodny.jpg", "jakiś tam\nznak wodny")