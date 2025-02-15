# Simpson Classification with SimCLR

This project proposes two approaches for classifying Simpson characters: a **Simple CNN** and a **SimCLR** approach for unsupervised learning followed by classification. The dataset is filtered to include only classes with more than 300 images, resulting in 19 available Simpson characters. The number of images per class is limited to 300, with specific allocations for training (70%), validation (10%), and testing (20%). 

Initially, the Keras part used the whole dataset and achieved an accuracy of 84% on test set. However, to reduce training time, the project experiments SimCLR with fewer images and labels.

## 📂 Image Dataset

The image dataset is available on [Kaggle](https://www.kaggle.com/datasets/alexattia/the-simpsons-characters-dataset). It contains over 20,000 images of 42 Simpson characters. For this project, only classes with more than 300 images are used, resulting in 19 characters. The dataset is further balanced to include **300 images per class**.

## 🛠️ Libraries Used

- **PyTorch**: For building and training neural networks.
- **Numpy / Matplotlib.pyplot**: For data manipulation and visualization.
- **Keras**: Used initially for classification with the whole dataset.


## 🔍 Classification Approaches and Comparison

### 1. **Simple CNN**
A basic CNN model for classifying Simpson characters.
- **Accuracy**: 33.14%
- **Issue**: Overfitting (the model memorizes training data instead of generalizing).
- **Dataset**: Uses 50 labels per class for classification.

### 2. **SimCLR**
An unsupervised learning approach followed by classification.
- **Principle**: SimCLR learns robust image representations by maximizing agreement between augmented views of the same image (positive pairs) while minimizing agreement with other images (negative pairs).
- **Steps**:
  1. **Unsupervised Learning**: Use an encoder to extract image representations.
  2. **Classification**: Use the learned representations to train a linear classifier.
- **Accuracy**: 46.52% (improvement of 13% compared to the basic CNN).
- **Issue**: Requires more time to train.
- **Dataset**: Uses 210 images per class for SimCLR training and 50 labels per class for classification.

## 📚 References

- [Kaggle Dataset](https://www.kaggle.com/datasets/alexattia/the-simpsons-characters-dataset)
- SimCLR: [A Simple Framework for Contrastive Learning of Visual Representations](https://arxiv.org/abs/2002.05709)
