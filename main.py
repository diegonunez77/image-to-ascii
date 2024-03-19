from PIL import Image

image = Image.open('input.jpg')

with Image.open('input.jpg') as im:
    im = im.convert("L")
    im = im.resize((128, 128))

ASCII_CHARS = "@$B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. "

width, height = im.size

ascii_art = ""

for y in range(height):
    for x in range(width):
        pixel_brightness = im.getpixel((x, y))
        index = int((pixel_brightness / 255) * (len(ASCII_CHARS) - 1))
        ascii_art += ASCII_CHARS[index]
    ascii_art += '\n'

output = 'output.txt'

with open(output, 'w') as file:
    file.write(ascii_art)

print(f"ASCII art has been saved to '{output}'.")
        