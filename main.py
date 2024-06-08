from tkinter import *

class Converter:
    def __init__(self):
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
        self.selected_output.set(self.current_options[3])

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
                                  state="readonly")
        self.output_entry.grid(row=1, column=1, padx=5, pady=5)

        # ** Type / Convert Section **
        self.type_convert_frame = Frame(self.converter_frame)
        self.type_convert_frame.grid(row=3)

        # Unit Type Selector
        self.type_selector = OptionMenu(self.type_convert_frame, self.selected_type, *self.unit_types,
                                        command=self.switch_lists)
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

    # Checks input to make sure it's a number
    def check_input(self):
        # try convert input_entry to float
        # breaks when it doesn't work
        try:
            input_int = float(self.input_entry.get())
            return input_int

        except ValueError:
            print("Please enter an integer")

    # Reads all relevant inputs and stores them in variables for easy use
    def read_inputs(self, input_int):
        # Read Inputted Info
        input_units = self.selected_input.get()
        output_units = self.selected_output.get()
        unit_type = self.selected_type.get()

        # Checks if self.input is a number or 0
        if input_int or input_int == 0:
            print("Converting {} {} to {}".format(input_int, input_units, output_units))
        return [input_int, input_units, output_units, unit_type]

    # Converts from the user's input to a 'base' variable
    def input_to_base(self, input_vars):
        input = input_vars[0] # int input
        input_unit = input_vars[1] # input unit
        unit_type = input_vars[3] # unit type
        base = 0

        match unit_type:
            # If time units, convert to seconds
            case "Time":
                match input_unit:
                    case "Milliseconds": base = input * 0.001
                    case "Seconds":      base = input
                    case "Minutes":      base = input * 60
                    case "Hours":        base = input * 3600
                    case "Days":         base = input * 86400
                    case "Weeks":        base = input * 604800
                    case "Years":        base = input * 31556952
                    case _: print("Error converting input to seconds")
            # If distance units, convert to meters
            case "Distance":
                match input_unit:
                    case "Millimeters":  base = input * 0.001
                    case "Centimeters":  base = input * 0.01
                    case "Meters":       base = input
                    case "Kilometers":   base = input * 1000
                    case "Inches":       base = input * 0.0254
                    case "Feet":         base = input * 0.3048
                    case "Yards":        base = input * 0.9144
                    case "Miles":        base = input * 1609.34
                    case _: print("Error converting input to meters")
            # If weight units, convert to kilograms
            case "Weight":
                match input_unit:
                    case "Grams":       base = input * 0.0001
                    case "Kilograms":   base = input
                    case "Metric Tons": base = input * 1000
                    case "Ounces":      base = input * 0.0283
                    case "Pounds":      base = input * 0.4536
                    case "Tons":        base = input * 907.185
                    case "Tonnes":      base = input * 1016.05
                    case _: print("Error converting input to kilograms")
            # If other unit type, print error message
            case _:
                print("Error converting to unit_type")

        return base

    # Converts from the user's input to a 'base' variable
    def base_to_output(self, input_vars, base):
        output_unit = input_vars[2] # input unit
        unit_type = input_vars[3] # unit type
        output = 0

        match unit_type:
            # If time units, convert to seconds
            case "Time":
                match output_unit:
                    case "Milliseconds": output = base / 0.001
                    case "Seconds":      output = base
                    case "Minutes":      output = base / 60
                    case "Hours":        output = base / 3600
                    case "Days":         output = base / 86400
                    case "Weeks":        output = base / 604800
                    case "Years":        output = base / 31556952
                    case _: print("Error converting input to seconds")
            # If distance units, convert to meters
            case "Distance":
                match output_unit:
                    case "Millimeters":  output = base / 0.001
                    case "Centimeters":  output = base / 0.01
                    case "Meters":       output = base
                    case "Kilometers":   output = base / 1000
                    case "Inches":       output = base / 0.0254
                    case "Feet":         output = base / 0.3048
                    case "Yards":        output = base / 0.9144
                    case "Miles":        output = base / 1609.34
                    case _: print("Error converting input to meters")
            # If weight units, convert to kilograms
            case "Weight":
                match output_unit:
                    case "Grams":       output = input / 0.0001
                    case "Kilograms":   output = input
                    case "Metric Tons": output = input / 1000
                    case "Ounces":      output = input / 0.0283
                    case "Pounds":      output = input / 0.4536
                    case "Tons":        output = input / 907.185
                    case "Tonnes":      output = input / 1016.05
                    case _: print("Error converting input to kilograms")
            # If other unit type, print error message
            case _:
                print("Error converting to unit_type")

        return output

    # Main function triggered when converting
    def convert(self):
        # Collect all relevant info and put them in variables for easy use
        if self.check_input():
            input_int = self.check_input()
            input_vars = self.read_inputs(input_int)
            base = self.input_to_base(input_vars)
            output = self.base_to_output(input_vars, base)
            print(output)

    # Function to switch lists between types
    def switch_lists(self, new_type):
        self.dropdown_input["menu"].delete(0, "end")
        self.dropdown_output["menu"].delete(0, "end")

        # Switch/Match statement to choose function based on input
        match new_type:
            case "Time":
                self.current_options = self.time_options
            case "Distance":
                self.current_options = self.distance_options
            case "Weight":
                self.current_options = self.weight_options

            # if no other cases are met
            case _:
                print("Exception: Chosen list is not applicable")

        # For loop code supplied by ChatGPT
        for item in self.current_options:
            self.dropdown_input["menu"].add_command(label=item, command=lambda value=item: self.selected_input.set(value))
            self.dropdown_output["menu"].add_command(label=item, command=lambda value=item: self.selected_input.set(value))

        self.selected_input.set(self.current_options[1])
        self.selected_output.set(self.current_options[4])



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