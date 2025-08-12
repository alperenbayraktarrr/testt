import argparse
from pathlib import Path
from typing import List, Tuple

from PIL import Image


def compute_segments(total: int, num_parts: int = 3) -> List[int]:
    base = total // num_parts
    remainder = total % num_parts
    # Distribute the remainder by adding 1 pixel to the first `remainder` parts
    return [base + (1 if i < remainder else 0) for i in range(num_parts)]


def split_image_three(input_path: Path, output_dir: Path, orientation: str) -> List[Path]:
    image = Image.open(input_path)
    width, height = image.size

    if orientation == "vertical":
        segment_widths = compute_segments(width, 3)
        x = 0
        boxes: List[Tuple[int, int, int, int]] = []
        for seg_w in segment_widths:
            boxes.append((x, 0, x + seg_w, height))
            x += seg_w
    elif orientation == "horizontal":
        segment_heights = compute_segments(height, 3)
        y = 0
        boxes = []
        for seg_h in segment_heights:
            boxes.append((0, y, width, y + seg_h))
            y += seg_h
    else:
        raise ValueError("orientation must be 'vertical' or 'horizontal'")

    output_dir.mkdir(parents=True, exist_ok=True)

    # Preserve original format/extension if possible
    img_format = image.format or "PNG"
    ext = input_path.suffix[1:] if input_path.suffix else "png"

    outputs: List[Path] = []
    for idx, box in enumerate(boxes, start=1):
        cropped = image.crop(box)
        out_path = output_dir / f"{input_path.stem}_part{idx}.{ext}"
        cropped.save(out_path, format=img_format)
        outputs.append(out_path)

    return outputs


def main() -> None:
    parser = argparse.ArgumentParser(description="Split an image into three equal parts.")
    parser.add_argument("input", type=Path, help="Path to the input image (e.g., /path/to/image.png)")
    parser.add_argument(
        "--orientation",
        choices=["vertical", "horizontal"],
        default="vertical",
        help="Split direction: vertical (left-to-right) or horizontal (top-to-bottom). Default: vertical",
    )
    parser.add_argument(
        "--outdir",
        type=Path,
        default=None,
        help="Directory to save outputs. Defaults to the same directory as the input image.",
    )

    args = parser.parse_args()

    input_path: Path = args.input
    if not input_path.exists():
        raise SystemExit(f"Input image not found: {input_path}")

    output_dir: Path = args.outdir if args.outdir is not None else input_path.parent

    outputs = split_image_three(input_path=input_path, output_dir=output_dir, orientation=args.orientation)

    # Print resulting paths for convenience
    for p in outputs:
        print(p)


if __name__ == "__main__":
    main()