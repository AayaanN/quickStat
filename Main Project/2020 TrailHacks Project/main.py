# IMPORTS
import tkinter as tk
from tkinter.font import Font
from svglib.svglib import svg2rlg
from PIL import Image, ImageTk
from reportlab.graphics import renderPM
import pygal
from pygal.style import NeonStyle

#------------------FUNCTIONS
def create_radar(player_name,stats):
    radar_chart = pygal.Radar(width=500,height=400, style=NeonStyle)
    radar_chart.title = 'Comparing Businesses'
    radar_chart.x_labels = ["Customer Service", "Prices", "Popularity", "Product Quality", "Specialty"]
    radar_chart.add(player_name, stats)
    radar_chart.render_to_file("Images/radarchart.svg")

def convert_svg(svg_file):
    file = svg2rlg('Images/' + svg_file)
    renderPM.drawToFile(file,"Images/radarchart.png",fmt="PNG")

def main():
    root = tk.Tk()
    create_radar("Apple",[4,3,5,5,3])
    convert_svg('radarchart.svg')
    main_window = Window(root,'quickStat','800x500')

class Window:
    def __init__(self,root,title,size):
        self.root = root
        self.root.title(title)
        self.root.geometry(size)
        self.root.resizable(0,0)
        self.gray = '#292424'
        self.orange = '#E68422'
        self.font = Font(family="MS Reference Sans Serif", size=40, weight="bold", slant="italic")
        self.font2 = Font(family="MS Reference Sans Serif",size=16, weight="bold", slant="italic")

        self.design()
        self.root.mainloop()

    def handle_focus_in(self):
        self.search_bar.delete(0, tk.END)
        self.search_bar.config(fg='black')

    def handle_focus_out(self):
        self.search_bar.delete(0, tk.END)
        self.search_bar.config(fg='grey')
        self.search_bar.insert(0, "Search for players, eg. Kawhi Leonard")

    def handle_enter(self):
        print(self.search_bar.get())
        self.handle_focus_out()

    def design(self):
        self.root.configure(background=self.gray) # set bg colour on entire window
        tk.Label(self.root, text="quickStat", background=self.gray, fg=self.orange, font=self.font).pack(pady=(100,35))
        self.search_bar = tk.Entry(self.root,bd=1,width=75, relief="groove")
        self.search_bar.pack(ipady=10)
        self.search_bar.insert("Search for players, eg. Kawhi Leonard")
        self.search_bar.bind("<FocusIn",self.handle_focus_in())
        self.search_bar.bind("<FocusOut",self.handle_focus_out())
        self.search_bar.bind("<Return",self.handle_enter())

        tk.Label(self.root, text="The simplest, most relevant basketball database out there", background=self.gray, fg=self.orange, font=self.font2).pack(pady=(35,0))

#----------------------------

main()