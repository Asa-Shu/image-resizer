import os
import glob
from PIL import Image

# set the path
files = glob.glob('/Users/as/images/*')
dst_dir = '/Users/as/images_800'

SIZE = (800, 800)
BACKGROUND_COLOR = (255, 255, 255)


def expand_to_square(pil_img, BACKGROUND_COLOR):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new('RGB', (width, width), BACKGROUND_COLOR)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new('RGB', (height, height), BACKGROUND_COLOR)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result


for file in files:
    root, ext = os.path.splitext(file)
    if ext in ['.png', '.jpg', '.jpeg', '.webp']:
        img = Image.open(file)
        img = expand_to_square(img, BACKGROUND_COLOR)
        img_resize = img.resize(SIZE)
        basename = os.path.basename(root)
        img_resize.save(os.path.join(dst_dir, basename + '_800' + ext))
