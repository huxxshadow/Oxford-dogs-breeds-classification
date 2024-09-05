
---

# Dog Breed Classification - ConvNeXt Model

This repository contains the implementation of a dog breed classification model based on the ConvNeXt architecture. The model is trained to classify dog images into one of 120 breeds using the [Stanford Dogs Dataset](http://vision.stanford.edu/aditya86/ImageNetDogs/). The project includes data processing, training, validation, and inference with the ability to handle misclassified samples.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
  - [Data Preparation](#data-preparation)
  - [Training the Model](#training-the-model)
  - [Inference and Visualization](#inference-and-visualization)
  - [Generate Predictions for Test Data](#generate-predictions-for-test-data)
- [Results](#results)
- [License](#license)

## Project Overview

The goal of this project is to classify dog breeds from images using a pre-trained ConvNeXt model. The project includes the following key components:

1. **Data Preprocessing**: The dataset is split into training and validation sets, and various data augmentation techniques are applied.
2. **Model Fine-tuning**: Fine-tuning the ConvNeXt model, which has been pre-trained on ImageNet, by replacing the last layer to classify 120 dog breeds.
3. **Training**: The model is trained using PyTorch with techniques such as label smoothing, learning rate scheduling, and mixed precision training.
4. **Inference and Visualization**: Misclassified samples are visualized, and predictions are generated for test images with data augmentation.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/dog-breed-classification.git
   cd dog-breed-classification
   ```

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the dataset**:
   - Download the Stanford Dogs Dataset and place it in the `data/` directory.

## Usage

### Data Preparation

1. **Organize Data**:
   - The images should be organized in the `data/train/` and `data/test/` directories. The `train` directory should contain subdirectories for each breed, with images of the corresponding breed.

2. **Label Encoding**:
   - The labels are encoded using `LabelEncoder` for training. The mapping between labels and breeds is stored in `data/breed.csv`.

## Results

- The model achieved an accuracy of **X.XX** on the validation set.
- The generated predictions for the test data can be found in the `out/` directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
