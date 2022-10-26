# # Import the required Libraries
import json
from logging import PlaceHolder
from tkinter import *
from tkinter import filedialog
import os
from tkinter.messagebox import showinfo
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.cm as cm
from tkinter import Tk, BOTH, W, N, E, S
from tkinter.ttk import Frame, Label
from matplotlib.font_manager import json_dump
import pandas as pd
from os.path import exists
import numpy as np


class Display(Frame):

    def __init__(self):
        super().__init__()
        self.airport_frequencies_path = None
        self.airports_path = None
        self.runway_path = None
        self.highf_mean = StringVar()
        self.highf_mode = StringVar()
        self.highf_median = StringVar()
        self.large_mean = StringVar()
        self.large_median = StringVar()
        self.large_mode = StringVar()

        self.highf_mean.set("0")
        self.highf_mode.set("0")
        self.highf_median.set("0")
        self.large_mean.set("0")
        self.large_median.set("0")
        self.large_mode.set("0")

        self.initUI()

    def initUI(self):
        self.master.title("Airport Data Visualizer")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        lbl = Label(self, text="Airport Data Visualizer")
        lbl.grid(sticky=W, pady=4, padx=5)

        # area = Text(self)
        # area.grid(row=1, column=0, columnspan=3, rowspan=4,
        #           padx=5, sticky=E + W + S + N)

        self.frequency = Button(self, text="Frequency Data", command=self.set_frequencies_path, activebackground="blue")
        self.frequency.grid(row=1, column=3, pady=1)
        self.airport = Button(self, text="Airport Data", command=self.set_airport_path, activebackground="blue")
        self.airport.grid(row=2, column=3, padx=1)
        self.runways = Button(self, text="Runways Data", command=self.set_runway_path, activebackground="blue")
        self.runways.grid(row=3, column=3, padx=1)
        self.show_data_button=Button(self,text="Show Data", command=self.view_json,activeforeground="green")
        self.show_data_button.grid(row=4,column=3,pady=1)
        
        self.load_saved=Button(self,text="Load Saved Data", command=self.load_saved,activeforeground="green")
        self.load_saved.grid(row=5,column=3,pady=1)
        self.save_data=Button(self,text="Save Data", command=self.save_data,activeforeground="green")
        self.save_data.grid(row=6,column=3,pady=1)
        
        
        self.clean = Button(self, text="Clean Data", command=self.clean_data)
        
        self.clean.grid(row=7, column=3, pady=1)

        hbtn = Button(self, text="Visualize Data", bg="blue", fg="white", command=self.display_data)
        hbtn.grid(row=22, column=0, padx=3, pady=2)

        obtn = Button(self, text="Calculate Statistics", command=self.calculate_statistics, bg="blue", fg="white")
        obtn.grid(row=22, column=3, pady=2)
        
        range_label=Label(self, text="Frequency Range To Display")
        range_label.grid(row=8,column=0,columnspan=2)
        
        lower_label=Label(self, text="Lower")
        lower_label.grid(row=9,column=0,columnspan=1)
        
        upper_label=Label(self, text="Upper")
        upper_label.grid(row=10,column=0,columnspan=1)
        self.lower_range=Entry(self)
        self.lower_range.grid(row=9,column=1, pady=1,padx=2)
        self.upper_range=Entry(self)
        self.upper_range.grid(row=10,column=1, pady=1,padx=2)
        sumarry_label = Label(self, text="Summary Statistics")
        sumarry_label.grid(row=11,pady=1, columnspan=2, rowspan=2)
        large_airport_label = Label(self, text="Large Airport:")
        large_airport_label.grid(row=12, column=0)
        mean_label_L = Label(self, text="Mean:")
        mean_label_L.grid(row=13, column=0)
        mean_label_LV = Label(self, textvariable=self.large_mean)
        mean_label_LV.grid(row=13, column=1)
        mode_label_L = Label(self, text="Mode:")
        mode_label_L.grid(row=14, column=0)
        mode_label_LV = Label(self, textvariable=self.large_mode)
        mode_label_LV.grid(row=14, column=1)
        median_label_L = Label(self, text="Median:")
        median_label_L.grid(row=15, column=0)
        median_label_LV = Label(self, textvariable=self.large_median)
        median_label_LV.grid(row=15, column=1)

        highf_airport_label = Label(self, text="Frequencies>100mhz:")
        highf_airport_label.grid(row=10, column=2)
        mean_label_H = Label(self, text="Mean:")
        mean_label_H.grid(row=11, column=2)
        mean_label_V = Label(self, textvariable=self.highf_mean)
        mean_label_V.grid(row=11, column=3)
        mode_label_H = Label(self, text="Mode:")
        mode_label_H.grid(row=12, column=2)
        mode_label_V = Label(self, textvariable=self.highf_mode)
        mode_label_V.grid(row=12, column=3)
        median_label_H = Label(self, text="Median:")
        median_label_H.grid(row=13, column=2)
        median_label_V = Label(self, textvariable=self.highf_median)
        median_label_V.grid(row=13, column=3)
    def save_data(self):
        showinfo("Data Saved", "Your has been saved!")
    def load_saved(self):
        if exists("merged_and_clean.json"):
            f = open("merged_and_clean.json")
            data = json.load(f)
            data=json.dumps(data,indent=4)
            # data = pd.read_json("merged_and_clean.json")
            text=Text(self, font="Times32")
            pd.set_option('display.max_columns', None)
        
            text.insert("end", data)
            text.grid(row=1, column=0, columnspan=3, rowspan=4,
                                            padx=5, sticky=E + W + S + N)
            f.close()
        else:
            showinfo("No Clean File", "Sorry we could not find a cleaned file\nEnsure upload and clean data before "
                                    "visualizing data!")
    def view_json(self):
        
        if exists("merged_and_clean.json"):
            # f = open("merged_and_clean.json")
            # data = json.load(f)
            # data=json.dumps(data,indent=4)
            data = pd.read_json("merged_and_clean.json")
            text=Text(self, font="Times32")
            pd.set_option('display.max_columns', None)
        
            text.insert("end", data)
            text.grid(row=1, column=0, columnspan=3, rowspan=4,
                                            padx=5, sticky=E + W + S + N)
            # f.close()
        else:
            showinfo("No Clean File", "Sorry we could not find a cleaned file\nEnsure upload and clean data before "
                                    "visualizing data!")


    def calculate_statistics(self):
        if exists("merged_and_clean.json"):
            data = pd.read_json("merged_and_clean.json")
        
            large_airport_data = data[data["type_y"] == "large_airport"]
            large_airport_frequency = large_airport_data["frequency_mhz"]
            highf_airport = data[data["frequency_mhz"] > 100]
            Hf_D = highf_airport["frequency_mhz"]
            Hf_mean = Hf_D.mean()
            Hf_median = Hf_D.median()
            Hf_mode = Hf_D.mode()
            L_mean = large_airport_frequency.mean()
            L_mode = large_airport_frequency.mode()
            L_median = large_airport_frequency.median()
            # print("Median",L_median)
            # print( L_mode[0])
            # print("Mean", L_mean)
            self.large_mode.set(L_mode[0])
            self.large_median.set(L_median)
            self.large_mean.set(L_mean)
            self.highf_mode.set(Hf_mode[0])
            self.highf_median.set(Hf_median)
            self.highf_mean.set(Hf_mean)

        else:
            showinfo("No Clean File", "Sorry we could not find a cleaned file\n Ensure you upload and clean files "
                                      "before "
                                      "calculating statistics!")

    def display_data(self):
        if exists("merged_and_clean.json"):
            data = pd.read_json("merged_and_clean.json")
            data_small_airports = data[data["type_y"] == "small_airport"]

            fig = Figure(figsize=(5, 5),
                         dpi=100)
            airport_types = data["type_y"]
            frequencies = data["frequency_mhz"]
            plot1 = fig.add_subplot(121)
            plot1.hist(data_small_airports["frequency_mhz"])
            plot1.set_title("Frequency Used By Small Airports")
            plot1.set_ylabel("Number of Airports")
            plot1.set_xlabel("Frequency Used")

            plot2 = fig.add_subplot(122)
            
            colors = cm.rainbow(np.linspace(0, 1, len(frequencies)))
            plot2.scatter(airport_types, frequencies, color=colors)
            plot2.set_title("Frequencies Used By Various Airport Categories")
            plot2.set_ylabel("Frequency (Mhz)")
            plot2.set_xlabel("Airport Category")

            canvas = FigureCanvasTkAgg(fig,
                                       master=self)
            canvas.draw()

            # placing the canvas on the Tkinter window
            canvas.get_tk_widget().grid(row=1, column=0, columnspan=3, rowspan=4,
                                        padx=5, sticky=E + W + S + N)


        else:
            showinfo("No Clean File", "Sorry we could not find a cleaned file\nEnsure upload and clean data before "
                                      "visualizing data!")

    def set_airport_path(self):
        file = filedialog.askopenfile(mode='r', filetypes=[('Comma Separated Files', '*.csv')])
        if file:
            self.airports_path = os.path.abspath(file.name)
            self.airport.configure(bg="gray", fg="blue")

    def set_runway_path(self):
        file = filedialog.askopenfile(mode='r', filetypes=[('Comma Separated Files', '*.csv')])
        if file:
            self.runway_path = os.path.abspath(file.name)
            self.runways.configure(bg="gray", fg="blue")

    def set_frequencies_path(self):
        file = filedialog.askopenfile(mode='r', filetypes=[('Comma Separated Files', '*.csv')])
        if file:
            self.airport_frequencies_path = os.path.abspath(file.name)
            self.frequency.configure(bg="gray", fg="blue")

    def clean_data(self):
        if self.runway_path and self.airports_path and self.airport_frequencies_path:
            try:
                frequencies = pd.read_csv(self.airport_frequencies_path)
                airports = pd.read_csv(self.airports_path)
                runways = pd.read_csv(self.runway_path)
                airports = airports.rename(columns={"ident": "airport_ident"})
                # using merge function
                airports_frequency = pd.merge(frequencies, airports,
                                              on='airport_ident',
                                              how='outer')
                airports_frequency_runways = pd.merge(airports_frequency, runways,
                                                      on='airport_ident',
                                                      how='outer')
                # Removing columns with many empty cells and not needed for analysis
                columns_to_drop = ["le_elevation_ft", "le_displaced_threshold_ft", "he_elevation_ft",
                                   "he_heading_degT", "he_displaced_threshold_ft"]
                airports_frequency_runways.drop(columns_to_drop, axis=1, inplace=True)
                airports_frequency_runways = airports_frequency_runways.dropna()
                airports_frequency_runways = airports_frequency_runways[airports_frequency_runways['closed'] == 0]
                airports_frequency_runways.to_json("merged_and_clean.json")
            except Exception as e:
                showinfo("Unknown Error", "We encountered an error while cleaning the files\n Some actions that might "
                                          "help\n 1. Ensure all the files are uploaded in the right area\n"
                                          "2. Ensure the files are not corrupted\n3. Ensure you upload the right files")
                print(e)

        else:
            showinfo("Missing Files", "Ensure that all files are chosen!")


def main():
    root = Tk()
    root.geometry("350x300+300+300")
    app = Display()
    root.mainloop()


if __name__ == '__main__':
    main()
