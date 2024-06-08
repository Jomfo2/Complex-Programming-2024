# Function to round input to 2dp
def round_number(num, sfs):
    if sfs < 6:
        num_rounded = round(num, sfs) # Round input to 2dp
    else:
        num_rounded = round(num, 6)  # Round input to 2dp
    return num_rounded

# Function to count significant figures in a number
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

i = 0
while i < 10:
    number = float(input("Input number: "))
    sfs = count_significant_figures(number)
    rounded = round_number(number, sfs)
    print(rounded)
    i += 1