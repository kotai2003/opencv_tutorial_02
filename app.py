import streamlit as st
import cv2


def main():
    st.title("Webcam Live Stream")
    run = st.checkbox('Run')
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)

    while run:
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)
    else:
        st.write('Stopped')

if __name__ == '__main__':
    main()