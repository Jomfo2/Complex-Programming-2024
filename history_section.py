from tkinter import *
from functools import partial

class Converter:
    def __init__(self):

        self.example_hist = ['Converted 15.0 Centimeters to 5.906 Inches',
                             'Converted 15.0 Kilometers to 49212.598 Feet',
                             'Converted 15.0 Seconds to 0.25 Minutes']

        # *** Options ***
        self.time_options = ["Milliseconds", "Seconds", "Minutes", "Hours", "Days", "Weeks", "Years"]
        self.distance_options = ["Millimeters", "Centimeters", "Meters", "Kilometers", "Inches", "Feet", "Yards", "Miles"]
        self.weight_options = ["Grams", "Kilograms", "Metric Tons","Ounces", "Pounds", "Tons", "Tonnes"]

        # Use and change this list
        self.current_options = self.distance_options

        self.unit_types = ["Time", "Distance", "Weight"]

        # Variables for storing desired input and output units
        self.selected_input = StringVar()
        self.selected_input.set(self.current_options[1])

        self.selected_output = StringVar()
        self.selected_output.set(self.current_options[4])

        self.selected_type = StringVar()
        self.selected_type.set(self.unit_types[1])

        # Setup GUI Frame
        self.converter_frame = Frame(padx=10, pady=10)
        self.converter_frame.grid()

        # Heading Widget
        self.converter_heading = Label(self.converter_frame, text="Measurement Converter",
                                       font=("Arial", "16", "bold"), padx=50,
                                       pady=10, justify="left")
        self.converter_heading.grid(row=0)

        # Instructions Widget
        instructions = "To use the Measurement Converter, type your desired number into the entry box, " \
                       "select the input and output units using the dropdowns beside the input and output, " \
                       "and click 'Convert'. \n\n" \
                       "For extended instructions and help, click the 'Help' button at the bottom of the window"
        self.converter_instructions = Label(self.converter_frame, text=instructions,
                                            wraplength=400, justify="left",
                                            pady=20)
        self.converter_instructions.grid(row=1)

        # ** Entry Section **
        self.entry_frame = Frame(self.converter_frame)
        self.entry_frame.grid(row=2)

        # Input Type Selector
        self.dropdown_input = OptionMenu(self.entry_frame, self.selected_input, *self.current_options)
        self.dropdown_input.config(width=20)
        self.dropdown_input.grid(row=0, column=0, padx=5, pady=5)

        # Text Entry Input
        self.input_entry = Entry(self.entry_frame, font=("Arial", "12"))
        self.input_entry.grid(row=0, column=1, padx=5, pady=5)

        # Output Type Selector
        self.dropdown_output = OptionMenu(self.entry_frame, self.selected_output, *self.current_options)
        self.dropdown_output.config(width=20)
        self.dropdown_output.grid(row=1, column=0, padx=5, pady=5)

        # Text Entry Output
        self.output_entry = Entry(self.entry_frame, font=("Arial", "12"),
                                  state=DISABLED)
        self.output_entry.grid(row=1, column=1, padx=5, pady=5)

        # ** Type / Convert Section **
        self.type_convert_frame = Frame(self.converter_frame)
        self.type_convert_frame.grid(row=3)

        # Unit Type Selector
        self.type_selector = OptionMenu(self.type_convert_frame, self.selected_type, *self.unit_types)
        self.type_selector.config(width=10, font=("Arial", "10"))
        self.type_selector.grid(row=0, column=0, padx=5, pady=5)

        # Convert Button
        self.convert_button = Button(self.type_convert_frame, text="Convert",
                                     font=("Arial", "10", "bold"), width=12)
        self.convert_button.grid(row=0, column=1, padx=5, pady=5)

        # ** Help / History Section **
        self.help_history_frame = Frame(self.converter_frame)
        self.help_history_frame.grid(row=4)

        # Help Button
        self.help_button = Button(self.help_history_frame, text="Help",
                                  font=("Arial", "10"), width=12)
        self.help_button.grid(row=0, column=0, padx=5, pady=5)

        # History/Export Button
        self.history_export_button = Button(self.help_history_frame, text="History / Export",
                                            font=("Arial", "10"), width=12,
                                            command=self.to_history_window)
        self.history_export_button.grid(row=0, column=1, padx=5, pady=5)

    def to_history_window(self):
        HistWindow(self)

class HistWindow:
    def __init__(self, partner):
        # Options
        self.hist_box = Toplevel()

        # Disable History / Export button
        partner.history_export_button.config(state=DISABLED)

        # Enable History button when window closed
        self.hist_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Setup GUI Frame
        self.hist_frame = Frame(self.hist_box, width=300,
                                height=200)
        self.hist_frame.grid()

        # Heading Label
        self.hist_heading_label = Label(self.hist_frame, text="History / Export",
                                        font=("Arial", "14", "bold"))
        self.hist_heading_label.grid(row=0)

        # File name entry
        self.filename_entry = Entry(self.hist_frame, font=("Arial", "14"),
                                    width=25)
        self.filename_entry.grid(row=1)

        # History Export Text
        hist_text = "You can export your history using the 'Export' button at the bottom of the page. It will be saved " \
                    "with the name entered above or a name automatically chosen. \n\n" \
                    "Below are the inputs and outputs for all of your calculations. All outputs rounded to up to 5dp"
        self.hist_text_label = Label(self.hist_frame, text=hist_text,
                                     wraplength=350, justify="left")
        self.hist_text_label.grid(row=2, padx=10)

        # History Label
        self.history_display = Label(self.hist_frame, font=("Arial", "10"),
                                     width=40, justify="left",
                                     text="You haven't done any conversions yet...", bg="gray",
                                     fg="white")
        self.history_display.grid(row=3)

        # *** Button Frame ***
        self.button_frame = Frame(self.hist_frame)
        self.button_frame.grid(row=4)

        # Close Button
        self.close_button = Button(self.button_frame, font=("Arial", "10", "bold"),
                                   text="Close", command=partial(self.close_history, partner))
        self.close_button.grid(row=0, column=0, padx=10, pady=10)

        # Export Button
        self.export_button = Button(self.button_frame, font=("Arial", "10", "bold"),
                                   text="Export", command=self.export_history)
        self.export_button.grid(row=0, column=1, padx=10, pady=10)

        # **** Display History ****
        self.calc_list = ""
        for item in partner.example_hist:
            self.calc_list = self.calc_list + item + '\n'
        self.history_display.config(text=self.calc_list)

    # Function to export history
    def export_history(self):
        pass

    # Function to close help dialogue
    def close_history(self, partner):
        # Put help button back to normal
        partner.history_export_button.config(state=NORMAL)
        self.hist_box.destroy()

# main routine
if __name__ == '__main__':
    root = Tk()
    root.title("Measurement Converter")
    root.geometry("500x450")

    # Configure grid of root window to add weight
    # Solution to centering issues by ChatGPT
    root.grid_columnconfigure(0, weight=1)

    Converter()
    root.mainloop()