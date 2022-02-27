from tkinter import *


bg_gray = "#ABB2B9"
bg_color = "#17202A"
text_color = "#EAECEE"

Font = "Helvetica 14"
Font_Bold = "Helvetica 13 bold"


class ChatApplication:

   def __init__(self):
      self.window = Tk()
      self._setup_main_window()

   # Run chatbot
   def run(self):
      self.window.mainloop()

   def _setup_main_window(self):
      self.window.title("Pre-Employment Survey")
      self.window.resizable(width=False, height=False)
      self.window.configure(width=700, height=700, bg=bg_color)

      # Title label
      head_label = Label(self.window, bg = bg_color, fg = text_color, text="Pre-Employment Survey", font=Font_Bold, pady=10)
      head_label.place(relwidth=1)

      # Tiny divider
      line = Label(self.window, width =450, bg=bg_gray)
      line.place(relwidth=1, rely= 0.07, relheight= 0.012)

      # Text Widget
      self.text_widget = Text(self.window, width=20, height=2, bg=bg_color, fg= text_color, font=Font, padx=5, pady=5)
      self.text_widget.place(relheight=0.75, relwidth=1, rely=0.08)
      self.text_widget.configure(cursor="arrow", state=DISABLED)

      # Scroll bar
      scrollbar = Scrollbar(self.text_widget)
      scrollbar.place(relheight=1,relx=0.974)
      scrollbar.configure(command=self.text_widget.yview)

      # bottom label
      bottom_label = Label(self.window,bg=bg_gray,height=80)
      bottom_label.place(rely=0.825, relwidth=1)

      # message box
      self.message = Entry(bottom_label, bg="#2C3E50", fg = text_color, font=Font)
      self.message.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
      self.message.focus()
      self.message.bind("<Return>", self._on_enter_pressed)

      # send button
      send_button = Button(bottom_label, text="Send", font=Font_Bold, width=20, bg=bg_gray,
                           command=lambda: self._on_enter_pressed(None))
      send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)


   def _on_enter_pressed(self,event):
      message = self.message.get()
      self._insert_message(message,"User")


   def _insert_message(self, message, sender):
      if not message:
         return

      self.message.delete(0,END)

      msg1 = f'''ELON: Hi, My name is ELON


ELON: Welcome to Connextion Pre-Employment Assessment.  


ELON: Do you have any job experience?'''
      self.text_widget.configure(cursor="arrow", state=NORMAL)
      self.text_widget.insert(END, msg1)
      self.text_widget.configure(state=DISABLED)

      msg2 = f"ELON: What's your experience level?\n\n\n"
      self.text_widget.configure(cursor="arrow", state=NORMAL)
      self.text_widget.insert(END, msg2)
      self.text_widget.configure(state=DISABLED)

      msg3 = f"ELON: Please state the reason\n\n\n"
      self.text_widget.configure(cursor="arrow", state=NORMAL)
      self.text_widget.insert(END, msg3)
      self.text_widget.configure(state=DISABLED)

      msg4 = f"ELON: Please choose your highest education \n          -A) Diploma\n          -B) Undergraduate\n          -C) Master\n          -D) PhD\n\n\n"
      self.text_widget.configure(cursor="arrow", state=NORMAL)
      self.text_widget.insert(END, msg4)
      self.text_widget.configure(state=DISABLED)

      msg5 = f"ELON: Please higlight your major \n          - A) Engineering & Technology Related\n          - B) Business Related\n          - C) Environmental Related\n          - D) Literature, Language & Social Science Related\n\n\n"
      self.text_widget.configure(cursor="arrow", state=NORMAL)
      self.text_widget.insert(END, msg5)
      self.text_widget.configure(state=DISABLED)

      msg6 = f"ELON: Please add you skills\n\n\n"
      self.text_widget.configure(cursor="arrow", state=NORMAL)
      self.text_widget.insert(END, msg6)
      self.text_widget.configure(state=DISABLED)

      msg7 = f"ELON: What languages do you know?\n\n\n"
      self.text_widget.configure(cursor="arrow", state=NORMAL)
      self.text_widget.insert(END, msg7)
      self.text_widget.configure(state=DISABLED)

      msg8 = f"ELON: Please add relevant information about you.\n          - Phone Number\n          - Email\n          - Address\n          - Nationality\n\n\n"
      self.text_widget.configure(cursor="arrow", state=NORMAL)
      self.text_widget.insert(END, msg8)
      self.text_widget.configure(state=DISABLED)

      
      self.text_widget.see((END))


if __name__ == "__main__":
   app = ChatApplication()
   app.run()

