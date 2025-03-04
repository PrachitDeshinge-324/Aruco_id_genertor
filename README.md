# ArUco Marker Generator

This script generates ArUco markers based on customizable parameters. ArUco markers are used in computer vision tasks like augmented reality, robotics, and calibration. The generated markers are saved as PNG images in the specified folder.

## Features

- Generates ArUco markers with customizable size, border, and dictionary type.
- Allows you to generate a specific range of marker IDs.
- Saves the markers as PNG files in the desired output folder.

## Requirements

- Python 3.x
- OpenCV (`opencv-python` and `opencv-contrib-python` packages)

You can install the required dependencies using pip:

```bash
pip install opencv-python opencv-contrib-python
```
## Usage

You can specify the following parameters when running the script:

### Command Line Arguments

- `--output_folder (str)`: Folder to save the generated ArUco markers (default: `aruco_markers`).
- `--size (int)`: Size of the ArUco markers in pixels (default: 200).
- `--border (int)`: Border thickness of the ArUco markers in bits (default: 1).
- `--dictionary_id (int)`: ArUco dictionary type ID (default: `cv2.aruco.DICT_5X5_1000`).
- `--start_id (int)`: Starting marker ID (default: 0).
- `--end_id (int)`: Ending marker ID (default: `None`, meaning all markers in the dictionary).

### Example Usage

#### Basic Usage

To generate ArUco markers using the default parameters and save them in the `aruco_markers` folder:

```bash
python generate_aruco_markers.py --output_folder "custom_output" --size 1000 --border 3 --dictionary_id 7 --start_id 0 --end_id 999
```

## Supported Dictionaries

The following predefined ArUco dictionaries are supported:

- `DICT_4X4_50` (ID: 0)
- `DICT_4X4_100` (ID: 1)
- `DICT_4X4_250` (ID: 2)
- `DICT_4X4_1000` (ID: 3)
- `DICT_5X5_50` (ID: 4)
- `DICT_5X5_100` (ID: 5)
- `DICT_5X5_250` (ID: 6)
- `DICT_5X5_1000` (ID: 7)
- `DICT_6X6_50` (ID: 8)
- `DICT_6X6_100` (ID: 9)
- `DICT_6X6_250` (ID: 10)
- `DICT_6X6_1000` (ID: 11)
- `DICT_7X7_50` (ID: 12)
- `DICT_7X7_100` (ID: 13)
- `DICT_7X7_250` (ID: 14)
- `DICT_7X7_1000` (ID: 15)
