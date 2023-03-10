import math
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

app = QApplication([])
loader = QUiLoader()
main_window = loader.load("main.ui")
main_window.show()

def numbers(num):
    main_window.txt_box.setText(main_window.txt_box.text()+ num)

def four_basic_operations(type):
    num = main_window.txt_box.text()
    main_window.txt_box.setText(num + type)

def trigonometry(type):
    main_window.txt_box.setText(type)
    
def neg():
    num = main_window.txt_box.text()
    main_window.txt_box.setText("-" + num)

def dot():
    number = ""
    num = main_window.txt_box.text()
    i = len(num)
    while i > 0 and (num[i-1] != "÷" and num[i-1] != "+" and num[i-1] != "-" and num[i-1] != "×"):
        number = number + num[i-1]
        i -= 1
        number = number[::-1]
    if "." not in number:
        main_window.txt_box.setText(num + ".")

def advanced_operations(op):
    main_window.txt_box.setText(op)

def percent():
    number = ""
    num = main_window.txt_box.text()
    i = len(num)
    while i > 0 and (num[i-1] != "÷" and num[i-1] != "+" and num[i-1] != "-" and num[i-1] != "×"):
        number = number + num[i-1]
        i -= 1
        number = number[::-1]
    if "%" not in number:
        main_window.txt_box.setText(num + "%")

def ac():
    main_window.txt_box.setText("")

def result():
    a = ""
    a2 = ""
    b = ""
    b2 = ""
    c = ""
    c2 = ""
    n = ""
    sum = 0
    res = main_window.txt_box.text()
    while "%" in res:
        index = res.find("%")
        while index > 0 and (res[index-1] != "÷" and res[index-1] != "+" and res[index-1] != "-" and res[index-1] != "×"):
            n = n + res[index - 1]
            index -= 1
        n1 = float(n[::-1])
        res = str(n1/100)
        main_window.txt_box.setText(res)

    if "log" in res:
        num = res[3:]
        res = str(math.log(int(num)))
        main_window.txt_box.setText(res)

    if "sqrt" in res:
        num = float(res[4:])
        if num > 0:
            res = str(math.sqrt(num))
            main_window.txt_box.setText(res)
        else:
            main_window.txt_box.setText("NA")

    if "sin" in res:
        rad = res[3:]
        res = str(math.sin(math.radians(float(rad))))
        main_window.txt_box.setText(res)

    if "cos" in res:
        rad = res[3:]
        res = str(math.cos(math.radians(float(rad))))
        main_window.txt_box.setText(res)

    if "tan" in res:
        rad = float(res[3:])
        if rad % 90 == 0 and (rad/90) % 2 != 0:
            main_window.txt_box.setText("NA") 
        else:
            res = str(math.tan(math.radians(rad)))
            main_window.txt_box.setText(res)

    if "cot" in res:
        rad = float(res[3:])
        if rad % 90 == 0 and (rad/90) % 2 == 0:
            main_window.txt_box.setText("NA")
        else:
            res = str(1/(math.tan(math.radians(rad))))
            main_window.txt_box.setText(res)

    while "÷" in res:
        i = res.find("÷")
        j = i
        k = i
        while i > 0 and (res[i-1] != "÷" and res[i-1] != "+" and res[i-1] != "-" and res[i-1] != "×"):
            a = a + res[i-1]
            i -= 1
        a1 = a[::-1]
        l1 = k - len(a1)

        while j < len(res)-1 and (res[j+1] != "÷" and res[j+1] != "+" and res[j+1] != "-" and res[j+1] != "×"):
            a2 = a2 + res[j+1]
            j += 1
        l2 = k + len(a2) + 1
        print(a2)
        if a2 != "0":
            if l1 == 0:
                if l2 == len(res):
                    res = str(float(a1) / float(a2))
                    main_window.txt_box.setText(res)
                else:
                    res = str(float(float(a1) / float(a2))) + res[l2:]
            elif l2 == len(res):
                res = res[0:l1] + str(float(float(a1) / float(a2)))
            else:
                res = res[0:l1] + str(float(float(a1) / float(a2))) + res[l2:]
        else:
            main_window.txt_box.setText("NA")
        a = ""
        a2 = ""

    while "×" in res:
        i = res.find("×")
        j = i
        k = i
        while i > 0 and (res[i-1] != "×" and res[i-1] != "+" and res[i-1] != "-") :
            b = b + res[i-1]
            i -= 1
        b1 = b[::-1]
        l1 = k - len(b1)

        while j < len(res)-1 and (res[j+1] != "×" and res[j+1] != "+" and res[j+1] != "-"):
            b2 = b2 + res[j+1]
            j += 1
        l2 = k + len(b2) + 1
        
        if l1 == 0:
            if l2 == len(res):
                res = str(float(b1) * float(b2))
                main_window.txt_box.setText(res)
            else:
                res = str(float(float(b1) * float(b2))) + res[l2:]   
        elif l2 == len(res):
            res = res[0:l1] + str(float(float(b1) * float(b2)))
        else:
            res = res[0:l1] + str(float(float(b1) * float(b2))) + res[l2:] 
        
        b = ""
        b2 = ""

    while "-" in res:
        i = res.find("-")
        j = i
        k = i
        while i > 0 and res[i-1] != "+" and res[i-1] != "-":
            c = c + res[i-1]
            i -= 1
        c1 = c[::-1]
        l1 = k - len(c1)

        while j < len(res)-1 and res[j+1] != "+" and res[i-1] != "-":
            c2 = c2 + res[j+1]
            j += 1
        l2 = k + len(c2) + 1

        if l1 == 0:
            if l2 == len(res):
                res = str(float(c1) - float(c2))
                main_window.txt_box.setText(res)
            else:
                res = str(float(float(c1) - float(c2))) + res[l2:]   
        elif l2 == len(res):
            res = res[0:l1] + str(float(float(c1) - float(c2)))
        else:
            res = res[0:l1] + str(float(float(c1) - float(c2))) + res[l2:]
        
        c = ""
        c2 = ""

    if "+" in res:
        d = res.split("+")
        for part in d:
            sum += float(part)
        main_window.txt_box.setText(str(sum))

