# sickwins

`sickwins` provides a simple command line tool to capture a sequence of images into a high-quality gif.

![Tony Hawk](movie.gif)

```
$ pip install sickwins
$ sickwins --help
usage: sickwins [-h] [--duration DURATION] [--quantizer QUANTIZER] folder

positional arguments:
  folder                Folder containing the images

optional arguments:
  -h, --help            show this help message and exit
  --duration DURATION   Seconds per frame
  --quantizer QUANTIZER, -q QUANTIZER
```

Example:

```
$ sickwins ~/Desktop/tony-hawk-900
Saved gif to ~/Desktop/tony-hawk-900/movie.gif
```
