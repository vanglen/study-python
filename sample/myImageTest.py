# coding: utf-8

from PIL import Image

im = Image.open(r'aaa.jpg')
w, h = im.size
im.thumbnail((w//2, h//2))
im.save(r'bbb.jpg', 'jpeg')
