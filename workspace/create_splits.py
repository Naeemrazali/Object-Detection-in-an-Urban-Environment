import argparse
import glob
import os
import random
import math
import shutil
import stat

import numpy as np

from utils import get_module_logger


def split(data_dir, dest_dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.

    args
        - data_dir [str]: data directory, /mnt/data
    """
    
    
    # Create three folders 
    trainingDest = os.path.join(dest_dir, 'train')
    validationDest = os.path.join(dest_dir, 'val')
    testingDest = os.path.join(dest_dir, 'test')
    os.makedirs(trainingDest, exist_ok=True)
    os.makedirs(validationDest, exist_ok=True)
    os.makedirs(testingDest, exist_ok=True)
                               
    fileList = glob.glob(os.path.join(data_dir, '*.tfrecord'))
    numFiles = len(fileList)
    # Split dataset into trainig 70% testing 20% validation 10%
    numTrain = math.floor(0.7 * numFiles)
    numTest = math.floor(0.2 * numFiles)
    numVal = math.floor(0.1 * numFiles)
    numTrain = numTrain + (numFiles - numTrain - numTest - numVal)
    #print(numTrain, numTest, numVal)
    random.shuffle(fileList)
    
    for i, file in enumerate(fileList):
        filePath = os.path.join(data_dir, file)
        if i < numTrain:
            shutil.move(filePath, trainingDest)
        elif i < numTest + numTrain:
            shutil.move(filePath, validationDest)
        else:
            shutil.move(filePath, testingDest)
    
    

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data_dir', required=True,
                        help='data directory')
    parser.add_argument('--dest_dir', required=True, help="destination directory")
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir, args.dest_dir)