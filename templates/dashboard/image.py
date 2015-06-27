from PIL import Image
m_name = 'test6.png'
image = Image.open('/home/kd/Pictures/%s'%im_name)
path = '/home/kd/Pictures/%s'%im_name
name = path[18:]

large_size = (1920, 1200)

im = Image.open(image)

image_w, image_h = im.size
aspect_ratio = image_w / float(image_h)
new_height = int(large_size[0] / aspect_ratio)

if new_height < 1200:
    final_width = large_size[0]
    final_height = new_height
else:
    final_width = int(aspect_ratio * large_size[1])
    final_height = large_size[1]

imaged = im.resize((final_width, final_height), Image.ANTIALIAS)

imaged.show()
imaged.save("out.jpg", quality=90)