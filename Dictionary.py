import csv
import json
import os
import webbrowser
from tkinter import *
from tkinter import messagebox as mess
import requests
from PIL import ImageTk, Image


class Online_oxford_dist:
    @staticmethod
    # API OF OXFORD
    def meaning_of_word(text='', all_information=False):
        definition_of_word_in_list = []

        app_id = '9454f9bf'
        app_key = 'b9396afdf711ddda4638ef282444af4a'

        language = 'en-gb'
        word_id = text
        # fields = 'pronunciations'
        fields1 = 'definitions'
        # fields2 = 'examples'
        strict_match = 'false'

        url_definition = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + \
                         word_id.lower() + '?fields=' + fields1 + '&strictMatch=' + strict_match

        definition = requests.get(url_definition, headers={'app_id': app_id, 'app_key': app_key})
        # example = requests.get(url_example, headers = {'app_id': app_id, 'app_key': app_key})
        if all_information:
            print("text \n" + definition.text)
        # print("text \n" + definition.text)

        definition = definition.json()
        # example = example.json()

        try:
            total_definition = len(definition['results'][0]['lexicalEntries'])

            for i in range(total_definition):
                definition_of_word_in_list.append(
                    definition['results'][0]['lexicalEntries'][i]['entries'][0]["senses"][0]['definitions'])

            definition_of_word = f'\n\nTotal Meanings: {total_definition} \n\n\n'

            for index, words in enumerate(definition_of_word_in_list):
                definition_of_word = definition_of_word + f'{index + 1}) ' + words[0] + '\n\n'

        except:
            # pass
            definition_of_word = f'\n\n\n\n\n\n\nOops!!!\n\nThere isn\'t any meaning of {text}.'

        return definition_of_word

online_or_offline = None

class DictionaryOnline:

    def __init__(self):
        self.num_of_search = 0
        self.window = Tk()
        self.window.geometry("800x500")
        self.window.configure(bg="#362210")
        self.window.title('Prashant Online Dictionary')

        self.canvas = Canvas(
            self.window,
            bg="#362210",
            height=500,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        img0 = PhotoImage(file=f"Program running image/img0.png")
        self.search_button = Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            background='#38360C',
            activebackground='#38360C',
            relief="flat")

        self.search_button.place(
            x=697, y=98,
            width=87,
            height=40)

        background_img = PhotoImage(file=f"Program running image/background_online.png")
        self.canvas.create_image(
            403.5, 213.0,
            image=background_img)

        entry0_img = PhotoImage(file=f"Program running image/img_textBox0.png")
        self.canvas.create_image(
            537.0, 118.0,
            image=entry0_img)

        self.word_to_search = Entry(
            bd=0,
            bg="#734e05",
            fg='white',
            font='QuicksandLight 15 bold',
            highlightthickness=0)

        self.word_to_search.focus()

        self.word_to_search.place(
            x=415.0, y=99,
            width=244.0,
            height=38)

        entry1_img = PhotoImage(file=f"Program running image/img_textBox1.png")
        self.canvas.create_image(
            592.0, 316.0,
            image=entry1_img)

        self.meaning_displaying_text_box = Text(
            bd=0,
            bg="#140d00",
            foreground='white',
            font='DustismoRoman 10',
            highlightthickness=0)

        self.meaning_displaying_text_box.place(
            x=420.0, y=177,
            width=344.0,
            height=278)

        self.window.resizable(False, False)
        self.window.bind('<Return>', lambda i: self.btn_clicked())
        self.window.bind('<Control-h>', lambda a: self.run_help())
        self.window.bind('<Control-q>', lambda a: exit())
        self.window.protocol('WM_DELETE_WINDOW', lambda : self.close_button_pressed())
        self.window.bind('<Control-Key-1>', lambda a: self.ctrl_1())
        self.window.bind('<Control-Key-2>', lambda a: self.ctrl_2())
        self.window.mainloop()

    def ctrl_1(self):
        self.window.destroy()
        DictionaryOffline()

    def ctrl_2(self):
        self.window.destroy()
        DictionaryOnline()

    def close_button_pressed(self):
        self.window.destroy()
        AskingAboutProgramExecution()

    def run_help(self):
        self.window.destroy()
        HelpClass()
        DictionaryOnline()

    def btn_clicked(self):
        word = self.word_to_search.get()

        if word == '' or word.startswith(' '):
            self.word_to_search.delete(0, END)
            mess.showwarning(title='Null Entry', message='Please enter word you wan\'t to find meaning.')
        elif len(word.split(' ')) > 1:
            self.word_to_search.delete(0, END)
            self.meaning_displaying_text_box.delete('1.0', END)
            mess.showwarning(title='Invalid Input', message='Word can\'t contain spaces.')
        else:
            if self.num_of_search != 0:
                self.meaning_displaying_text_box.delete(index1='1.0', index2=END)
            self.num_of_search += 1
            word = word.lower()
            meaning_of_word_str = Online_oxford_dist().meaning_of_word(text=word)
            self.meaning_displaying_text_box.insert(END, f'{meaning_of_word_str}')

