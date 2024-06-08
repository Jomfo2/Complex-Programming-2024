from tkinter import *

class Converter:
    def __init__(self):
        # *** Options ***
        self.options = ["Centimeters", "Meters", "Kilometers", "Inches", "Feet", "Yards"]
        self.unit_types = ["Time", "Distance", "Weight"]

        # Variables for storing desired input and output units
        self.selected_input = StringVar()
        self.selected_input.set(self.options[1])

        self.selected_output = StringVar()
        self.selected_output.set(self.options[4])

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
        instructions = "Instructions go here..." \
                       "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quam velit, vulputate eu pharetra nec, mattis ac neque. Duis vulputate commodo lectus, ac blandit elit tincidunt id. Sed rhoncus, tortor sed eleifend tristique, tortor mauris molestie elit, et lacinia ipsum quam nec dui. Quisque nec mauris sit amet elit iaculis pretium sit amet quis magna. Aenean velit odio, elementum in tempus ut, vehicula eu diam. Pellentesque rhoncus aliquam mattis. Ut vulputate eros sed felis sodales nec vulputate justo hendrerit. Vivamus varius pretium ligula, a aliquam odio euismod sit amet. Quisque laoreet sem sit amet orci ullamcorper at ultricies metus viverra. Pellentesque arcu mauris, malesuada quis ornare accumsan, blandit sed diam."
        self.converter_instructions = Label(self.converter_frame, text=instructions,
                                            wraplength=400, justify="left",
                                            pady=20)
        self.converter_instructions.grid(row=1)

        # ** Entry Section **
        self.entry_frame = Frame(self.converter_frame)
        self.entry_frame.grid(row=2)

        # Input Type Selector
        self.dropdown_input = OptionMenu(self.entry_frame, self.selected_input, *self.options)
        self.dropdown_input.config(width=20)
        self.dropdown_input.grid(row=0, column=0, padx=5, pady=5)

        # Text Entry Input
        self.input_entry = Entry(self.entry_frame, font=("Arial", "12"))
        self.input_entry.grid(row=0, column=1, padx=5, pady=5)

        # Output Type Selector
        self.dropdown_output = OptionMenu(self.entry_frame, self.selected_output, *self.options)
        self.dropdown_output.config(width=20)
        self.dropdown_output.grid(row=1, column=0, padx=5, pady=5)

        # Text Entry Output
        self.output_entry = Entry(self.entry_frame, font=("Arial", "12"))
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
                                     font=("Arial", "10", "bold"), width=12,
                                     command=self.convert)
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
                                            font=("Arial", "10"), width=12)
        self.history_export_button.grid(row=0, column=1, padx=5, pady=5)

    def read_inputs(self):
        # Read Inputted Info
        self.input_units = self.selected_input.get()
        self.output_units = self.selected_output.get()
        self.input_int = self.input_entry.get()
        print("Converting {} {} to {}".format(self.input_int, self.input_units, self.output_units))

    def convert(self):
        self.read_inputs()


# main routine
if __name__ == '__main__':
    root = Tk()
    root.title("Measurement Converter")
    root.geometry("500x550")

    # Configure grid of root window to add weight
    # Solution to centering issues by ChatGPT
    root.grid_columnconfigure(0, weight=1)

    Converter()
    root.mainloop()