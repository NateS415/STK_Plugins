import requests


def get_satellite_name(ssc_number):
    """
    Retrieve the satellite name from the Celestrak API using the SSC number.
    """
    url = f"https://celestrak.com/NORAD/elements/gp.php?CATNR={ssc_number}"
    response = requests.get(url)

    if response.status_code == 200:
        lines = response.text.strip().split('\n')
        if len(lines) >= 3:
            # The first line contains the satellite name
            return lines[0].strip()
        else:
            return f"Unknown_Satellite_{ssc_number}"
    else:
        return f"Unknown_Satellite_{ssc_number}"


def process_tle_file(input_file, output_file):
    """
    Process the input TLE file, remove empty lines, and convert to the 3-line element format.
    """
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # Remove empty lines
    lines = [line.strip() for line in lines if line.strip()]

    if len(lines) % 2 != 0:
        raise ValueError(
            "Input file does not contain a valid number of TLE lines (should be multiples of 2).")

    with open(output_file, 'w') as outfile:
        for i in range(0, len(lines), 2):
            line1 = lines[i]
            line2 = lines[i+1]

            # Extract the SSC number from line1 (assuming it is the 3rd to 7th character)
            ssc_number = line1[2:7].strip()

            # Get the satellite name
            satellite_name = get_satellite_name(ssc_number)

            # Write the three-line element data
            outfile.write(f"{satellite_name}\n")
            outfile.write(f"{line1}\n")
            outfile.write(f"{line2}\n")


# Specify the input and output file paths
input_file = 'Two_Line_El_to_Three/Roof_Test_5hrs_TLE.txt'
output_file = 'Two_Line_El_to_Three/Roof_Test_5hrs_ThreeLineElement.txt'

# Process the TLE file
process_tle_file(input_file, output_file)
