import cv2
import os
import glob
import argparse
import sys
import re


def sort_key(filename):
    numbers = re.findall(r'\d+', filename)
    return int(numbers[0]) if numbers else 0


def convert_png_to_mp4(input_directory, output_file, num_frames, duration, width, height):
    images = glob.glob(os.path.join(input_directory, '*.png'))
    images.sort(key=sort_key)

    if not images:
        raise RuntimeError(
            f"No PNG files found in directory: {input_directory}")

    if num_frames > len(images):
        raise RuntimeError(
            f"Insufficient frames: {len(images)} available, but {num_frames} needed.")

    size = (width, height)

    video = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(
        *'avc1'), num_frames / duration, size)

    frame_interval = len(images) / num_frames
    current_frame = 0

    for i in range(num_frames):
        index = int(current_frame)
        img = cv2.imread(images[index])
        img = cv2.resize(img, size)
        video.write(img)
        current_frame += frame_interval

    video.release()


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Convert a series of PNG images to an MP4 video.')
    parser.add_argument('--input', type=str, required=True,
                        help='Input directory containing PNG files.')
    parser.add_argument('--output', type=str, required=True,
                        help='Output MP4 file path.')
    parser.add_argument('--num_frames', type=int, required=True,
                        help='Total number of frames to use.')
    parser.add_argument('--duration', type=int, required=True,
                        help='Duration of the output video in seconds.')
    parser.add_argument('--width', type=int, default=1920,
                        help='Width of the output video. Default is 1920.')
    parser.add_argument('--height', type=int, default=1080,
                        help='Height of the output video. Default is 1080.')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()

    if not os.path.exists(args.input):
        print(f"Input directory {args.input} does not exist.", file=sys.stderr)
        sys.exit(1)

    try:
        convert_png_to_mp4(args.input, args.output, args.num_frames,
                           args.duration, args.width, args.height)
    except RuntimeError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
