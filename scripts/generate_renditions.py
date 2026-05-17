#!/usr/bin/env python3
"""Generate web + Open Graph renditions from the source painting.

Run once after updating images/source/De_Bierdrinkers-2.jpg.
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "images" / "source" / "De_Bierdrinkers-2.jpg"
OUT_WEB = ROOT / "images" / "de-baolse-bierdrinkers.jpg"
OUT_OG = ROOT / "images" / "og-image.jpg"


def resize(img: Image.Image, target_width: int) -> Image.Image:
    if img.width <= target_width:
        return img.copy()
    ratio = target_width / img.width
    target_height = round(img.height * ratio)
    return img.resize((target_width, target_height), Image.LANCZOS)


def main() -> None:
    with Image.open(SRC) as src:
        src.load()
        if src.mode != "RGB":
            src = src.convert("RGB")

        web = resize(src, 2000)
        web.save(OUT_WEB, "JPEG", quality=85, optimize=True, progressive=True)

        og = resize(src, 1200)
        og.save(OUT_OG, "JPEG", quality=82, optimize=True, progressive=True)

    for path in (OUT_WEB, OUT_OG):
        with Image.open(path) as img:
            print(f"{path.relative_to(ROOT)}: {img.width}x{img.height}, "
                  f"{path.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
