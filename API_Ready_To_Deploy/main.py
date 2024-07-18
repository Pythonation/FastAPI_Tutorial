from fastapi import FastAPI, Query
from pydantic import BaseModel

# إعداد CORS للسماح بطلبات من متصفح الويب
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # يجب تحديد المجالات المسموح بها في الإنتاج
    allow_methods=["*"],
    allow_headers=["*"],

)

class BMIOutput(BaseModel):
    bmi: float
    message: str
    image: str

@app.get("/")
def Hi():
    return {"message": "Marhaba python"}

@app.get("/calculate_bmi")
def calculate_bmi(
    weight: float = Query(..., gt=20, lt=200, description="الوزن بالكيلوغرام"),
    height: float = Query(..., gt=1, lt=3, description="الطول بالمتر")
):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        message = "لديك نقص في الوزن، كُل أكثر"
        pic = "1"
    elif 18.5 <= bmi < 25:
        message = "لديك وزن طبيعي، حافظ عليه"
        pic = "2"
    elif 25 <= bmi < 30:
        message = "لديك زيادة في الوزن، تمرن أكثر"
        pic = "3"
    else:
        message = "أنت تعاني من السمنة، قم بمراجعة طبيب"
        pic="4"

    return BMIOutput(bmi=bmi, message=message,image=pic)
