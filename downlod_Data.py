from roboflow import Roboflow
rf = Roboflow(api_key="EKFZ6M3SVzOK7ydunQxF")
project = rf.workspace("ahmed-w1lji").project("pothole-detection-irkz9-qi835")
version = project.version(1)
dataset = version.download("yolov11")
                