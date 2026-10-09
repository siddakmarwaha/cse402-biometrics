# CSE 402 — Biometrics & Face Recognition

![Python](https://img.shields.io/badge/python-3.9%2B-blue) ![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange) ![PyTorch](https://img.shields.io/badge/PyTorch-CNN-ee4c2c) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Biometrics coursework centered on face recognition.

**Course:** CSE 402 — Biometrics and Pattern Recognition  
**Term:** Fall 2024  
**Institution:** Michigan State University

## Highlights

- **Final project:** PyTorch CNN that identifies 17 celebrities from face images, evaluated with 5-fold cross-validation — **93.6% average accuracy**, with per-fold confusion matrices.
- FaceNet (`facenet-pytorch`) embedding pipeline with Albumentations augmentation for face verification.
- Image-processing assignments on face, fingerprint and iris images (NumPy, Pillow, scikit-image).

## Contents

- [`final_project/cnn_face_recognition_kfold.ipynb`](final_project/cnn_face_recognition_kfold.ipynb) — final CNN with 5-fold CV
- [`final_project/cnn_face_recognition_draft.ipynb`](final_project/cnn_face_recognition_draft.ipynb) — earlier iteration of the model
- [`labs/facenet_embeddings.ipynb`](labs/facenet_embeddings.ipynb) — FaceNet embedding lab
- [`homework/hw2_q3_image_processing.ipynb`](homework/hw2_q3_image_processing.ipynb) — HW2 Q3
- [`homework/hw3/hw3.ipynb`](homework/hw3/hw3.ipynb) — HW3

## Repository Structure

```text
cse402-biometrics/
├── final_project/
│   ├── cnn_face_recognition_draft.ipynb
│   └── cnn_face_recognition_kfold.ipynb
├── homework/
│   ├── hw3/
│   │   ├── code/
│   │   │   └── pgm.py
│   │   └── hw3.ipynb
│   └── hw2_q3_image_processing.ipynb
├── labs/
│   └── facenet_embeddings.ipynb
├── LICENSE
├── README.md
└── requirements.txt
```

## Tech Stack

Python, PyTorch, torchvision, facenet-pytorch, scikit-learn, scikit-image, Pillow

## Getting Started

```bash
git clone https://github.com/siddakmarwaha/cse402-biometrics.git
cd cse402-biometrics
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

## Data

The Kaggle *Celebrity Faces* image dataset and course biometric images are not committed; place them in `Celebrity Faces Dataset/` and `IMAGES_Biometrics/` respectively.

> **Academic integrity:** This repository contains my own submitted work for a university course and is shared as a portfolio sample. Assignment prompts and starter code belong to the course instructors. Current students should not copy this work.

## Author

**Siddak Marwaha**

## License

Code in this repository is released under the [MIT License](LICENSE). Course-provided prompts and materials remain the property of their authors.
