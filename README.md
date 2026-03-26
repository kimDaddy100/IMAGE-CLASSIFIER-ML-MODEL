# AI Image Classifier Web App

A lightweight Streamlit web app that uses TensorFlow's pre-trained MobileNetV2 model to classify user-uploaded images with ImageNet labels. This repository includes model loading, preprocessing, and UI integration for quick experimentation and demonstrations.

## ✅ Features

- Upload and display images in-browser
- MobileNetV2 model from `tensorflow.keras.applications` with `imagenet` weights
- Image preprocessing (resize, normalization, batch dimension)
- Top-3 prediction labels with confidence scores
- `@st.cache_resource` for model load performance

## 📦 Requirements

- Python 3.13+
- Streamlit
- TensorFlow
- OpenCV-Python
- Pillow
- NumPy

Optional (recommended in venv):

- `ipykernel` (if using notebooks)
- `pip-tools` / `poetry` for dependency management

## ⚙️ Installation

1. Clone repository:

```bash
git clone "https://your.git.repo/url.git"
cd "AI MODELS"
```

2. Create venv and install dependencies:

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install --upgrade pip
pip install streamlit tensorflow opencv-python pillow numpy
```

3. (Optional) If using `pyproject.toml`, add dependencies there and run your preferred installer.

## ▶️ Run

```bash
streamlit run main.py
```

Then open the local URL shown (`http://localhost:8501` by default).

## 🧠 How it works

- `main.py` loads MobileNetV2 weights with `load_model()`.
- `preprocess_image()` resizes input to `(224, 224)`, applies `preprocess_input`, and expands dims to `(1, 224, 224, 3)`.
- `classify_image()` runs `model.predict` and decodes top-3 predictions with `decode_predictions`.
- Streamlit UI uploads image, displays it, and shows prediction text on button click.

## 🗂️ Project structure

- `main.py` – app entrypoint and classification logic
- `pyproject.toml` – project metadata
- `README.md` – this documentation

## 🛠️ Customization

- Swap `MobileNetV2` for another Keras application (e.g. `ResNet50`) in `load_model()`.
- Add additional output options (e.g. JSON response for API mode).
- Add image upload validation and error handling for unsupported formats.

## 🧪 Testing

No dedicated tests in repo, but you can validate by running app and checking predictions for sample images.

## 🤝 Contribution

- Fork -> feature branch -> PR
- Document changes
- Keep style consistent

## 📜 License

Use your preferred license, e.g. MIT.