main_window.btn_sum.clicked.connect(partial(four_basic_operations, "+"))
main_window.btn_sub.clicked.connect(partial(four_basic_operations, "-"))
main_window.btn_mul.clicked.connect(partial(four_basic_operations, "×"))
main_window.btn_div.clicked.connect(partial(four_basic_operations, "÷"))
main_window.btn_sqrt.clicked.connect(partial(advanced_operations, "sqrt"))
main_window.btn_log.clicked.connect(partial(advanced_operations, "log"))
main_window.btn_sin.clicked.connect(partial(trigonometry, "sin"))
main_window.btn_cos.clicked.connect(partial(trigonometry, "cos"))
main_window.btn_tan.clicked.connect(partial(trigonometry, "tan"))
main_window.btn_cot.clicked.connect(partial(trigonometry, "cot"))
main_window.btn_0.clicked.connect(partial(numbers, "0"))
main_window.btn_1.clicked.connect(partial(numbers, "1"))
main_window.btn_2.clicked.connect(partial(numbers, "2"))
main_window.btn_3.clicked.connect(partial(numbers, "3"))
main_window.btn_4.clicked.connect(partial(numbers, "4"))
main_window.btn_5.clicked.connect(partial(numbers, "5"))
main_window.btn_6.clicked.connect(partial(numbers, "6"))
main_window.btn_7.clicked.connect(partial(numbers, "7"))
main_window.btn_8.clicked.connect(partial(numbers, "8"))
main_window.btn_9.clicked.connect(partial(numbers, "9"))
main_window.btn_percent.clicked.connect(percent)
# main_window.btn_neg.clicked.connect(neg)
main_window.btn_dot.clicked.connect(dot)
main_window.btn_ac.clicked.connect(ac)
main_window.btn_equal.clicked.connect(result)

app.exec()