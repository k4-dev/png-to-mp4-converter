# png-to-mp4-converter

By following the steps below, you can convert multiple PNG frames into a single MP4 file.

## Setting
Install dependencies:
```
$ pip install -r requirements.txt
```

## Conversion
Execute by specifying the source path, save destination, num_frames, duration, width(default is 1920), and height(default is 1080):
```
$ python src/png_to_mp4.py \
--input input/ \
--output output/result.mp4 \
--num_frames 10 \
--duration 1 \
--width 3840 \
--height 2160
```

## Result
You will find the integrated MP4 file like:
- [result.mp4](https://github.com/mozu-dev/png-to-mp4-converter/blob/main/output/result.mp4)

## License
[MIT license](https://github.com/mozu-dev/png-to-mp4-converter/blob/main/LICENSE)