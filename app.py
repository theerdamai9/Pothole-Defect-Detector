
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.set_page_config(
    page_title="Pothole & Defect Detector",
    page_icon="🚧",
    layout="wide"
)

@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

st.title("🚧 Pothole & Defect Detector")
st.write("Upload a road image to detect potholes and estimate severity.")

uploaded_file = st.file_uploader(
    "Upload Road Image",
    type=["jpg", "jpeg", "png"]
)

confidence = st.slider(
    "Detection Confidence",
    0.1, 1.0, 0.25, 0.05
)

def calculate_severity(result):
    height, width = result.orig_shape
    total_area = height * width
    pothole_area = 0

    for box in result.boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        pothole_area += (x2 - x1) * (y2 - y1)

    percentage = (pothole_area / total_area) * 100

    if percentage == 0:
        severity = "NONE"
    elif percentage <= 3:
        severity = "LOW"
    elif percentage <= 10:
        severity = "MEDIUM"
    elif percentage <= 20:
        severity = "HIGH"
    else:
        severity = "CRITICAL"

    return percentage, severity

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")

    results = model.predict(
        source=image,
        conf=confidence,
        verbose=False
    )

    result = results[0]
    area, severity = calculate_severity(result)

    annotated = result.plot()
    annotated = annotated[:, :, ::-1]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("Detection Result")
        st.image(annotated, use_container_width=True)

    st.subheader("Detection Report")

    st.metric("Potholes Detected", len(result.boxes))
    st.metric("Pothole Area", f"{area:.2f}%")
    st.metric("Severity Level", severity)

    if len(result.boxes) > 0:
        st.subheader("Confidence Scores")
        for i, box in enumerate(result.boxes):
            st.write(
                f"Pothole {i+1}: {float(box.conf[0]):.2%}"
            )
    else:
        st.success("No potholes detected!")
