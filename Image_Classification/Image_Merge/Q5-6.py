import cv2

# Open the source video
source_video_path = 'sample.mp4'  # Replace with the path to your source video file
source_cap = cv2.VideoCapture(source_video_path)

# video's width and height
width = int(source_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(source_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# output video path
output_video_path = 'output.avi'  # Replace with the desired output video file path
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = cv2.VideoWriter(output_video_path, fourcc, 60.0, (width // 2, height // 2))

while source_cap.isOpened():
    ret, frame = source_cap.read()  # Read a frame from source video

    if not ret:
        break  # Break the loop when the video ends

    # Flip the frame horizontally
    flipped_frame = cv2.flip(frame, 1)

    # Resize the frame to half width and height
    resized_frame = cv2.resize(flipped_frame, (width // 2, height // 2))

    # Write to the output video
    output_video.write(resized_frame)

    cv2.imshow('Processed Video', resized_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # Press 'q' to exit the loop

# close windows
source_cap.release()
output_video.release()
cv2.destroyAllWindows()
