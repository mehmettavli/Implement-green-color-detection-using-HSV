# HSV-Based Green Color Detection (Static Image)

This project demonstrates **green color detection** on a static image using **Python** and **OpenCV** with the **HSV color space**.

The implementation is a fundamental computer vision task and serves as a building block for more advanced applications such as **object detection**, **target tracking**, and **UAV vision systems**.

---

## 📌 Project Overview

In this project:

* A synthetic test image with multiple colored objects is created
* The image is converted from **BGR** to **HSV** color space
* A specific HSV range is defined for the green color
* A binary mask is generated to isolate green objects

---

## 🛠 Technologies Used

* Python
* OpenCV
* NumPy

---

## 📷 Sample Output

### Original Image

The input image containing red, green, and blue circles.

### Green Color Mask

The resulting binary mask where only the green object is detected.

*(Add screenshots to the `screenshots/` folder and link them here if available.)*

---

## 🚀 How to Run

Install required libraries:

```bash
pip install opencv-python numpy
```

Run the script:

```bash
python green_color_detection_static.py
```

---

## 🎯 Use Cases

* Computer vision fundamentals
* Color-based object detection
* Preprocessing step for UAV target detection
* Image segmentation tasks

---

## 📈 Next Steps

Possible improvements:

* Contour detection on the masked region
* Object center calculation
* Extending the approach to real-time webcam input

---

## 📬 Feedback

Feedback and suggestions are welcome.
