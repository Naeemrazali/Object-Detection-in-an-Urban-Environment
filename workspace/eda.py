from utils import get_dataset
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Rectangle
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from glob import glob
import io
from PIL import Image
import matplotlib
import math
import IPython.display as display

#matplotlib.use('TkAgg')

feature_descriptions = {
    'image/height': tf.io.VarLenFeature(tf.int64),
    'image/width': tf.io.VarLenFeature(tf.int64),
    'image/encoded': tf.io.FixedLenFeature([], tf.string),
    'image/object/bbox/xmin': tf.io.VarLenFeature(tf.float32),
    'image/object/bbox/xmax': tf.io.VarLenFeature(tf.float32),
    'image/object/bbox/ymin': tf.io.VarLenFeature(tf.float32),
    'image/object/bbox/ymax': tf.io.VarLenFeature(tf.float32),
    'image/object/class/text': tf.io.VarLenFeature(tf.string),
    'image/object/class/label': tf.io.VarLenFeature(tf.int64)
}


def _parse_image_fn(example):
    return tf.io.parse_single_example(example, feature_descriptions)

def give_image(image_dataset):
    for e in image_dataset:
        image = Image.open(io.BytesIO(e['image/encoded'].numpy()))
    return image

def give_bbox(e):
    xmins = e['image/object/bbox/xmin'].values.numpy()
    ymins = e['image/object/bbox/ymin'].values.numpy()
    xmaxs = e['image/object/bbox/xmax'].values.numpy()
    ymaxs = e['image/object/bbox/ymax'].values.numpy()

    for i, xmin in enumerate(xmins):
        xmin = xmin * 640
        xmin = xmin / 1920
        xmins[i] = math.floor(xmin * 640)

    for i, ymin in enumerate(ymins):
        ymin = ymin * 640
        ymin = ymin / 1080
        ymins[i] = math.floor(ymin * 640 - 75)

    for i, xmax in enumerate(xmaxs):
        xmax = xmax * 640
        xmax = xmax / 1920
        xmaxs[i] = math.floor(xmax * 640)

    for i, ymax in enumerate(ymaxs):
        ymax = ymax * 640
        ymax = ymax / 1080
        ymaxs[i] = math.floor(ymax * 640 - 75)
    return xmins, ymins, xmaxs, ymaxs

def give_label(e):
    labels = e['image/object/class/label'].values.numpy()
    return labels

def draw_bbox(ax, labels, xmins, ymins, xmaxs, ymaxs):
    #something
    colormap = {1: [1, 0, 0], 2: [0, 1, 0], 4: [0, 0, 1]}

    for i, label in enumerate(labels):
        xmin = xmins[i]
        ymin = ymins[i]
        xmax = xmaxs[i]
        ymax = ymaxs[i]

        rec = Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, facecolor='none', edgecolor=colormap[label])
        ax.add_patch(rec)

def show_images(image_dataset):
    f, ax = plt.subplots(2, 5, figsize=(20,20))
    x = 0
    y = 0

    for e in image_dataset:
        xmins, ymins, xmaxs, ymaxs = give_bbox(e)
        labels = give_label(e)
        img = Image.open(io.BytesIO(e['image/encoded'].numpy()))
        ax[x, y].imshow(img)
        draw_bbox(ax[x, y], labels, xmins, ymins, xmaxs, ymaxs)
        ax[x, y].axis('off')

        x = (x+1) % 2
        y = (y+1) % 5
    plt.show()

if __name__ == "__main__":

    tfr_filepaths = glob("./data/processed/*.tfrecord")
    dataset = tf.data.TFRecordDataset(tfr_filepaths)

    image_dataset = dataset.map(_parse_image_fn)
    
    image_dataset = image_dataset.shuffle(500)
    image_dataset = image_dataset.take(10)

    show_images(image_dataset)
    



    


    
