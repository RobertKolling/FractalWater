import random
from PIL import Image
import noise

# Image size (width, height)
size = (800, 600)

# Create a new image with a black background
img = Image.new("RGB", size, (0, 0, 0))
pixels = img.load()

# Fractal noise parameters
octaves = 6
persistence = 0.5
lacunarity = 2.0

# Generate fractal noise
for x in range(img.width):
    for y in range(img.height):
        value = noise.pnoise3(x/50, y/50, octaves, persistence, lacunarity)
        value = (value + 1) / 2
        r = int(random.uniform(50, 150) * value)
        g = int(random.uniform(100, 200) * value)
        b = int(random.uniform(150, 255) * value)
        pixels[x, y] = (r, g, b)

# Save the image
img.save("fractal_water.png")
