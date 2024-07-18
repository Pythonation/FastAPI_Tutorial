
def calculate_bmi():
    weight = float(input("أدخل وزنك بالكيلوجرام: "))
    height = float(input("أدخل طولك بالمتر: "))
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        message = "لديك نقص في الوزن، كُل أكثر"
    elif 18.5 <= bmi < 25:
        message = "لديك وزن طبيعي، حافظ عليه"
    elif 25 <= bmi < 30:
        message = "لديك زيادة في الوزن، تمرن أكثر"
    else:
        message = "أنت تعاني من السمنة، قم بمراجعة طبيب"

    print ("Your BMI: ",bmi)
    print(message)

calculate_bmi()