class DictionaryOffline:

    def __init__(self):
        self.num_of_search = 0
        self.window = Tk()
        self.window.geometry("800x500")
        self.window.configure(bg="#362210")
        self.window.title('Prashant Offline Dictionary')

        self.canvas = Canvas(
            self.window,
            bg="#362210",
            height=500,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        img0 = PhotoImage(file=f"Program running image/img0.png")
        self.search_button = Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            background='#38360C',
            activebackground='#38360C',
            relief="flat")

        self.search_button.place(
            x=697, y=98,
            width=87,
            height=40)

        background_img = PhotoImage(file=f"Program running image/background.png")
        self.canvas.create_image(
            403.5, 213.0,
            image=background_img)

        entry0_img = PhotoImage(file=f"Program running image/img_textBox0.png")
        self.canvas.create_image(
            537.0, 118.0,
            image=entry0_img)

        self.word_to_search = Entry(
            bd=0,
            bg="#734e05",
            fg='white',
            font='QuicksandLight 15 bold',
            highlightthickness=0)

        self.word_to_search.focus()

        self.word_to_search.place(
            x=415.0, y=99,
            width=244.0,
            height=38)

        entry1_img = PhotoImage(file=f"Program running image/img_textBox1.png")
        self.canvas.create_image(
            592.0, 316.0,
            image=entry1_img)

        self.meaning_displaying_text_box = Text(
            bd=0,
            bg="#140d00",
            foreground='white',
            font='DustismoRoman 10',
            highlightthickness=0)

        self.meaning_displaying_text_box.place(
            x=420.0, y=177,
            width=344.0,
            height=278)

        self.window.resizable(False, False)
        self.window.bind('<Return>', lambda i: self.btn_clicked())
        self.window.bind('<Control-h>', lambda a: self.run_help())
        self.window.bind('<Control-q>', lambda a: exit())
        self.window.protocol('WM_DELETE_WINDOW', lambda: self.close_button_pressed())
        self.window.bind('<Control-Key-1>', lambda a: self.ctrl_1())
        self.window.bind('<Control-Key-2>', lambda a: self.ctrl_2())
        self.window.mainloop()

    def ctrl_1(self):
        self.window.destroy()
        DictionaryOffline()

    def ctrl_2(self):
        self.window.destroy()
        DictionaryOnline()

    def close_button_pressed(self):
        self.window.destroy()
        AskingAboutProgramExecution()

    def run_help(self):
        self.window.destroy()
        HelpClass()
        DictionaryOffline()

    def btn_clicked(self):
        word = self.word_to_search.get()
        meaning = []

        if word == '' or word.startswith(' '):
            self.word_to_search.delete(0, END)
            mess.showwarning(title='Null Entry', message='Please enter word you wan\'t to find meaning.')
        elif len(word.split(' ')) > 1:
            self.word_to_search.delete(0, END)
            self.meaning_displaying_text_box.delete('1.0', END)
            mess.showwarning(title='Invalid Input', message='Word can\'t contain spaces.')
        else:
            if self.num_of_search != 0:
                self.meaning_displaying_text_box.delete(index1='1.0', index2=END)
            self.num_of_search += 1
            word = word.title()

            with open('Program running image/Dictionary in csv/dict.json') as json_file:
                data = json.load(json_file)
            if word in data:
                self.meaning_displaying_text_box.insert(END, f'\nMeaning of the word {word} is:-')
                self.meaning_displaying_text_box.insert(END, f'\n\n#) {data[word]}')

            else:
                with open('Program running image/Dictionary in csv/dictionary.csv') as f:
                    data = csv.reader(f)
                    for row in data:
                        if row[0] == word:
                            meaning.append(row[2])

                    if len(meaning) == 0:
                        self.meaning_displaying_text_box.insert(END, f'\n\n\n\n\n\n\nOops!!!\n\nThere isn\'t any meaning of {word}.')
                        return

                self.meaning_displaying_text_box.insert(END, f'\nTotal Meanings: {len(meaning)}')
                for index, mean in enumerate(meaning):
                    self.meaning_displaying_text_box.insert(END, f'\n\n{index+1}) {mean}')

