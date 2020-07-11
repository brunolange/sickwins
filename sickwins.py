import os
import argparse

import imageio
import tqdm


__author__ = "Bruno Lange"


def main(config):
    files = sorted(
        [
            f
            for f in os.listdir(config.folder)
            if os.path.isfile(os.path.join(config.folder, f))
        ]
    )
    output = os.path.join(config.folder, "movie.gif")
    with imageio.get_writer(
        output, "GIF-FI", mode="I", duration=2, quantizer="nq"
    ) as writer:
        for file in tqdm.tqdm(files, desc="Writing gif from images..."):
            image = imageio.imread(os.path.join(config.folder, file))
            writer.append_data(image)

    print(f"Saved gif to {output}")


def validate_folder(value):
    path = os.path.realpath(value)
    if not os.path.isdir(path):
        raise argparse.ArgumentTypeError("Need a valid folder")
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "folder", help="Folder containing the images", type=validate_folder
    )
    main(parser.parse_args())
