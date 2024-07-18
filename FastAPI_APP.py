from fastapi import FastAPI , Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware,
    allow_origins=["*"],  allow_methods=["*"],allow_headers=["*"],
)
class BMIOutput(BaseModel):
    bmi: float
    message: str

@app.get("/")
def Hi():
    return {"message": "Marhaba python"}

@app.get("/calculate_bmi")
def calculate_bmi(
    weight: float= Query(... , gt=20,lt=200, description="الوزن بالكيلوغرام") ,
    height: float= Query(..., gt=1, lt=3, description="الطول بالمتر")
    ):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        message = "لديك نقص في الوزن، كُل أكثر "
    elif 18.5 <= bmi < 25:
        message = "لديك وزن طبيعي، حافظ عليه."
    elif 25 <= bmi < 30:
        message = "لديك زيادة في الوزن، تمرن أكثر"
    else:
        message = "أنت تعاني من السمنة، قم بمراجعة طبيب"
    return BMIOutput(bmi=bmi,message=message)
    
