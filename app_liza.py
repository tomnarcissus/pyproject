import tkinter as tk
import math

# Функция для вычисления значения в соответствии с условиями
def calculate_value():
    x = float(entry.get())
    if x >= 0:
        result = math.pow(x, 1/3)  # y = кубический корень из x при x >= 0
    else:
        result = math.log(abs(x))  # y = натуральный логарифм модуля x при x < 0
    result_label.config(text=f"Результат: {result}")

# Создание окна
window = tk.Tk()
window.title("Вычисление значения")
window.geometry("500x200")

# Создание метки и поля ввода
label = tk.Label(window, text="Введите значение x:")
label.pack()
entry = tk.Entry(window)
entry.pack()

# Создание кнопки для вычисления
button = tk.Button(window, text="Вычислить", command=calculate_value)
button.pack()

# Создание метки для вывода результата
result_label = tk.Label(window, text="Результат:")
result_label.pack()

# Запуск основного цикла обработки событий
window.mainloop()