class AskingAboutProgramExecution:
    def submit_button_command(self):
        global online_or_offline
        information = self.radiobutton_int_var.get()
        if information == 1:
            self.window.destroy()
            DictionaryOnline()
            online_or_offline = 'online'
        elif information == 0:
            self.window.destroy()
            DictionaryOffline()
        else:
            mess.showerror(title='Null Selection', message='Please select ether online mode or offline mode.')

    def help_button_command(self):
        self.window.destroy()
        HelpClass()
        AskingAboutProgramExecution()

    def __init__(self):
        self.window = Tk()
        self.window.title('Prashant\'s Dictionary')
        self.window.geometry("400x400")
        self.window.configure(bg = "#ffffff")
        canvas = Canvas(
            self.window,
            bg = "#ffffff",
            height = 400,
            width = 400,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"Program running image/background_1.png")
        canvas.create_image(
            196.0, 198.0,
            image=background_img)

        self.radiobutton_int_var = IntVar()
        self.radiobutton_int_var.set(3)
        Radiobutton(text='', background='#1A1002', borderwidth=0, border=0, highlightthickness=0, activebackground='black', variable=self.radiobutton_int_var, value=0).place(x=42, y=188)
        Radiobutton(text='', background='#1A1002', borderwidth=0, border=0, highlightthickness=0, activebackground='black', variable=self.radiobutton_int_var, value=1).place(x=158, y=243)

        img0 = PhotoImage(file = f"Program running image/img0_1.png")
        self.submit_button = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.submit_button_command(),
            bg='#1A1002',
            activebackground='#1A1002',
            relief = RAISED)

        self.submit_button.place(
            x = 42, y = 310,
            width = 103,
            height = 35)

        img1 = PhotoImage(file = f"Program running image/img1_1.png")
        self_help_button = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            bg='#2C231C',
            activebackground='#2C231C',
            command = lambda: self.help_button_command(),
            relief = GROOVE)

        self_help_button.place(
            x = 261, y = 310,
            width = 103,
            height = 35)

        self.window.resizable(False, False)
        self.window.bind('<Return>', lambda i: self.submit_button_command())
        self.window.bind('1', lambda i : self.radiobutton_int_var.set(0))
        self.window.bind('2', lambda i : self.radiobutton_int_var.set(1))
        self.window.bind('<Control-h>', lambda a: self.help_button_command())
        self.window.bind('<Control-q>', lambda a: exit())
        self.window.bind('<Control-Key-1>', lambda a: self.ctrl_1())
        self.window.bind('<Control-Key-2>', lambda a: self.ctrl_2())
        self.window.mainloop()

    def ctrl_1(self):
        self.window.destroy()
        DictionaryOffline()

    def ctrl_2(self):
        self.window.destroy()
        DictionaryOnline()

class HelpClass:
    def __init__(self):
        self.run_next_program = False
        self.programmer_description_string = '''(#)This Program is made on July 18, 2022
by Prashant Ranjan Singh.


(#) This Program is basically an offline/
online dictionary.


(#) Linkedin Profile of mine :-'''
        self.working_of_program_explain_str = '''--> It is an dictionary which are used in daily life.

--> It has 2 options go online or offline. 

--> If we chose offline mode then it has limited word list throw which
it can find meaning of word and if we chose online mode then it will 
connect to Oxford API and fetch our data from there servers using API.

--> Shortcuts are :-
1) ctrl+1 --> Option 1 (Offline)                                5) ctrl+q --> Exit Program
2) ctrl+2 --> Option 2 (Online)
3) Enter --> For Searching
4) ctrl+h --> for opening help page'''
        background = 'white'

        # Screen
        self.screen = Tk()
        self.screen.geometry('600x620')
        self.screen.minsize(600, 620)
        self.screen.maxsize(600, 620)
        self.screen.title('Calculator By Prashant Ranjan Singh')
        self.screen.config(bg=background, padx=50, pady=50)
        self.screen.resizable(False, False)

        # image
        self.password_image = ImageTk.PhotoImage(Image.open("Program running image/Mine_photo.jpg"))
        self.image = Label(width=250, height=250, image=self.password_image, borderwidth=0)

        # Label
        self.text = Label()
        self.about_programmer = Label(text='About Programmer', font=('LatinModernRomanDunhill', 12, 'bold'),
                                      background=background)
        self.text.configure(text=self.programmer_description_string, bg='white', justify=LEFT)
        self.link = Label(text="www.linkedin.com", fg="blue", cursor="hand2", bg=background)
        self.link.bind("<Button-1>", lambda e: self.callback("www.linkedin.com/in/prashant-ranjan-singh-b9b6b9217"))
        self.working_heading = Label(text='Working of Program', font=('LatinModernRomanDunhill', 12, 'bold'),
                                     bg=background)
        self.working_of_program_explain = Label(text=self.working_of_program_explain_str, bg='white', justify=LEFT)

        # Create a Label to display the link
        self.image.grid(column=0, row=0)
        self.about_programmer.grid(column=1, row=0, sticky=NE, padx=70)
        self.text.grid(column=1, row=0, sticky=NW, pady=50, padx=10)
        self.link.grid(column=1, row=0, sticky=SW, padx=35, pady=30)
        self.working_heading.grid(column=0, row=1, padx=50, columnspan=2, pady=5)
        self.working_of_program_explain.grid(column=0, row=2, columnspan=3, sticky=W)
        self.screen.bind('<Control-Key-1>', lambda a: self.ctrl_1())
        self.screen.bind('<Control-Key-2>', lambda a: self.ctrl_2())
        self.screen.bind('<Control-q>', lambda a: exit())
        self.screen.mainloop()

    def ctrl_1(self):
        self.screen.destroy()
        DictionaryOffline()

    def ctrl_2(self):
        self.screen.destroy()
        DictionaryOnline()

    @staticmethod
    def callback(url):
        webbrowser.open_new_tab(url)

