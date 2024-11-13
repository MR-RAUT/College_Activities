# Advance Animal Species Detection System

## 🐾 Project Overview
The **Advance Animal Species Detection System** is an advanced deep learning-based image classification model designed to accurately identify various animal species. Built using the VGG16 architecture and transfer learning, this system offers reliable, efficient, and scalable solutions for image classification tasks, making it valuable for conservationists, wildlife enthusiasts, and researchers in zoology.

## 🎯 Objective
This project was created to:
- **Classify animal species** from a set of predefined categories with high accuracy.
- **Optimize training efficiency** by leveraging pre-trained VGG16 bottleneck features.
- **Provide interpretative insights** through detailed evaluation metrics and visualizations.

## 📂 Project Structure

- **`data/`**: Contains the image datasets for training, validation, and testing organized in folders by species.
- **`experiments/`**: Includes scripts for experimentation, tuning, and testing alternative model architectures.
- **`images/`**: Stores sample images used for demonstrations and tests.
- **`final project.ipynb`**: The main Jupyter notebook, documenting the complete workflow from data loading to model evaluation.
- **`split_data.ipynb`**: A helper notebook that allows users to split datasets into training, validation, and test sets.
- **`bottleneck_fc_model.h5`**: Saved weights for the final fully connected layers used in classification.
- **`bottleneck_features_test.npy`**: Precomputed bottleneck features for the test dataset.
- **`bottleneck_features_train.npy`**: Precomputed bottleneck features for the training dataset.
- **`bottleneck_features_validation.npy`**: Precomputed bottleneck features for the validation dataset.

## 🛠️ Approach

1. **Data Preprocessing**:
   - Images are resized to 224x224 pixels and normalized for compatibility with VGG16.
   - Bottleneck features are extracted using the VGG16 model (excluding fully connected layers), which reduces the dimensionality and speeds up training.

2. **Model Architecture**:
   - The model is a sequential network consisting of Flatten, Dense, and Dropout layers.
   - Optimized for categorical classification using cross-entropy loss and the RMSprop optimizer.

3. **Training & Evaluation**:
   - The model is trained on precomputed bottleneck features to save on computation time.
   - Evaluation metrics include accuracy, precision, recall, and F1-score, allowing for comprehensive model assessment.
   - Confusion matrices and classification reports are generated for in-depth analysis of performance on each class.

4. **Visualization**:
   - Graphs of training and validation accuracy/loss are plotted to monitor model learning.
   - Confusion matrices are visualized to understand class-wise performance.

## 📊 Model Evaluation

- **Classification Metrics**: Detailed reports including accuracy, precision, recall, and F1-score for each class.
- **Confusion Matrix**: Provides a clear view of true positives, false positives, true negatives, and false negatives for each class.
- **Loss & Accuracy Curves**: Training and validation curves are plotted to track model performance over epochs.

## 🗂 Dataset Structure

The dataset should be organized as follows within the `data/` directory:

```
data/
├── train/
│   ├── butterflies/
│   ├── cats/
│   ├── chickens/
│   ├── cows/
│   ├── dogs/
│   ├── elephants/
│   ├── horses/
│   ├── sheep/
│   ├── spiders/
│   └── squirrels/
├── val/
│   ├── butterflies/
│   ├── cats/
│   ├── chickens/
│   ├── cows/
│   ├── dogs/
│   ├── elephants/
│   ├── horses/
│   ├── sheep/
│   ├── spiders/
│   └── squirrels/
└── test/
    ├── butterflies/
    ├── cats/
    ├── chickens/
    ├── cows/
    ├── dogs/
    ├── elephants/
    ├── horses/
    ├── sheep/
    ├── spiders/
    └── squirrels/
```

Each subfolder represents a different animal class with images in `.jpg` or `.png` format.

## 🚀 Getting Started

### Requirements
Install required dependencies:
```bash
pip install -r requirements.txt
```

### Running the Project
1. Place datasets into the `data/` directory, organized by class as shown above.
2. Open and run `final project.ipynb` to execute the full pipeline, from data preprocessing to model evaluation.
3. Use `split_data.ipynb` to create custom data splits, if necessary.

### Testing on a New Image
To classify a new image, specify the file path in the `test_single_image()` function within `final project.ipynb`:
```python
path = 'path_to_your_image.jpg'
test_single_image(path)
```

## 🤖 Troubleshooting

- **Memory Error**: Large datasets or high-resolution images may cause memory issues. Consider reducing batch size or image resolution.
- **FileNotFoundError**: Ensure all directories (`train`, `val`, and `test`) and class folders exist and contain images.
- **Low Accuracy**: If accuracy is low, consider increasing the number of epochs or trying different optimizers.

## 📈 Results

Detailed classification reports, confusion matrices, and learning curves are available in `final project.ipynb`.
