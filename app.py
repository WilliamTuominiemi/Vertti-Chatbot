from tkinter import *
from chat import get_response

bot_name = 'VerttiBot'

master = Tk()
master.iconbitmap("images/vertti.ico")
master.title(bot_name)
master.geometry("400x300")  

message = StringVar()

def send():
    user_input = message.get()
    if not user_input.strip(): 
        return
    
    chatbox.config(state=NORMAL)
    chatbox.insert(END, f'You: {user_input}\n', 'you')
    
    response = get_response(user_input)
    chatbox.insert(END, f'{bot_name}: {response}\n', 'bot')
    
    chatbox.config(state=DISABLED)
    chatbox.yview(END) 
    message.set('')

w = Label(master, text='Vertti Chatbot')
w.pack()

chatbox = Text(master, height=10, width=30)
chatbox.pack(fill=BOTH, expand=True) 
chatbox.config(state=DISABLED)  
chatbox.tag_config('bot', foreground='darkblue', font=('Helvetica', 10, 'bold'))
chatbox.tag_config('you', font=('Helvetica', 10, 'bold'))

frame = Frame(master)
frame.pack(side=BOTTOM, fill=X, anchor=S) 

chat = Entry(frame, textvariable=message)
chat.pack(side=LEFT, fill=X, expand=True)

button = Button(frame, text="Send", command=send)
button.pack(side=LEFT)

mainloop()
