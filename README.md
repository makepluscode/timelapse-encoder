# GOPRO TIMELAPS TO VIDEO

This repository contains scripts designed for handling GoPro time-lapse files: `group_files.py` and `encode.py`. These tools are tailored for organizing GoPro image files and converting them into a cohesive time-lapse video.

## group_files.py

### Description

The `group_files.py` script is designed to manage and organize JPEG images from GoPro time-lapses. It groups images based on their modification times, segregates them into corresponding directories, and compiles their details into a CSV file.

### Usage

1. Ensure all your GoPro JPG time-lapse files are in a directory named `timelaps`.
2. Run the script in your Python environment:


### Output

- Creates grouped subdirectories in the `timelaps` directory.
- Each group contains a series of images, sorted and segregated based on the modification time.
- Generates a CSV file `file_info.csv`, cataloging each image's name, modification time, size, and group number.

## encode.py

### Description

`encode.py` takes the organized images from the GoPro time-lapse and encodes them into a video file. This script resizes images to a standard width (default is 1920 pixels) and compiles them into a video format.

### Requirements

- Python
- OpenCV-Python package (`opencv-python`)

Install it using:


### Usage

Run the script with the following command, specifying the image folder, output video name, and frame rate:


Replace `[image_folder]`, `[video_name]`, and `[fps]` with your desired folder path, output video name, and frames per second.

### Example


This command processes images from the `grouped_timelaps` folder and creates a video named `output_video.mp4` at 30 FPS.

---
