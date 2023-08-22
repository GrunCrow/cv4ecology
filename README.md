# AI-Census: Automated Census and Biodiversity Monitoring System using Deep Learning

<!--![Project Logo](project_logo.png) <!-- You can add a logo/image related to your project here -->

## Description

The "Automated Census and Biodiversity Monitoring System using Deep Learning" is an ongoing project focused on developing an advanced protocol and workflow for wildlife monitoring using camera trapping, citizen science, and deep learning techniques. The primary objective of this project is to create a powerful Neural Network for species classification using camera-trap images obtained from Doñana National Park.

By leveraging cutting-edge deep learning methods, the project aims to achieve unbiased estimates of species and community dynamics. This will enable cost-effective and prompt responses to ecological changes, ultimately contributing to the conservation and understanding of biodiversity in the region.

## Features

- Utilization of camera-trap images from Doñana National Park.
- Generation of bounding boxes and JSON annotations for images in COCO format.
- Development of a comprehensive dataset for training, validation and evaluation.
- Creation of a state-of-the-art Neural Network for species detection and classification.
<!--- Advanced techniques for optimizing model performance and efficiency.-->


## Project Structure

The repository is organized as follows:

- `AI_Census/`: Contains main code related to the model.
- `Assignments/`: Contains cv4ecology workshop assigments before workshop started.
    - `Assignment0_DataExploration/`: Data Visualization from COCO file.
- `configs/`: Contains models configurations.
- `Data/`: Contains the dataset corresponding annotations in different formats:
    - `CSVs/`: Contains the dataset corresponding annotations in CSV format.
    - `JSONs/`: Contains the dataset corresponding annotations in JSONs format.
    - `TXTs/`: Contains the dataset corresponding annotations in TXT format.
    - `YAMLs/`: Contains the dataset corresponding annotations in YAMLs format.
- `Dataset/`: Contains the dataset:
    - `images/`: Contains the dataset images.
    - `labels/`: Contains the dataset labels (class + bounding box). It replicates images structure but replaces images for a TXT file with the corresponding annotations for the corresponding image.
    - `multispecies.jpeg`: Multispecies image that it is not in any of the Dataset, for experimental purposes.
    - `test.txt`: Test Dataset TXT file.
    - `train.txt`: Train Dataset TXT file.
    - `validation.txt`: Validation Dataset TXT file.
    - `val_unique_locations.txt`: Validation Dataset TXT file but only with the images that are in unique locations among the entire Dataset.
- `runs/detect`: Contains the prediction and validation folders generated by [YOLOv8](https://github.com/ultralytics/ultralytics)
- `Scripts/`: Includes scripts for data preprocessing, bounding box generation, different files format generation, images visualization with Bounding Boxes, Data Split, Dataset distribution visualization...

## Model Information

Using [Yolov8](https://github.com/ultralytics/ultralytics) trained on custom data for detection and classification.

At the moment this is the best model I have been able to create:
- [Model Folder](https://github.com/GrunCrow/cv4ecology/tree/main/AI_Census/Trainings/YOLOv8/1_exp_batch_128)
- [Configuration](https://github.com/GrunCrow/cv4ecology/blob/main/AI_Census/Trainings/YOLOv8/1_exp_batch_128/args.yaml)
- [Results]()

#### Cool stuff related to this workshop

It seems that I have done something cool and that it has been the result and thanks to this workshop, so I am sharing it here

- Contributed a [bug fix](https://github.com/ultralytics/ultralytics/pull/4468) to YOLOv8 that was merged during the workshop