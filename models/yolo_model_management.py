from ultralytics import YOLO
from PIL import Image
import shutil


class YoloResult(object):
    def __init__(self, result):
        self.result = result

    def printInfoBoxes(self):
        for box in self.result.boxes:
            label = self.result.names[box.cls[0].item()]
            cords = [round(x) for x in box.xyxy[0].tolist()]
            prob = box.conf[0].item()
            print("Object type:", label)
            print("Coordinates:", cords)
            print("Probability:", prob)
            print("----")

    def getImage(self):
        return Image.fromarray(self.result.plot()[:, :, ::-1])


class YoloV8ModelManagement(object):
    def __init__(self):
        self.model = YOLO("yolov8m.pt")

    def get_predict_result(self, url):
        result = self.model.predict(url)
        return YoloResult(result[0])

    def train(self, yaml_file=None, epochs=1,imgsz=100):
        self.model.train(data=yaml_file, epochs=epochs,imgsz=imgsz)
