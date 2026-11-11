
# 🚧 Pothole & Defect Detector

An AI-powered road pothole detection system using YOLOv8. It detects potholes in road images, draws bounding boxes, and estimates severity based on the detected area.

## Features
- Pothole detection using YOLOv8
- Bounding box visualization
- Confidence score display
- Severity estimation: Low, Medium, High, Critical
- Image upload through Streamlit interface

## Technologies Used
- Python
- YOLOv8
- Ultralytics
- Streamlit
- OpenCV
- NumPy

## Model Performance

| Metric | Test Result |
|---|---:|
| Precision | 60.77% |
| Recall | 58.78% |
| mAP@50 | 59.12% |
| mAP@50-95 | 20.67% |

## Severity Estimation

| Area Percentage | Severity |
|---|---|
| 0% | None |
| 0–3% | Low |
| 3–10% | Medium |
| 10–20% | High |
| Above 20% | Critical |

*Severity is estimated using detected bounding-box area, not actual pothole depth or physical road damage.*

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Dataset

Dataset: [Pothole Detection YOLOv8 - Roboflow](https://universe.roboflow.com/gerapothole/pothole-detection-yolov8/dataset/1)

Dataset license: CC BY 4.0. Attribution to the dataset creator is required.

## Author

Theerdamai Konkipudi
