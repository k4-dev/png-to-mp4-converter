import cv2
import os
import glob
import argparse
import sys
import re

def sort_key(filename):
    numbers = re.findall(r'\d+', filename)
    return int(numbers[0]) if numbers else 0

def convert_png_to_mp4(input_directory, output_file, frame_rate):
    images = glob.glob(os.path.join(input_directory, '*.png'))
    images.sort(key=sort_key)

    if not images:
        raise RuntimeError(
            f"No PNG files found in directory: {input_directory}")

    frame = cv2.imread(images[0])
    height, width, _ = frame.shape
    size = (width, height)

    video = cv2.VideoWriter(
        output_file, cv2.VideoWriter_fourcc(*'avc1'), frame_rate, size)

    for image in images:
        video.write(cv2.imread(image))

    video.release()


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Convert a series of PNG images to an MP4 video.')
    parser.add_argument('--input', type=str, required=True,
                        help='Input directory containing PNG files.')
    parser.add_argument('--output', type=str, required=True,
                        help='Output MP4 file path.')
    parser.add_argument('--framerate', type=float, default=30,
                        help='Frame rate of the output video. Default is 30.')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()

    if not os.path.exists(args.input):
        print(f"Input directory {args.input} does not exist.", file=sys.stderr)
        sys.exit(1)

    convert_png_to_mp4(args.input, args.output, args.framerate)