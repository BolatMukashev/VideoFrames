import cv2
from pathlib import Path

class VideoFrameExtractor:
    def __init__(self, video_path, saving_frames_per_second=2):
        self.video_path = Path(video_path)
        self.save_dir = self.video_path.parent / self.video_path.stem
        self.saving_frames_per_second = saving_frames_per_second
    
    def extract_frames(self):
        save_dir = self.create_save_directory()
        video = self.open_video()

        if not video.isOpened():
            print("[!] Can't open video:")
            exit(-1)

        fps = video.get(cv2.CAP_PROP_FPS)
        frame_counts = video.get(cv2.CAP_PROP_FRAME_COUNT)
        frame_save_count = int(fps / self.saving_frames_per_second)

        for x in range(int(frame_counts) + 1):
            success, frame = video.read()
            if x % frame_save_count == 0:
                save_path = save_dir / f'frame{x}.jpg'
                cv2.imwrite(str(save_path), frame)

        video.release()

    def create_save_directory(self):
        save_dir = self.save_dir
        save_dir.mkdir(parents=True, exist_ok=True)
        return save_dir

    def open_video(self):
        video = cv2.VideoCapture(str(self.video_path))
        return video


# Usage:
video_path = 'C:\\Users\\bolat\\Desktop\\Client\\IMG_0053.MOV'
frame_extractor = VideoFrameExtractor(video_path)
frame_extractor.extract_frames()
