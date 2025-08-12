from ultralytics import YOLO
from PIL import Image

tuned_model=YOLO("runs/detect/train3/weights/best.pt")
def predict_img(img):
    result=tuned_model.predict(img)
    result=result[0]
    img=result.plot()
    pil_img=Image.fromarray(img)
    return pil_img
if __name__ =='__main__' :
    predicted_img=predict_img('/Users/ahmedmaher/Desktop/Pathholes_detection/Pothole-Detection-1/train/images/img_1881_jpg.rf.c28563f83b13d34400c272bc33986f60.jpg')
    predicted_img.show()
   