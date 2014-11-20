from PIL import Image, ImageFilter

im = Image.open(r'aaa.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save(r'ccc.jpg', 'jpeg')
im2.show()
