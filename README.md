# Handwritten Text Recognition using CNN + BiLSTM + CTC

A deep learning based Handwritten Text Recognition (HTR) system built using TensorFlow, OpenCV, CNNs, Bidirectional LSTMs, and CTC Loss.
This project recognizes handwritten words from images without requiring character-level segmentation.

---

# Features

* Handwritten word recognition
* CNN feature extraction
* Bidirectional LSTM sequence modeling
* CTC (Connectionist Temporal Classification) decoding
* Beam Search decoding support
* Word Beam Search support
* IAM Handwriting Dataset support
* Data augmentation
* Validation with Character Error Rate (CER)
* Inference on custom images

---

# Architecture

```text
Input Image
     ↓
Preprocessing
     ↓
CNN Feature Extractor
     ↓
Bidirectional LSTM
     ↓
CTC Layer
     ↓
Decoded Text
```

---

# Tech Stack

* Python
* TensorFlow 1.x
* OpenCV
* NumPy
* Matplotlib
* EditDistance

---

# Project Structure

```text
Handwritten-Text-Recognition/
│
├── src/
│   ├── DataLoader.py
│   ├── SamplePreprocessor.py
│   ├── Model.py
│   ├── main.py
│   └── analyze.py
│
├── data/
│   ├── words/
│   ├── words.txt
│   └── corpus.txt
│
├── model/
│   ├── charList.txt
│   ├── accuracy.txt
│   └── snapshot*
│
├── dump/
│
├── README.md
└── requirements.txt
```

---

# Dataset

This project uses the IAM Handwriting Database.

Dataset Link:
[IAM Handwriting Database](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database?utm_source=chatgpt.com)

---

# How It Works

## 1. Preprocessing

Images are:

* converted to grayscale
* resized to fixed dimensions
* normalized
* transposed for sequence learning

---

## 2. CNN

The CNN extracts visual handwriting features such as:

* edges
* strokes
* curves
* character patterns

---

## 3. BiLSTM

Bidirectional LSTM processes features left-to-right and right-to-left to understand character dependencies in handwriting.

---

## 4. CTC Loss

CTC allows the model to recognize text without needing segmented character labels.

Instead of:

* detecting each character separately

the model learns:

* image → text sequence directly

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/Handwritten-Text-Recognition.git

cd Handwritten-Text-Recognition
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Requirements

```text
tensorflow
opencv-python
numpy
matplotlib
editdistance
```

---

# Training

```bash
python main.py --train
```

The model will:

* train on IAM dataset
* validate after each epoch
* save best model automatically

---

# Validation

```bash
python main.py --validate
```

Outputs:

* Character Error Rate (CER)
* Word Accuracy

---

# Inference

Place test image path in:

```python
fnInfer = '../data/test.png'
```

Then run:

```bash
python main.py
```

Example Output:

```text
Recognized: "hello"
Probability: 0.98
```

---

# Decoding Methods

## Best Path Decoding

Fast greedy decoding.

```bash
python main.py
```

---

## Beam Search Decoding

More accurate sequence decoding.

```bash
python main.py --beamsearch
```

---

## Word Beam Search

Uses dictionary constraints for improved word prediction.

```bash
python main.py --wordbeamsearch
```

---

# Data Augmentation

The project applies:

* random horizontal stretching
* normalization
* resizing

This improves model generalization on different handwriting styles.

---

# Evaluation Metrics

## Character Error Rate (CER)

Measures character-level prediction errors.

```text
CER = edit distance / total characters
```

---

## Word Accuracy

Measures percentage of completely correct words.

---

# Example Pipeline

```text
Handwritten Image
        ↓
Preprocessing
        ↓
CNN
        ↓
BiLSTM
        ↓
CTC Decoder
        ↓
Recognized Text
```

---

# Key Concepts Learned

This project demonstrates:

* Deep Learning
* CNNs
* RNNs
* LSTMs
* CTC Loss
* Sequence Modeling
* OCR Systems
* Image Processing
* TensorFlow
* Beam Search Decoding

---

# Future Improvements

* Transformer-based OCR
* Vision Transformers (ViT)
* TrOCR integration
* Attention mechanisms
* Paragraph recognition
* Real-time handwriting recognition
* Multilingual support

---

# Sample Result

| Input Image            | Predicted Text |
| ---------------------- | -------------- |
| Handwritten word image | `"hello"`      |

---

# Author

Jeff Phil

---

# License

This project is for educational and research purposes.
