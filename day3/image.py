from PIL import Image

im = Image.open("photo.jpg")
im.thumbnail((100, 100))
im.save('photo_thumbnail.jpg', 'JPEG')