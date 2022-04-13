import os
import zipfile
import random
import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from shutil import copyfile

!wget --no-check-certificate \
    "https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_3367a.zip" \
    -O "/tmp/cats-and-dogs.zip"

local_zip = '/tmp/cats-and-dogs.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/tmp')
zip_ref.close()

print(len(os.listdir('/tmp/PetImages/Cat/')))
print(len(os.listdir('/tmp/PetImages/Dog/')))

def split_data(SOURCE, TRAINING, TESTING, SPLIT_SIZE):
# YOUR CODE STARTS HERE
  source_files = os.listdir(SOURCE)

  for source_file in source_files:
    if os.path.getsize(SOURCE + '/' + source_file) == 0:
      source_files.remove(source_file)
      print(source_file + ' is zero length, so ignoring')

  source_files_len = len(source_files)
  source_files = random.sample(source_files, source_files_len)

  source_files_training_len = (int)(source_files_len * SPLIT_SIZE)
  source_files_testing_len = source_files_len - source_files_training_len

  source_files_training = source_files[:source_files_training_len]
  source_files_testing = source_files[:-source_files_testing_len]

  for source_training_file in source_files_training:
    copyfile(SOURCE + '/' + source_training_file, TRAINING)

  for source_testing_file in source_files_testing:
    copyfile(SOURCE + '/' + source_testing_file, TESTING)

# YOUR CODE ENDS HERE

CAT_SOURCE_DIR = "/tmp/PetImages/Cat/"
TRAINING_CATS_DIR = "/tmp/cats-v-dogs/training/cats/"
TESTING_CATS_DIR = "/tmp/cats-v-dogs/testing/cats/"
DOG_SOURCE_DIR = "/tmp/PetImages/Dog/"
TRAINING_DOGS_DIR = "/tmp/cats-v-dogs/training/dogs/"
TESTING_DOGS_DIR = "/tmp/cats-v-dogs/testing/dogs/"

split_size = .9
split_data(CAT_SOURCE_DIR, TRAINING_CATS_DIR, TESTING_CATS_DIR, split_size)
split_data(DOG_SOURCE_DIR, TRAINING_DOGS_DIR, TESTING_DOGS_DIR, split_size)
