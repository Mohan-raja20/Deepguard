import streamlit as st
import tempfile, os
from models.image_detector import detect_image
from models.voice_detector import detect_voice
from models.video_detector import detect_video

st.set_page_config(page_title="DeepGuard AI", page_icon="🛡️", layout="centered")

st.markdown("""
<h1 style='color:#1D9E75;'>🛡️ DeepGuard AI</h1>
<p style='color:#666;'>Detect fake Images, Voice and Videos using AI — by Mohan Raja</p>
<hr/>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🖼️ Image", "🎙️ Voice", "🎥 Video"])

with tab1:
    st.subheader("Image Deepfake Detector")
    file = st.file_uploader("Upload an image", type=["jpg","jpeg","png","webp"])
    if file:
        st.image(file, use_column_width=True)
        if st.button("🔍 Detect Image"):
            with st.spinner("Analyzing image..."):
                with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
                    tmp.write(file.read())
                    tmp_path = tmp.name
                label, conf = detect_image(tmp_path)
            if label == "FAKE":
                st.error(f"❌ FAKE DETECTED — Confidence: {conf}%")
            else:
                st.success(f"✅ REAL — Confidence: {conf}%")
            st.progress(conf / 100)
            st.info(f"🔬 Model: EfficientNet-B0\n\n📊 Confidence: {conf}%\n\n🧠 Result: {label}")

with tab2:
    st.subheader("Voice Deepfake Detector")
    file = st.file_uploader("Upload audio", type=["mp3","wav","ogg"])
    if file:
        st.audio(file)
        if st.button("🔍 Detect Voice"):
            with st.spinner("Extracting MFCC features..."):
                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                    tmp.write(file.read())
                    tmp_path = tmp.name
                label, conf = detect_voice(tmp_path)
            if label == "FAKE":
                st.error(f"❌ FAKE VOICE — Confidence: {conf}%")
            else:
                st.success(f"✅ REAL VOICE — Confidence: {conf}%")
            st.progress(conf / 100)
            st.info(f"🎙️ Model: MFCC + SVM\n\n📊 Confidence: {conf}%\n\n🧠 Result: {label}")

with tab3:
    st.subheader("Video Deepfake Detector")
    file = st.file_uploader("Upload video", type=["mp4","mov","avi"])
    if file:
        st.video(file)
        if st.button("🔍 Detect Video"):
            with st.spinner("Analyzing video frames..."):
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
                    tmp.write(file.read())
                    tmp_path = tmp.name
                label, conf, fake_frames, total = detect_video(tmp_path)
            if label == "FAKE":
                st.error(f"❌ FAKE VIDEO — Confidence: {conf}%")
            else:
                st.success(f"✅ REAL VIDEO — Confidence: {conf}%")
            st.progress(conf / 100)
            st.info(f"🎬 Frames Analyzed: {total}\n\n🔴 Fake Frames: {fake_frames}/{total}\n\n📊 Confidence: {conf}%\n\n🧠 Result: {label}")