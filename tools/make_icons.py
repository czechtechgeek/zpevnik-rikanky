#!/usr/bin/env python3
"""Vygeneruje ikony add-onu (128 a 256 px) — notička na terakotovém pozadí."""
from PIL import Image, ImageDraw

BG = (180, 83, 42)
FG = (255, 248, 239)


def make(size: int) -> Image.Image:
    scale = size / 512
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=int(112 * scale), fill=BG)

    def s(*v):
        return [int(x * scale) for x in v]

    # nota
    d.ellipse(s(144, 300, 248, 404), fill=FG)
    d.rounded_rectangle(s(232, 120, 254, 356), radius=int(10 * scale), fill=FG)
    d.polygon(
        [
            (254 * scale, 120 * scale),
            (350 * scale, 126 * scale),
            (350 * scale, 196 * scale),
            (254 * scale, 190 * scale),
        ],
        fill=FG,
    )
    return img


for size, name in ((128, "icon.png"), (256, "logo.png")):
    make(size).save(f"addon/{name}")
    print(f"addon/{name}")
