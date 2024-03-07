import os
import tensorflow as tf
import pandas as pd

def create_tfrecord(input_dir, output_dir, class_id_mapping, annotations_file, output_tfrecord_filename):
    # Load the annotations CSV file
    annotations = pd.read_csv(annotations_file)

    # Create the TFRecord writer
    writer = tf.io.TFRecordWriter(os.path.join(output_dir, output_tfrecord_filename))

    # Iterate over the annotations dataframe and create a TFRecord example for each image
    for index, row in annotations.iterrows():
        image_path = os.path.join(input_dir, row["filename"])
        width = int(row["width"])
        height = int(row["height"])
        class_name = row["class"]
        class_id = class_id_mapping[class_name]
        xmin = float(row["xmin"])
        ymin = float(row["ymin"])
        xmax = float(row["xmax"])
        ymax = float(row["ymax"])
        example = create_example(image_path, width, height, class_id, xmin, ymin, xmax, ymax)
        writer.write(example)

    writer.close()

# Define the input and output directories
input_dir = "/path/to/input_dir"
output_dir = "/path/to/output_dir"
output_tfrecord_filename = "any_filename.tfrecord"
class_id_mapping = {"class_placeholder": 1}  # Replace "class_placeholder" with a generic class name

# Define the path to the annotations CSV file
annotations_file = os.path.join(input_dir, "_annotations.csv")

# Call the create_tfrecord function
create_tfrecord(input_dir, output_dir, class_id_mapping, annotations_file, output_tfrecord_filename)
