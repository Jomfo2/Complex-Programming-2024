from tkinter import *
from functools import partial

class Converter:
    def __init__(self):
        # Variables
        self.history_list = []

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
                                  font=("Arial", "10"), width=12,
                                  command=self.to_help_window)
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

    # Function to round input to 2dp
    @staticmethod
    def round_number(num, sfs):
        if sfs < 3:
            num_rounded = round(num, sfs)  # Round input to sfs dp
        else:
            num_rounded = round(num, 3)  # Round input to 6dp
        return num_rounded

    # Function to count significant figures in a number
    @staticmethod
    def count_significant_figures(num):
        # Convert number to string and strip leading/trailing spaces
        num_str = str(num).strip()

        # Remove leading and trailing zeros and the decimal point for counting
        if '.' in num_str:
            # Split into integer and fractional parts
            integer_part, fractional_part = num_str.split('.')
            # Remove leading zeros from integer part
            integer_part = integer_part.lstrip('0')
            # Remove trailing zeros from fractional part
            fractional_part = fractional_part.rstrip('0')
            # Concatenate the significant parts
            significant_part = integer_part + fractional_part
        else:
            # If no decimal point, just remove leading zeros
            significant_part = num_str.lstrip('0')

        # Return the length of the significant part
        return len(significant_part)

    # Function for operations involving base conversions
    @staticmethod
    def base_conversion(input_vars, base, operation):
        input_int = input_vars[0] # input number
        input_unit = input_vars[1] # input unit
        output_unit = input_vars[2] # output unit
        unit_type = input_vars[3] # unit type
        feedback = 0
        secondary = 1

        if operation == "input_to_base": unit = input_unit
        elif operation == "base_to_output": unit = output_unit
        else:
            unit = 0
            print("Error with operation selection")
            return 0

        match unit_type:
            # If time units, convert to seconds
            case "Time":
                match unit:
                    case "Milliseconds": secondary = 0.001
                    case "Seconds":      secondary = 1
                    case "Minutes":      secondary = 60
                    case "Hours":        secondary = 3600
                    case "Days":         secondary = 86400
                    case "Weeks":        secondary = 604800
                    case "Years":        secondary = 31556952
                    case _: print("Error retrieving secondary var")
            # If distance units, convert to meters
            case "Distance":
                match unit:
                    case "Millimeters":  secondary = 0.001
                    case "Centimeters":  secondary = 0.01
                    case "Meters":       secondary = 1
                    case "Kilometers":   secondary = 1000
                    case "Inches":       secondary = 0.0254
                    case "Feet":         secondary = 0.3048
                    case "Yards":        secondary = 0.9144
                    case "Miles":        secondary = 1609.34
                    case _: print("Error retrieving secondary var")
            # If weight units, convert to kilograms
            case "Weight":
                match unit:
                    case "Grams":       secondary = 0.0001
                    case "Kilograms":   secondary = 1
                    case "Metric Tons": secondary = 1000
                    case "Ounces":      secondary = 0.0283
                    case "Pounds":      secondary = 0.4536
                    case "Tons":        secondary = 907.185
                    case "Tonnes":      secondary = 1016.05
                    case _: print("Error retrieving secondary var")
            # If other unit type, print error message
            case _:
                print("Error retrieving from unit_type")

        if operation == "input_to_base":
            # feedback is now base
            feedback = input_int * secondary
        elif operation == "base_to_output":
            # feedback is now output
            feedback = base / secondary
        else:
            print("Invalid Operation")
            return 0

        return feedback

    # Main function triggered when converting
    def convert(self):
        # Collect all relevant info and put them in variables for easy use
        if self.check_input():
            input_int = self.check_input()
            input_vars = self.read_inputs(input_int)
            base = self.base_conversion(input_vars, None, "input_to_base")
            output = self.base_conversion(input_vars, base, "base_to_output")

            # Round output to significant figures
            significant_figures = self.count_significant_figures(output)
            rounded_output = self.round_number(output, significant_figures)
            self.output_response(rounded_output, input_vars)

    # Function to output response to the user and history
    def output_response(self, output, input_vars):
        # Display output to the user
        self.output_entry.config(state=NORMAL)
        self.output_entry.delete(0, "end")
        self.output_entry.insert(0, output)
        self.output_entry.config(state=DISABLED)

        # Store output for history / export
        self.formatted_output = "Converted {} {} to {} {}".format(input_vars[0], input_vars[1],
                                                                   output, input_vars[2])
        self.history_list.append(self.formatted_output)
        print(self.history_list)

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
            self.dropdown_output["menu"].add_command(label=item, command=lambda value=item: self.selected_output.set(value))

        self.selected_input.set(self.current_options[1])
        self.selected_output.set(self.current_options[4])

    # Open Help window
    def to_help_window(self):
        HelpWindow(self)

class HelpWindow:
    def __init__(self, partner):
        # Options
        self.help_box = Toplevel()

        # Disable Help button
        partner.help_button.config(state=DISABLED)

        # Enable Help button when window closed
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Setup GUI Frame
        self.help_frame = Frame(self.help_box, width=300,
                                height=200)
        self.help_frame.grid()

        # Heading Label
        self.help_heading_label = Label(self.help_frame, text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        # Help Text
        help_text = "The Program is divided into lines. The first line is the input line. The dropdown menu selects " \
                    "which unit you are typing in (defaults to centimeters), and the text box allows you to enter " \
                    "the number you want to convert. \n\nThe second line is the output line. The dropdown menu selects " \
                    "which unit you are converting to, and the text box to the right is where the output is " \
                    "displayed. \n\n" \
                    "The dropdown on the third line changes the type of measurement converted (e.g. time, weight, " \
                    "distance) and the 'Convert' button converts the input to the output. You can see your history of " \
                    "conversions and export it to a file with the 'History / Export' Button. \n\n" \
                    "Note that the output will be rounded to 3dp if it is a very small number, this includes 0"
        self.help_text_label = Label(self.help_frame, text=help_text,
                                     wraplength=350, justify="left")
        self.help_text_label.grid(row=1, padx=10)

        # Close Button
        self.close_button = Button(self.help_frame, font=("Arial", "10", "bold"),
                                   text="Close Help", command=partial(self.close_help, partner))
        self.close_button.grid(row=2, padx=10, pady=10)

    # Function to close help dialogue
    def close_help(self, partner):
        # Put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


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