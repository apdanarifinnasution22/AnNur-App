# 🖼️ AnNur App - Image Processing Application

AnNur App adalah aplikasi desktop berbasis Python untuk **Digital Image Processing (Pengolahan Citra Digital)** menggunakan **OpenCV**, **CustomTkinter**, dan **NumPy**.

Aplikasi ini dibuat sebagai proyek pembelajaran dan tugas mata kuliah pengolahan citra digital dengan fokus pada manipulasi gambar, filtering, morfologi citra, komparasi citra, face detection, histogram, hingga pemrosesan warna.

---

## ✨ Features

### 📷 Camera Processing
- Start Camera
- Stop Camera
- Capture Photo
- Reset Image
- Save Image

### 🎨 Image Filtering
- Grayscale
- Blur
- Edge Detection

### 🌈 Color Processing
- Brightness Adjustment
- Contrast Adjustment
- Color Space Conversion:
  - HSV
  - HSI
  - YCbCr
  - CMYK

### 🧩 Channel Split
- Red Channel
- Green Channel
- Blue Channel

### 😀 Face Detection
- Detect Face
- Auto Crop Face

### ✂️ Crop Processing
- Crop Center

### 🧪 Morphological Operations
- Erosion
- Dilation
- Opening
- Closing

### 📊 Image Comparison
- Before vs After
- Difference Image

### 📈 Histogram Processing
- Histogram Visualization

### 🗜️ Image Compression
- Image Compression Feature

---

## 🛠️ Technologies Used

- Python 3
- OpenCV
- CustomTkinter
- NumPy
- Pillow (PIL)

---

## 📂 Project Structure

```text
AnNur App/
│
├── main.py
│
├── ui/
│   ├── app.py
│   ├── canvas_view.py
│   ├── menubar.py
│   └── sidebar.py
│
├── processing/
│   ├── camera.py
│   ├── channel_split.py
│   ├── color.py
│   ├── color_space.py
│   ├── compare.py
│   ├── compress.py
│   ├── crop.py
│   ├── face.py
│   ├── filter.py
│   ├── histogram.py
│   └── morphology.py
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/USERNAME/annur-app.git
```

### 2. Open Project Folder

```bash
cd annur-app
```

### 3. Install Dependencies

```bash
pip install opencv-python
pip install customtkinter
pip install pillow
pip install numpy
```

Atau:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
python main.py
```

---

## 📖 How To Use

### Using Camera
1. Click **Start Camera**
2. Click **Capture Photo**
3. Apply image processing features
4. Save result image

### Using Image File
1. Open **File → Open Image**
2. Select image
3. Apply filters or image processing
4. Save processed image

---

## 🧠 Digital Image Processing Concepts Implemented

This application implements several concepts in digital image processing:

- Image Filtering
- Edge Detection
- Morphological Image Processing
- Face Detection (Haar Cascade)
- Histogram Analysis
- Image Comparison
- Color Space Transformation
- Channel Splitting
- Brightness & Contrast Adjustment
- Image Compression

---

## 🎓 Project Purpose

This project was developed for:

> **Digital Image Processing Course**

as a practical implementation of image manipulation and computer vision fundamentals using Python.

---

## 👨‍💻 Developer

**Apdan Arifin Nasution**  
Informatics Engineering / Teknik Informatika

---

## 🚀 Future Improvements

Possible future developments:

- Object Detection (YOLO)
- OCR (Text Recognition)
- Face Recognition
- Drag & Crop using Mouse
- Advanced Histogram Analysis
- AI-based Image Enhancement

---

## ⭐ Support

If you find this project useful, feel free to give it a **star ⭐** on GitHub.
