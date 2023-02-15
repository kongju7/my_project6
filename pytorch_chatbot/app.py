from tkinter import *
from chat import get_response, bot_name 
from speech import recognize_speech

# 색깔 및 폰트 설정 
BG_GRAY = "#ABB2B9"  
BG_COLOR = "#293740"
TEXT_COLOR = "#EAECEE"
MSG_COLOR = "#547475"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class ChatApplication: 

    def __init__(self): 
        self.window = Tk()
        self._setup_main_window()

    def run(self): 
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Kong's Chatbot")
        self.window.resizable(width = False, height = False)
        self.window.configure(width = 470, height = 550, bg = BG_COLOR)

        # 헤드 라벨 
        head_label = Label(self.window, bg = BG_COLOR, fg = TEXT_COLOR, text = "안녕하세요!", 
                            font = FONT_BOLD, pady = 10)
        head_label.place(relwidth = 1)

        # 구분자
        line = Label(self.window, width = 450, bg = BG_GRAY)
        line.place(relwidth = 1, rely = 0.07, relheight = 0.12)

        # 텍스트 위젯 
        self.text_widget = Text(self.window, width = 20, height = 2, bg = BG_COLOR, 
                                fg = TEXT_COLOR, font = FONT, padx = 5, pady = 5)
        self.text_widget.place(relheight = 0.745, relwidth = 1, rely = 0.08)
        self.text_widget.configure(cursor = "arrow", state = DISABLED)

        # 스크롤바
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight = 1, relx = 0.974)
        scrollbar.configure(command = self.text_widget.yview)

        # 바닥 라벨 
        bottom_label = Label(self.window, bg = BG_GRAY, height = 80)
        bottom_label.place(relwidth = 1, rely = 0.825)

        # 메세지 입력 상자 
        self.msg_entry = Entry(bottom_label, bg = MSG_COLOR, fg = TEXT_COLOR, font = FONT)
        self.msg_entry.place(relwidth = 0.74, relheight = 0.06, rely = 0.008, relx = 0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # 음성 인식 버튼 
        speech_button = Button(bottom_label, text = "음성", font = FONT_BOLD, width = 20, 
                            bg = BG_GRAY, command = lambda: self._on_speech_pressed(None))
        speech_button.place(relx = 0.55, rely = 0.008, relheight = 0.06, relwidth = 0.22)
        
        # 문자 전송 버튼
        send_button = Button(bottom_label, text = "전송", font = FONT_BOLD, width = 20, 
                            bg = BG_GRAY, command = lambda: self._on_enter_pressed(None))
        send_button.place(relx = 0.77, rely = 0.008, relheight = 0.06, relwidth = 0.22)


    def _on_speech_pressed(self, event): 
        msg = recognize_speech()
        self._insert_message(msg, "나")

    def _on_enter_pressed(self, event): 
        msg = self.msg_entry.get()
        self._insert_message(msg, "나")

    def _insert_message(self, msg, sender): 
        if not msg: 
            return 

        self.msg_entry.delete(0, END)
        msg1 = f"{sender} : {msg}\n\n"
        self.text_widget.configure(state = NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state = DISABLED)

        # 봇의 응답 설정  
        msg2 = f"{bot_name} : {get_response(msg)}\n\n"
        self.text_widget.configure(state = NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state = DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__": 
    app = ChatApplication()
    app.run()