class Errors:
    def file_missing(cls,
                     url='https://github.com/Prashant-ranjan-singh-123/GUI_Dictionary',
                     show_name_of_url='www.github.com'):
        def callback(url):
            webbrowser.open_new_tab(url)

        root = Tk()
        cls.background = 'white'
        root.geometry('500x310')
        root.resizable(False, False)
        root.title('Dictionary by Prashant Singh')
        root.config(background=cls.background, borderwidth=30)

        def exit_command():
            nonlocal root
            root.destroy()
            is_rerun = False

        # Heading Label
        cls.L1 = Label(root, text='Prashant\'s Dictionary', font='LatinModernRomanDunhill 20 bold',
                       background=cls.background)
        cls.L1.pack(anchor='center')

        # Label
        cls.error = Label(root, text='Error', foreground='red', font='arial 30 bold', justify=CENTER,
                          background=cls.background)
        cls.error.pack(anchor='center', pady=20)

        cls.what_to_do = Label(root, text=f'You wont have essential component\'s for proper \n'
                                          f'execution of program please download it from \n'
                                          f'official github repository from below link :-',
                               font=('arial', 12, 'bold'), justify=CENTER, bg=cls.background)
        cls.what_to_do.pack()

        cls.link = Label(text=show_name_of_url, fg="blue", cursor="hand2", bg=cls.background,
                         font=('arial', 12, 'bold'))
        cls.link.bind("<Button-1>", lambda e: callback(url))
        cls.link.pack(anchor='center')

        # Button
        exit_button = Button(text='Previous Menu', bg='#ff4d4d', padx=40, borderwidth=2, highlightbackground='black',
                             activebackground='#ff0000', command=exit_command)
        exit_button.place(x=480, y=300)
        root.mainloop()

if __name__ == '__main__':
    all_file_there = True
    if os.path.exists('Program running image'):
        if not os.path.exists('Program running image/background_online.png'):
            all_file_there = False
        if not os.path.exists('Program running image/background.png'):
            all_file_there = False
        if not os.path.exists('Program running image/background_1.png'):
            all_file_there = False
        if not os.path.exists('Program running image/img0.png'):
            all_file_there = False
        if not os.path.exists('Program running image/img0_1.png'):
            all_file_there = False
        if not os.path.exists('Program running image/img1_1.png'):
            all_file_there = False
        if not os.path.exists('Program running image/img_textBox0.png'):
            all_file_there = False
        if not os.path.exists('Program running image/img_textBox1.png'):
            all_file_there = False
        if not os.path.exists('Program running image/Dictionary in csv'):
            all_file_there = False
        if not os.path.exists('Program running image/Dictionary in csv/dict.json'):
            all_file_there = False
        if not os.path.exists('Program running image/Dictionary in csv/dictionary.csv'):
            all_file_there = False

    else:
        all_file_there = False
    if not os.path.exists('Program running image/Mine_photo.jpg'):
        all_file_there = False

    if all_file_there:
        AskingAboutProgramExecution()

    else:
        Errors().file_missing()



