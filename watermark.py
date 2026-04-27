"""
Watermark script — subtle JBA grid (4-8 marks per image)
Paintings: re-process from originals, save as JPEG to images/watercolor/
Logos:     copy from Logo folder, save as PNG to images/logo/
"""
import os, math
from PIL import Image, ImageDraw, ImageFont

WEBSITE = "/Users/jenniferba/Documents/AI_Agents/JBA Website"
WATERCOLOR_SRC = "/Users/jenniferba/Documents/My Art Portfolios/Watercolor"
LOGO_SRC = "/Users/jenniferba/Documents/My Art Portfolios/Logo"

WATERCOLOR_MAP = {
    "Rose12x15 _2.JPG":              "rose.jpg",
    "white rose 12x15_2.jpeg":       "whiterose.jpg",
    "Tulip12x15_2.JPG":              "tulip.jpg",
    "WaterLily12x15_2.JPG":         "waterlily.jpg",
    "SunFlowers 12x15_2.JPG":       "sunflowers.jpg",
    "YellowFlower12x15_2.JPG":      "yellowflower.jpg",
    "Wild Flowers 7.5x9_2.JPG":     "wildflowers.jpg",
    "Hydrangea 12x15_2.JPG":        "hydrangea.jpg",
    "Lily12x15_2.JPG":               "lily.jpg",
    "Cat 7.5x11_2.JPG":             "cat.jpg",
    "Tiger 7.5x11 _2.JPG":          "tiger.jpg",
    "GoldenFish 7.5x11_2.JPG":      "goldenfish.jpg",
    "LeLe.jpeg":                     "lele.jpg",
    "IC.jpg":                        "ic.jpg",
}

LOGO_MAP = {
    "NACBC Logo (red).png":                        "nacbc-red.png",
    "NACBC Logo with Glow (red).png":              "nacbc-glow-red.png",
    "NACBC Logo with Glow (white).png":            "nacbc-glow-white.png",
    "NuB7Logo_v2.png":                             "nub7-v2.png",
    "NuB7Logo_v3.png":                             "nub7-v3.png",
    "NuB7Logo_v4.png":                             "nub7-v4.png",
    "RED Logo-GreenWhite-updated (large).png":     "red-green-white.png",
    "RED Logo-RedWhite-updated (medium large).png":"red-red-white.png",
}

FONT_PATHS = [
    "/System/Library/Fonts/Helvetica.ttc",
    "/System/Library/Fonts/Arial.ttf",
    "/Library/Fonts/Arial.ttf",
]

def get_font(size):
    for path in FONT_PATHS:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()

def add_watermark_grid(img_rgba, text="JBA", opacity=50, cols=3, rows=2, angle=-35):
    W, H = img_rgba.size
    font_size = max(28, int(W * 0.045))
    font = get_font(font_size)

    # Measure text
    tmp = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    bbox = tmp.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]

    wm_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))

    for r in range(rows):
        for c in range(cols):
            cx = int(W * (c + 0.5) / cols)
            cy = int(H * (r + 0.5) / rows)

            pad = max(tw, th) + 20
            stamp = Image.new("RGBA", (pad * 2, pad * 2), (0, 0, 0, 0))
            d = ImageDraw.Draw(stamp)
            d.text((pad - tw // 2, pad - th // 2), text, font=font,
                   fill=(255, 255, 255, opacity))
            stamp = stamp.rotate(angle, expand=False)

            sx = cx - stamp.width // 2
            sy = cy - stamp.height // 2
            wm_layer.paste(stamp, (sx, sy), stamp)

    return Image.alpha_composite(img_rgba, wm_layer)


# ── Paintings ────────────────────────────────────────────────────────────────
out_wc = os.path.join(WEBSITE, "images", "watercolor")
os.makedirs(out_wc, exist_ok=True)

for src_name, dst_name in WATERCOLOR_MAP.items():
    src = os.path.join(WATERCOLOR_SRC, src_name)
    dst = os.path.join(out_wc, dst_name)
    if not os.path.exists(src):
        print(f"  SKIP (not found): {src_name}")
        continue
    img = Image.open(src).convert("RGBA")
    result = add_watermark_grid(img, opacity=50, cols=3, rows=2)
    result.convert("RGB").save(dst, "JPEG", quality=88, optimize=True)
    print(f"  Painting: {dst_name}")

# ── Logos ────────────────────────────────────────────────────────────────────
out_logo = os.path.join(WEBSITE, "images", "logo")
os.makedirs(out_logo, exist_ok=True)

for src_name, dst_name in LOGO_MAP.items():
    src = os.path.join(LOGO_SRC, src_name)
    dst = os.path.join(out_logo, dst_name)
    if not os.path.exists(src):
        print(f"  SKIP (not found): {src_name}")
        continue
    img = Image.open(src).convert("RGBA")
    # For logos use fewer marks and slightly darker watermark
    result = add_watermark_grid(img, opacity=55, cols=2, rows=2, angle=-35)
    result.save(dst, "PNG", optimize=True)
    print(f"  Logo: {dst_name}")

print("Done.")
