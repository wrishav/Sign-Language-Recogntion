import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import ctypes
import sys
import cv2
from tkinter import *
from tkinter.tix import *
from time import sleep
from PIL import ImageTk, Image
from detect import detect_frame
import tkinter.messagebox as tkMessageBox
from tensorflow.keras.models import load_model


model = load_model('sequencial_model.h5')
print(model.summary())
print("Model Loaded...")
classes = os.listdir('dataset/train')

def HomePage():
	global cntct,about, predict_stream, cap
	try:
		cntct.destroy()
	except:
		pass
	try:
		about.destroy()
	except:
		pass
	try:
		predict_stream.destroy()
	except:
		pass
	try:
		cap.release()
	except:
		pass
	window = Tk()
	img = Image.open("Images\\HomePage.png")
	img = ImageTk.PhotoImage(img)
	panel = Label(window, image=img)
	panel.pack(side="top", fill="both", expand="yes")

	user32 = ctypes.windll.user32
	user32.SetProcessDPIAware()
	[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
	lt = [w, h]
	a = str(lt[0]//2-446)
	b= str(lt[1]//2-383)

	window.title("HOME - American Sign Language")
	window.geometry("1214x680+"+a+"+"+b)
	window.resizable(0,0)

	def contactus():
		global cntct,about, predict_stream, cap
		try:
			window.destroy()
		except:
			pass
		try:
			about.destroy()
		except:
			pass
		try:
			predict_stream.destroy()
		except:
			pass
		try:
			cap.release()
		except:
			pass
		cntct = Tk()
		img = Image.open("Images\\AboutTeam.png")
		img = ImageTk.PhotoImage(img)
		panel = Label(cntct, image=img)
		panel.pack(side="top", fill="both", expand="yes")

		user32 = ctypes.windll.user32
		user32.SetProcessDPIAware()
		[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
		lt = [w, h]
		a = str(lt[0]//2-446)
		b= str(lt[1]//2-383)

		cntct.title("About Team - American Sign Language")
		cntct.geometry("1214x680+"+a+"+"+b)
		cntct.resizable(0,0)

		homebtn = Button(cntct,text = "HomePage",font = ("Agency FB",16,"bold"),width=10, relief = FLAT, bd = 0, borderwidth='0',bg="#787A91",fg="#0F044C",activebackground = "#EEEEEE",activeforeground = "#141E61",command=HomePage)	
		homebtn.place(x=784, y = 40)
		contactusbtn = Button(cntct,text = "About Project",font = ("Agency FB",16,"bold"), width=12, relief = FLAT, bd = 0, borderwidth='0',bg="#787A91",fg="#0F044C",activebackground = "#EEEEEE",activeforeground = "#141E61",command=aboutus)
		contactusbtn.place(x=909,y = 40)
		exitbtn = Button(cntct,text = "Exit",font = ("Agency FB",16,"bold"), width=10, relief = FLAT, bd = 0, borderwidth='0',bg="#787A91",fg="#0F044C",activebackground = "#EEEEEE",activeforeground = "#141E61",command=exit)
		exitbtn.place(x=1050,y = 40)

		cntct.mainloop()

	def aboutus():
		global about,cntct, predict_stream, cap
		try:
			window.destroy()
		except:
			pass
		try:
			cntct.destroy()
		except:
			pass
		try:
			predict_stream.destroy()
		except:
			pass
		try:
			cap.release()
		except:
			pass
		about = Tk()
		img = Image.open("Images\\AboutUs.png")
		img = ImageTk.PhotoImage(img)
		panel = Label(about, image=img)
		panel.pack(side="top", fill="both", expand="yes")

		user32 = ctypes.windll.user32
		user32.SetProcessDPIAware()
		[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
		lt = [w, h]
		a = str(lt[0]//2-446)
		b= str(lt[1]//2-383)

		about.title("About Project - American Sign Language")
		about.geometry("1214x680+"+a+"+"+b)
		about.resizable(0,0)

		homebtn = Button(about,text = "HomePage",font = ("Agency FB",16,"bold"), width=10, relief = FLAT, bd = 0, borderwidth='0',bg="#787A91",fg="#0F044C",activebackground = "#EEEEEE",activeforeground = "#141E61",command=HomePage)	
		homebtn.place(x=800, y = 40)
		contactusbtn = Button(about,text = "About Us",font = ("Agency FB",16,"bold"), width=10, relief = FLAT, bd = 0, borderwidth='0',bg="#787A91",fg="#0F044C",activebackground = "#EEEEEE",activeforeground = "#141E61",command=contactus)
		contactusbtn.place(x=925,y = 40)
		exitbtn = Button(about,text = "Exit",font = ("Agency FB",16,"bold"), width=10, relief = FLAT, bd = 0, borderwidth='0',bg="#787A91",fg="#0F044C",activebackground = "#EEEEEE",activeforeground = "#141E61",command=exit)
		exitbtn.place(x=1050,y = 40)

		about.mainloop()

	# EXIT . . . 
	def exit():
		global cntct,about, predict_stream
		result = tkMessageBox.askquestion("American Sign Language", "Are you sure you want to exit?", icon= "warning")
		if result == 'yes':
			sys.exit()

	def StreamMode():
		pass

	def VideoMode():
		global about,cntct, predict_stream
		try:
			window.destroy()
		except:
			pass
		try:
			cntct.destroy()
		except:
			pass

		predict_stream = Tk()
		img = Image.open("Images\\Loading.png")
		img = ImageTk.PhotoImage(img)
		panel = Label(predict_stream, image=img)
		panel.pack(side="top", fill="both", expand="yes")

		user32 = ctypes.windll.user32
		user32.SetProcessDPIAware()
		[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
		lt = [w, h]
		a = str(lt[0]//2-446)
		b= str(lt[1]//2-383)

		imageFrame = Frame(predict_stream, width=600, height=500)
		imageFrame.place(x=300, y=100)

		global cap
		cap = cv2.VideoCapture(0)
		
		def show_frame():
			_, frame = cap.read()
			global current_character
			frame, current_character = detect_frame(frame, model, classes)
			cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
			img = Image.fromarray(cv2image)
			imgtk = ImageTk.PhotoImage(image=img)
			display1.imgtk = imgtk
			display1.configure(image=imgtk)
			window.after(10, show_frame) 

		display1 = Label(imageFrame)
		display1.grid(row=1, column=0)

		
		show_frame()

		##########################

		def add_into_string():
			try:
				global current_character
				if current_character == "Space":
					current_character = " "
				value = predicted_string_label['text'] + current_character
				predicted_string_label.config(text = value)
			except:
				pass
		def remove_from_string():
			value = predicted_string_label['text'][:-1]
			predicted_string_label.config(text = value)

		predict_stream.title("Predict - American Sign Language")
		predict_stream.geometry("1214x680+"+a+"+"+b)
		predict_stream.resizable(0,0)

		homebtn = Button(predict_stream,text = "HomePage",font = ("Agency FB",16,"bold"), width=10, relief = FLAT, bd = 0, borderwidth='0',bg="#787A91",fg="#0F044C",activebackground = "#EEEEEE",activeforeground = "#141E61",command=HomePage)	
		homebtn.place(x=800, y = 40)
		contactusbtn = Button(predict_stream,text = "About Us",font = ("Agency FB",16,"bold"), width=10, relief = FLAT, bd = 0, borderwidth='0',bg="#787A91",fg="#0F044C",activebackground = "#EEEEEE",activeforeground = "#141E61",command=contactus)
		contactusbtn.place(x=925,y = 40)
		exitbtn = Button(predict_stream,text = "Exit",font = ("Agency FB",16,"bold"), width=10, relief = FLAT, bd = 0, borderwidth='0',bg="#787A91",fg="#0F044C",activebackground = "#EEEEEE",activeforeground = "#141E61",command=exit)
		exitbtn.place(x=1050,y = 40)


		Label(predict_stream, text="Predicted String: ", font = ("Agency FB",16,"bold")).place(x=300, y=600)
		predicted_string_label = Label(predict_stream, text="", font = ("Agency FB",16,"bold"))
		predicted_string_label.place(x=407, y = 600)

		add_string = Button(predict_stream, text = "ADD", font = ("Agency FB",16,"bold"), width=12, relief = FLAT, bd = 0, borderwidth='0',bg="#787A91",fg="#0F044C",activebackground = "#EEEEEE",activeforeground = "#141E61",command=add_into_string)	
		add_string.place(x=600, y = 600)
		remove_string = Button(predict_stream, text = "REMOVE",font = ("Agency FB",16,"bold"), width=10, relief = FLAT, bd = 0, borderwidth='0',bg="#787A91",fg="#0F044C",activebackground = "#EEEEEE",activeforeground = "#141E61",command=remove_from_string)
		remove_string.place(x=850,y = 600)


		predict_stream.mainloop()


	''' MENU BAR '''             
	aboutusbtn = Button(window,text = "About Project",font = ("Agency FB",16,"bold"), width=12, relief = FLAT, bd = 0, borderwidth='0',bg="#787A91",fg="#0F044C",activebackground = "#EEEEEE",activeforeground = "#141E61",command=aboutus)	
	aboutusbtn.place(x=784, y = 40)
	contactusbtn = Button(window,text = "About Us",font = ("Agency FB",16,"bold"), width=10, relief = FLAT, bd = 0, borderwidth='0',bg="#787A91",fg="#0F044C",activebackground = "#EEEEEE",activeforeground = "#141E61",command=contactus)
	contactusbtn.place(x=925,y = 40)
	exitbtn = Button(window,text = "Exit",font = ("Agency FB",16,"bold"), width=10, relief = FLAT, bd = 0, borderwidth='0',bg="#787A91",fg="#0F044C",activebackground = "#EEEEEE",activeforeground = "#141E61",command=exit)
	exitbtn.place(x=1050,y = 40)

	livestream = Button(window,text = "LIVE STREAM",font = ("Arial Narrow",18,"bold"),width = 20,relief = FLAT, bd = 1, borderwidth='1',bg="#787A91",fg="#0F044C",activebackground = "#EEEEEE",activeforeground = "#141E61",command=VideoMode)
	livestream.place(x=225,y = 350)

	window.mainloop()

#HomePage()
def LoadingScreen():
	root = Tk()
	root.config(bg="white")
	root.title("Loading - American Sign Language")

	img = Image.open(r"Images\\Loading.png")
	img = ImageTk.PhotoImage(img)
	panel = Label(root, image=img)
	panel.pack(side="top", fill="both", expand="yes")

	user32 = ctypes.windll.user32
	user32.SetProcessDPIAware()
	[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
	lt = [w, h]
	a = str(lt[0]//2-446)
	b= str(lt[1]//2-383)

	root.geometry("1214x680+"+a+"+"+b)
	root.resizable(0,0)

	for i in range(40):
		Label(root, bg="#EEEEEE",width=2,height=1).place(x=(i+4)*25,y=600) 

	def play_animation(): 
		for j in range(40):
			Label(root, bg= "#141E61",width=2,height=1).place(x=(j+4)*25,y=600) 
			sleep(0.07)
			root.update_idletasks()
		else:
			root.destroy()
			HomePage()

	root.update()
	play_animation()
	root.mainloop()
	
LoadingScreen()