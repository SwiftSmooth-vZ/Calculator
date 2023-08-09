import tkinter as tk

calculations = ""

def add_calculation(symbol):
    global calculations
    calculations += str(symbol)
    result_box.delete(1.0, "end")
    result_box.insert(1.0, calculations)

def eval_calculations():
    global calculations
    try:
        calculations = str(eval(calculations))
        result_box.delete(1.0, "end")
        result_box.insert(1.0, calculations)
    except:
        clear_field()
        result_box.insert(1.0, "Error")

def clear_field():
    global calculations
    calculations = ""
    result_box.delete(1.0, "end")



calc = tk.Tk()

bg_color = "#241023"
button_color = "#381A36"
hover_over_color = "#462044"
result_color = "#FFF1D0"


calc.title("Calculator")
calc.geometry("300x275")
calc.configure(bg=bg_color)

result_box = tk.Text(calc, font=("Gilroy", 24), bg= bg_color, fg= result_color, insertbackground= result_color, width=16,height=2)
result_box.grid(columnspan=5)

btn1 = tk.Button(calc, text="1", bg=button_color, fg= result_color, font= ("Gilroy", 14), width= 5, command=lambda: add_calculation(1)).grid(row=2, column= 1)

btn2 = tk.Button(calc, text="2", bg=button_color, fg= result_color, font= ("Gilroy", 14), width= 5, command=lambda: add_calculation(2)).grid(row=2, column= 2)

btn3 = tk.Button(calc, text="3", bg=button_color, fg= result_color, font= ("Gilroy", 14), width= 5, command=lambda: add_calculation(3)).grid(row=2, column= 3)

btn4 = tk.Button(calc, text="4", bg=button_color, fg= result_color, font= ("Gilroy", 14), width= 5, command=lambda: add_calculation(4)).grid(row=3, column= 1)

btn5 = tk.Button(calc, text="5", bg=button_color, fg= result_color, font= ("Gilroy", 14), width= 5, command=lambda: add_calculation(5)).grid(row=3, column= 2)

btn6 = tk.Button(calc, text="6", bg=button_color, fg= result_color, font= ("Gilroy", 14), width= 5, command=lambda: add_calculation(6)).grid(row=3, column= 3)

btn7 = tk.Button(calc, text="7", bg=button_color, fg= result_color, font= ("Gilroy", 14), width= 5, command=lambda: add_calculation(7)).grid(row=4, column= 1)

btn8 = tk.Button(calc, text="8", bg=button_color, fg= result_color, font= ("Gilroy", 14), width= 5, command=lambda: add_calculation(8)).grid(row=4, column= 2)

btn9 = tk.Button(calc, text="9", bg=button_color, fg= result_color, font= ("Gilroy", 14), width= 5, command=lambda: add_calculation(9)).grid(row=4, column= 3)

btn0 = tk.Button(calc, text="0", bg=button_color, fg= result_color, font= ("Gilroy", 14), width= 5, command=lambda: add_calculation(0)).grid(row=5, column= 1)

btn_plus = tk.Button(calc, text="+", bg=button_color, fg= result_color, font= ("Gilroy", 14), width= 5, command=lambda: add_calculation("+")).grid(row=2, column= 4)

btn_minus = tk.Button(calc, text="-", bg=button_color, fg= result_color, font= ("Gilroy", 14), width= 5, command=lambda: add_calculation("-")).grid(row=3, column= 4)

btn_div = tk.Button(calc, text="/", bg=button_color, fg= result_color, font= ("Gilroy", 14), width= 5, command=lambda: add_calculation("/")).grid(row=4, column= 4)

btn_mul = tk.Button(calc, text="*", bg=button_color, fg= result_color, font= ("Gilroy", 14), width= 5, command=lambda: add_calculation("*")).grid(row=5, column= 4)

btn_par1 = tk.Button(calc, text="(", bg=button_color, fg= result_color, font= ("Gilroy", 14), width= 5, command=lambda: add_calculation("(")).grid(row=5, column= 2)

btn_par2 = tk.Button(calc, text=")", bg=button_color, fg= result_color, font= ("Gilroy", 14), width= 5, command=lambda: add_calculation(")")).grid(row=5, column= 3)

btn_clear = tk.Button(calc, text="C", bg=button_color, fg= result_color, font= ("Gilroy", 14), width= 11, command= clear_field).grid(row=6, column= 1, columnspan= 2)

btn_equals = tk.Button(calc, text="=", bg=button_color, fg= result_color, font= ("Gilroy", 14), width= 11, command= eval_calculations).grid(row=6, column= 3, columnspan= 2)

calc.mainloop()

