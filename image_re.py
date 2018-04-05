from PIL import Image

hight = 160
width = 420
text = ''
try:
    image_file = raw_input('image file:')
except:
    print 'input fail'
def get_char(r, g, b, d=256):
    if d == 0:
        return ''
    a = (2126 *r + 7152 * g + 722 * b)/10000
    ascii_char = list("qwertyuiopasdfghjklzxcvbnm[];'\,./1234567890-=`~!@#$%^&*()_+{}:\"|<>?")
    c = int((a/(d + 1.0)) *len(ascii_char))
    return ascii_char[c]
    
im = Image.open(image_file)
im = im.resize((width, hight), Image.NEAREST)
for i in xrange(hight):
    for j in xrange(width):
        content = im.getpixel((j, i))
        text += get_char(*content)
    text += '\n'
# print text
re_file = open('image_re.txt', 'w')
re_file.write(text)
re_file.close()
