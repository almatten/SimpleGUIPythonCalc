# برنامج واجهة بلغة الـ Python
# الة حاسبة باستعمال Tkinter

from tkinter import *

# متغر لتسلسل المدخلات
expression = ""

# دالة للتحديث في مكان الادخال
def press(num):
	# نشير إلى المتغير العام
	global expression

	# تسلسل المدخلات (Concatenation)
	expression = expression + str(num)

	# تحديث التعبير باستعمال set
	equation.set(expression)

# وظيفة لتقييم النتيجة النهائية
def equalpress():
	# exception لا ننسى وضع الـ 
    # لاحتواء الاخطاء مثل القسمة على صفر
	try:
		global expression

		# تقوم بتقييم التعبير eval
		# تقوم بتحويل التعبير الى تسلسل احرف str و
		total = str(eval(expression))

		equation.set(total)

		# تهيئة متغير التعبير بسلسلة فارغة
		expression = ""

	# اذا حدث خطأ ما, سوف يتعمال معه هنا
	except:

		equation.set(" خطأ ")
		expression = ""

# مسح شاشة الادخال
def clear():
	global expression
	expression = ""
	equation.set("")

# الدالة العامة (main)
if __name__ == "__main__":
	# انشاء النافذة
	gui = Tk()

	# ضبط لون الخلفية
	gui.configure(background="#131417")

	# ضبط عنوان الواجهة الرسومية
	gui.title("اَلة حاسبة")

	# ضبط حجم الواجهة الرسومية
	gui.geometry("270x150")

	# StringVar() ننشئ كائن من الـكلاس 
	equation = StringVar()

	# ننشئ نافذة الادخال, لادخال المدخلات
	expression_field = Entry(gui, textvariable=equation)

	# تمكننا من وضع العناصر مثل الجدول grid
	expression_field.grid(columnspan=4, ipadx=70)

	# انشاء زر و وضعة في النافذة
	# عند الضغط على الزر, يتم تنفيذ الدالة او الكود المعين معها
	button1 = Button(gui, text=' 1 ', fg='white', bg='#131417',
					command=lambda: press(1), height=1, width=7)
	button1.grid(row=2, column=0)

	button2 = Button(gui, text=' 2 ', fg='white', bg='#131417',
					command=lambda: press(2), height=1, width=7)
	button2.grid(row=2, column=1)

	button3 = Button(gui, text=' 3 ', fg='white', bg='#131417',
					command=lambda: press(3), height=1, width=7)
	button3.grid(row=2, column=2)

	button4 = Button(gui, text=' 4 ', fg='white', bg='#131417',
					command=lambda: press(4), height=1, width=7)
	button4.grid(row=3, column=0)

	button5 = Button(gui, text=' 5 ', fg='white', bg='#131417',
					command=lambda: press(5), height=1, width=7)
	button5.grid(row=3, column=1)

	button6 = Button(gui, text=' 6 ', fg='white', bg='#131417',
					command=lambda: press(6), height=1, width=7)
	button6.grid(row=3, column=2)

	button7 = Button(gui, text=' 7 ', fg='white', bg='#131417',
					command=lambda: press(7), height=1, width=7)
	button7.grid(row=4, column=0)

	button8 = Button(gui, text=' 8 ', fg='white', bg='#131417',
					command=lambda: press(8), height=1, width=7)
	button8.grid(row=4, column=1)

	button9 = Button(gui, text=' 9 ', fg='white', bg='#131417',
					command=lambda: press(9), height=1, width=7)
	button9.grid(row=4, column=2)

	button0 = Button(gui, text=' 0 ', fg='white', bg='#131417',
					command=lambda: press(0), height=1, width=7)
	button0.grid(row=5, column=0)

	plus = Button(gui, text=' + ', fg='white', bg='#131417',
				command=lambda: press("+"), height=1, width=7)
	plus.grid(row=2, column=3)

	minus = Button(gui, text=' - ', fg='white', bg='#131417',
				command=lambda: press("-"), height=1, width=7)
	minus.grid(row=3, column=3)

	multiply = Button(gui, text=' * ', fg='white', bg='#131417',
					command=lambda: press("*"), height=1, width=7)
	multiply.grid(row=4, column=3)

	divide = Button(gui, text=' / ', fg='white', bg='#131417',
					command=lambda: press("/"), height=1, width=7)
	divide.grid(row=5, column=3)

	equal = Button(gui, text=' = ', fg='white', bg='#131417',
				command=equalpress, height=1, width=7)
	equal.grid(row=5, column=2)

	clear = Button(gui, text='مسح', fg='white', bg='#131417',
				command=clear, height=1, width=7)
	clear.grid(row=5, column='1')

	Decimal= Button(gui, text='.', fg='white', bg='#131417',
					command=lambda: press('.'), height=1, width=7)
	Decimal.grid(row=6, column=0)
	# بدأ برنامج الواجهة الرسومية
	gui.mainloop()
