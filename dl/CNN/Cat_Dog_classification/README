# 🐶🐱 Dog vs Cat Classifier (CNN)

A Convolutional Neural Network (CNN) project to classify images of dogs and cats using **TensorFlow** and **Keras**. This project demonstrates the complete workflow from data preprocessing to model training, evaluation, and deployment.

---

## 📋 Overview

This project predicts whether an image contains a **dog** or a **cat**. It uses a CNN architecture with multiple convolutional and pooling layers, followed by flattening and dense layers. The model is trained on labeled images and can classify new images accurately after training.

---

## 🗂 Dataset Details

- Source: Custom collected or Kaggle Dog vs Cat dataset
- Number of images: ~1000 images (500 dogs, 500 cats)
- Folder structure:
- Image preprocessing:
  - Resize all images to **224x244 pixels**
  - Normalize pixel values to `[0,1]`

---

## 🛠 Tech Stack

- **Python 3.x**
- **TensorFlow & Keras** – Model creation and training
- **OpenCV & Pillow** – Image reading and preprocessing
- **NumPy & Pandas** – Data handling
- **Scikit-learn** – Train-test split and label encoding

---

## 🔧 Project Steps

1. **Data Loading**

   - Images loaded from `dataset/cats/` and `dataset/dogs/`
   - Converted into arrays using OpenCV
   - Resized to **224x244 pixels**

2. **Data Preprocessing**

   - Normalize pixel values (`X/255.0`)
   - Encode labels (`cat=0`, `dog=1`)

3. **Train-Test Split**

   - 80% training data
   - 20% testing data

4. **CNN Model Architecture**

   - **Conv2D Layer 1:** 64 filters, (3x3), ReLU, input shape `(224,244,3)`
   - **MaxPooling2D Layer 1:** Pool size `(2,2)`
   - **Conv2D Layer 2:** 32 filters, (3x3), ReLU
   - **MaxPooling2D Layer 2:** Pool size `(2,2)`
   - **Conv2D Layer 3:** 16 filters, (3x3), ReLU
   - **MaxPooling2D Layer 3:** Pool size `(2,2)`
   - **Flatten Layer**
   - **Dense Layer:** 64 neurons, ReLU
   - **Output Layer:** 1 neuron, Sigmoid

5. **Compile Model**

   - Optimizer: Adam
   - Loss: Binary Crossentropy
   - Metrics: Accuracy

6. **Train Model**

   - Epochs: 10
   - Batch size: 32
   - Validate on test set

7. **Save & Deploy Model**
   - Save trained model using `model.save('model.h5')`
   - Load model for inference on new images

---

## 💻 Code Example

```python
# Example CNN model for Dog vs Cat classification
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

model = Sequential([
    Conv2D(64, (3,3), activation='relu', input_shape=(224,244,3)),
    MaxPooling2D(2,2),
    Conv2D(32, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Conv2D(16, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
```

## 🎓 Key Learnings

- Understanding **CNN layers**: convolution, pooling, flatten, dense
- **Image preprocessing** for consistent model input
- **Data normalization** to improve training performance
- **Label encoding** for binary classification
- **Model training and validation** using train-test split
- **Saving and loading Keras models** for future use
- Importance of **batch size and epochs** for model convergence
- Observing **overfitting and underfitting** through validation accuracy
