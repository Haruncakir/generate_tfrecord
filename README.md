# Creating TFRecord from Annotations CSV

This script converts image annotations stored in a CSV file into TFRecord format, which is commonly used in TensorFlow for efficient data loading. TFRecord is a binary file format that stores serialized data, making it faster and more memory-efficient to read data during training.

## Requirements
- Python 3.x
- TensorFlow
- pandas

## Installation
1. Install the required libraries using pip:
```bash
pip install tensorflow pandas
``` 

## Usage
1. Update the input directory (input_dir), output directory (output_dir), output TFRecord filename (output_tfrecord_filename), and class ID mapping (class_id_mapping) in the script as per your dataset.

2. Prepare your dataset annotations in a CSV file with the following columns:
    filename: Name of the image file.
    width: Width of the image.
    height: Height of the image.
    class: Class name of the object in the image.
    xmin: Minimum x-coordinate of the bounding box.
    ymin: Minimum y-coordinate of the bounding box.
    xmax: Maximum x-coordinate of the bounding box.
    ymax: Maximum y-coordinate of the bounding box.

3. Run the script to create the TFRecord:
```bash
pip install tensorflow pandas 
```


## Example
For a sample dataset, consider the following directory structure:
dataset/
├── images/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
└── annotations.csv

Here's how the CSV file (annotations.csv) might look like:
```csv
filename,width,height,class,xmin,ymin,xmax,ymax
image1.jpg,640,480,cat,100,100,300,300
image2.jpg,800,600,dog,200,150,500,450
...
```

You would update the script as follows:
  ```python
  input_dir = "dataset/images"
  output_dir = "tfrecord"
  output_tfrecord_filename = "dataset.tfrecord"
  class_id_mapping = {"cat": 1, "dog": 2}
  annotations_file = "dataset/annotations.csv"
  ```
  
Feel free to adjust the instructions and paths as needed for your specific dataset and project structure.
