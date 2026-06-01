# Handwritten Text Recognition Using Transformer-Based OCR

## Project Overview

This project focuses on developing a modern Handwritten Text Recognition (HTR) system using Transformer-based Optical Character Recognition (OCR) techniques. The original repository initially contained an older OCR implementation based on traditional deep learning architectures such as CNNs, BiLSTMs, and CTC decoding. The project was later modernized into a new version called **htr-v2**, which integrates state-of-the-art Transformer OCR models from Hugging Face.

The primary objective of this project is to recognize handwritten text from images using modern Vision Transformer architectures while learning real-world AI engineering workflows such as environment setup, model inference, preprocessing, version control, and deployment preparation.

---

# Evolution of the Project

## Original OCR System

The original version of the repository used a classic OCR pipeline consisting of:

* Convolutional Neural Networks (CNNs)
* Bidirectional LSTMs (BiLSTMs)
* Connectionist Temporal Classification (CTC) Loss
* TensorFlow-based architecture
* IAM Handwriting Dataset preprocessing

This architecture was commonly used in older handwriting recognition systems and worked by extracting visual features from images and decoding sequences into text.

Although effective for its time, the architecture had several limitations:

* Older TensorFlow dependencies
* More complex training pipelines
* Limited scalability
* Inferior performance compared to modern Transformer OCR systems

---

# Modernization to Transformer OCR

To modernize the project, a new version called **htr-v2** was created.

The new system replaces the older OCR architecture with:

* PyTorch
* Hugging Face Transformers
* Microsoft TrOCR Model
* VisionEncoderDecoder architecture

The modern pipeline uses a Transformer-based OCR system trained specifically for handwritten text recognition.

---

# Technologies Used

## Programming Language

* Python 3.11

## Deep Learning Frameworks

* PyTorch
* Hugging Face Transformers

## OCR Model

* Microsoft TrOCR Base Handwritten Model

## Image Processing Libraries

* Pillow (PIL)
* OpenCV
* Matplotlib

## Additional Tools

* Git
* GitHub
* VS Code
* Virtual Environments (venv)

---

# Project Structure

The repository contains both the legacy OCR implementation and the modern Transformer OCR implementation.

```text
Handwritten-Text-Recognition/
│
├── DataLoader.py
├── Model.py
├── SamplePreprocessor.py
├── main.py
│
├── htr-v2/
│   ├── data/
│   ├── outputs/
│   ├── src/
│   │   ├── inference/
│   │   │   └── test_inference.py
│   │   ├── api/
│   │   ├── dataset/
│   │   ├── models/
│   │   ├── training/
│   │   └── utils/
│   ├── sample.png
│   └── venv/
│
└── README.md
```

---

# How the Modern OCR Pipeline Works

The Transformer OCR pipeline follows the following sequence:

```text
Input Image
↓
Image Preprocessing
↓
Vision Transformer Encoder
↓
Transformer Decoder
↓
Generated Text Output
```

Unlike older OCR systems that required character segmentation and CTC decoding, the Transformer-based architecture directly generates text from image features using sequence generation techniques.

---

# Model Used

The project uses:

```python
microsoft/trocr-base-handwritten
```

This model is a pretrained Transformer OCR model designed specifically for handwritten text recognition tasks.

It uses:

* Vision Transformer (ViT) encoder
* Transformer text decoder
* Sequence generation approach

The model was downloaded directly from Hugging Face.

---

# Image Preprocessing

The OCR system performs preprocessing before inference:

* Image loading
* RGB conversion
* Image resizing
* Normalization through processor pipeline

The preprocessing stage is critical because OCR accuracy strongly depends on:

* image quality
* stroke thickness
* whitespace handling
* contrast
* alignment

During experimentation, it was observed that tightly cropped images with clearer handwriting produced significantly better predictions.

---

# OCR Inference Process

The OCR inference script performs the following operations:

1. Load the TrOCR processor
2. Load the VisionEncoderDecoder model
3. Open the input image
4. Resize image for model compatibility
5. Convert image into tensor representation
6. Generate predicted text tokens
7. Decode generated tokens into readable text

Example prediction:

```text
Prediction: hello world .
```

This demonstrated successful handwritten text recognition using the Transformer-based OCR pipeline.

---

# Challenges Faced During Development

Several real-world engineering challenges were encountered during the project:

## Python Compatibility Issues

The original setup used Python 3.13, which caused compatibility problems with several AI libraries. The project was migrated to Python 3.11 for stable package support.

## Virtual Environment Path Issues

After moving the project folder, the virtual environment paths became invalid. The issue was solved by recreating the venv inside the new repository structure.

## Dependency Installation Problems

Some packages produced compatibility warnings and installation conflicts. These were resolved using:

* proper virtual environments
* package upgrades
* dependency isolation

## OCR Accuracy Problems

Initial OCR predictions were poor due to:

* thin handwriting strokes
* large whitespace
* non-natural handwriting styles

Accuracy improved significantly after:

* using clearer handwriting
* resizing images
* tighter cropping

---

# Key Learnings From the Project

This project provided practical experience in:

* Transformer-based OCR systems
* Hugging Face model inference
* PyTorch workflows
* Environment management
* Git and GitHub workflows
* OCR preprocessing techniques
* Real-world debugging
* AI engineering practices

One major realization from the project was that OCR performance heavily depends not only on the model but also on preprocessing and input quality.

---

# Future Improvements

Several future improvements are planned for the project:

## OCR Enhancements

* Better preprocessing pipeline
* Automatic text region cropping
* Thresholding and denoising
* Batch inference

## AI Engineering Improvements

* GPU acceleration
* Confidence score generation
* Model fine-tuning
* Faster inference pipeline

## Deployment Features

* FastAPI backend
* Streamlit frontend
* Web-based OCR application
* REST API support

## Advanced OCR Features

* Paragraph segmentation
* Multi-line recognition
* Text detection before recognition
* Real-time OCR support

---

# Conclusion

This project represents the evolution from a traditional OCR architecture to a modern Transformer-based OCR system. It demonstrates practical AI engineering skills including model integration, preprocessing, inference pipelines, debugging, environment management, and GitHub-based project development.

The project successfully achieved handwritten text recognition using modern Transformer OCR models and established a scalable foundation for future OCR research and deployment-oriented development.
