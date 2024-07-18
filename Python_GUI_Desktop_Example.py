import tkinter as tk
from tkinter import messagebox
import requests

def calculate_bmi():
    weight = entry_weight.get()
    height = entry_height.get()
    
    if weight and height:
        try:
            response = requests.get(f'http://127.0.0.1:8000/calculate_bmi?weight={weight}&height={height}')
            data = response.json()
            result_text.set(f'BMI: {data["bmi"]:.2f}\nالرسالة: {data["message"]}')
        except Exception as e:
            messagebox.showerror("Error", "حدث خطأ، يرجى المحاولة مرة أخرى.")
    else:
        messagebox.showwarning("Input Error", "يرجى إدخال الوزن والطول.")

# إنشاء النافذة الرئيسية
root = tk.Tk()
root.title("حساب مؤشر كتلة الجسم (BMI)")
root.geometry("400x400")
root.resizable(False, False)

# تعيين الخطوط والألوان
font_large = ("Cairo", 16)
font_medium = ("Cairo", 12)
font_small = ("Cairo", 10)
bg_color = "#f8f9fa"
fg_color = "#343a40"
btn_color = "#007bff"
btn_hover_color = "#0056b3"

# تعيين الألوان الخلفية
root.configure(bg=bg_color)

# إنشاء عناصر الواجهة
label_title = tk.Label(root, text="حساب مؤشر كتلة الجسم (BMI)", font=font_large, bg=bg_color, fg=fg_color)
label_weight = tk.Label(root, text="أدخل وزنك بالكيلوغرام:", font=font_medium, bg=bg_color, fg=fg_color)
entry_weight = tk.Entry(root, font=font_medium)
label_height = tk.Label(root, text="أدخل طولك بالمتر:", font=font_medium, bg=bg_color, fg=fg_color)
entry_height = tk.Entry(root, font=font_medium)
result_text = tk.StringVar()
label_result = tk.Label(root, textvariable=result_text, font=font_medium, bg="#e9ecef", fg=fg_color, wraplength=350, justify="center", padx=10, pady=10)

# وظيفة تغيير لون الزر عند التحويم
def on_enter(e):
    btn_calculate['background'] = btn_hover_color

def on_leave(e):
    btn_calculate['background'] = btn_color

btn_calculate = tk.Button(root, text="احسب BMI", font=font_medium, bg=btn_color, fg="white", command=calculate_bmi)
btn_calculate.bind("<Enter>", on_enter)
btn_calculate.bind("<Leave>", on_leave)

# وضع العناصر في النافذة
label_title.pack(pady=20)
label_weight.pack()
entry_weight.pack(pady=5)
label_height.pack()
entry_height.pack(pady=5)
btn_calculate.pack(pady=20)
label_result.pack(pady=10)

# بدء تشغيل البرنامج
root.mainloop()
