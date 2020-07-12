import os
import argparse

import imageio
import tqdm


__all__ = ["main"]


def validate_folder(value):
    path = os.path.realpath(value)
    if not os.path.isdir(path):
        raise argparse.ArgumentTypeError("Need a valid folder")
    return path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "folder", help="Folder containing the images", type=validate_folder
    )
    parser.add_argument("--output", "-o", default="movie.gif", help="Output file")
    parser.add_argument("--duration", default=0.5, help="Seconds per frame", type=float)
    parser.add_argument("--quantizer", "-q", default="nq")
    config = parser.parse_args()

    files = sorted(
        [
            f
            for f in os.listdir(config.folder)
            if os.path.isfile(os.path.join(config.folder, f))
        ]
    )
    with imageio.get_writer(
        config.output,
        "GIF-FI",
        mode="I",
        duration=config.duration,
        quantizer=config.quantizer,
    ) as writer:
        for file in tqdm.tqdm(files, desc="Writing gif from images..."):
            try:
                image = imageio.imread(os.path.join(config.folder, file))
            except ValueError:
                continue
            writer.append_data(image)

    print(f"Saved gif to {config.output}")
