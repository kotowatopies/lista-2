from PIL import Image
import os
def get_thumbnail(input_path, output_path, thumbnail_size):
    '''resizes choosen image to make it into thumbnail (without distortion)
    arguments:
        input_path (str): path to original file (must be png or jpg)
        output_path (str): path to generated thumbnail
        thumbnail_size (tuple): tuple with maximal size of thumbnail
    raises:
        TypeError: raised when one of arguments has incorrect type
        ValueError: raised when path to original file doesnt exist
        TypeError: raise when image extension isnt supported
        FileExistsError: raised when output path already lead to other file
    returns:
        None
    '''
    print(type(thumbnail_size))
    if __name__ == "__main__":
        if not isinstance(input_path, str) or not isinstance(output_path, str) or not isinstance(thumbnail_size, tuple):
            raise TypeError("one of inputs has wrong type")
        elif not os.path.exists(input_path):
            raise ValueError("path does not exist")
        elif os.path.splitext(input_path)[1] not in [".jpg", ".png"]:
            raise TypeError("wrong image format inputed")
        elif os.path.exists(output_path):
            raise FileExistsError('output path already leads to a file')
        else:
            image = Image.open(input_path)
            image.thumbnail(thumbnail_size)
            try:
                image.save(output_path)
                image.show()
            except Exception as e:
                print(f'thumbnail couldnt be saved error ocured, Error: {e}')
get_thumbnail(r"E:\277477\programowanie\sem 2\lista 2\obrazek.jpg", r"E:\277477\programowanie\sem 2\lista 2\maly_obrazek.jpg", (100,100))
