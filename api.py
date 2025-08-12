from fastapi import FastAPI ,File ,UploadFile
from fastapi.responses import StreamingResponse
import io
from PIL import Image
from predict import predict_img
app=FastAPI()
@app.post("/predict")
async def predict_img_route(file:UploadFile=File(...)):
    image=Image.open(file.file)
    predicted_img=predict_img(image)
    buffer=io.BytesIO()
    predicted_img.save(buffer,format="PNG")
    buffer.seek(0)
    return StreamingResponse(buffer,media_type="image/png")
