from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
import cv2


def run_tracking(source):

    # Load YOLO model
    model = YOLO("yolov8n.pt")

    # Initialize DeepSORT tracker
    tracker = DeepSort(max_age=30)

    # Open source (video or camera)
    cap = cv2.VideoCapture(source)

    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    if fps == 0:
        fps = 30

    # Create output video
    out = cv2.VideoWriter(
        "outputs/output_video.mp4",
        cv2.VideoWriter_fourcc(*'mp4v'),
        fps,
        (frame_width, frame_height)
    )

    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            print("Video Finished")
            break

        detections = []

        person_count = 0
        car_count = 0

        results = model(frame)

        for result in results:

            boxes = result.boxes

            for box in boxes:

                x1, y1, x2, y2 = box.xyxy[0].tolist()

                confidence = float(box.conf[0])

                class_id = int(box.cls[0])

                class_name = model.names[class_id]

                if class_name == "person":
                    person_count += 1

                if class_name == "car":
                    car_count += 1

                detections.append(
                    (
                        [x1, y1, x2 - x1, y2 - y1],
                        confidence,
                        class_id
                    )
                )

        tracks = tracker.update_tracks(
            detections,
            frame=frame
        )

        for track in tracks:

            if not track.is_confirmed():
                continue

            track_id = track.track_id

            l, t, r, b = track.to_ltrb()

            object_name = "Object"

            try:
                if track.det_class is not None:
                    object_name = model.names[int(track.det_class)]
            except:
                pass

            cv2.rectangle(
                frame,
                (int(l), int(t)),
                (int(r), int(b)),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"{object_name} ID: {track_id}",
                (int(l), int(t) - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

        cv2.putText(
            frame,
            f"Persons: {person_count}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Cars: {car_count}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        out.write(frame)

        cv2.imshow("Object Tracking", frame)

        if cv2.waitKey(25) == 27:
            print("Program Stopped")
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()