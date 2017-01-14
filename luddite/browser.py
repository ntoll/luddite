"""
Contains the core classes for the Luddite browser.
"""
import requests
# import classic tkinter widgets
from tkinter import Tk, Text
# import Tkinter constants
from tkinter import N, E, S, W, END, INSERT, X, Y, RIGHT, BOTTOM
# import themed Tkinter widgets
from tkinter.ttk import Button, Entry, Frame, Notebook, Scrollbar

class Tab(Frame):
    """
    Represents a tab in the main browser.
    """

    def setup(self, url):
        """
        Add the address bar, "GO" button and page display area for the tab.
        """
        self.address_bar = Entry(self)
        self.go_button = Button(self, text='GO', command=self._get)
        self.page = Text(self)
        vbar = Scrollbar(self.page)
        vbar['command'] = self.page.yview
        vbar.pack(side=RIGHT, fill=Y)
        self.page['yscrollcommand'] = vbar.set
        self.address_bar.grid(row=0, column=0, sticky=W+E)
        self.go_button.grid(row=0, column=1, sticky=E)
        self.page.grid(row=1, column=0, columnspan=2, sticky=N+E+S+W)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.url = url
        if self.url:
            self.address_bar.insert(0, self.url)
            self._get()

    def _get(self):
        """
        Get the URL in the address bar.
        """
        url = self.address_bar.get()
        response = requests.get(url)
        if response.ok:
            self.page.delete('1.0', END)
            self.page.insert(INSERT, response.text)
    

class Browser(Tk):
    """
    The core class representing the browser.
    """

    def __init__(self):
        super().__init__()
        self.title('Luddite')
        self.geometry('800x600')
        self.tab_holder = Notebook(self)
    
    def create_tab(self, url=None):
        """
        Create a new tab. Navigate to the optional URL.
        """
        new_tab = Tab()
        new_tab.setup(url)
        self.tab_holder.add(new_tab, text=url)
        self.tab_holder.pack(expand=1, fill='both')
        return new_tab
