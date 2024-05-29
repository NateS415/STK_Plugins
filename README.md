
TLE to Three-Line Element Converter
Overview
This Python program processes a file containing Two-Line Element (TLE) data, removes any empty lines, and converts the data into a Three-Line Element format. It appends the satellite name to the TLE data by querying the Celestrak API using the SSC (Satellite Catalog Number).

Features
Remove Empty Lines: The program cleans the input file by removing any empty lines.
Convert to Three-Line Format: It converts TLE data into the Three-Line Element format by adding the satellite name as the first line.
Satellite Name Retrieval: The program retrieves satellite names using the Celestrak API based on the SSC number.
Requirements
Python 3.x
requests library
You can install the requests library using pip:

sh
Copy code
pip install requests
Usage
1. Prepare Your Input File
Ensure your input file containing TLE data has the following format:

yaml
Copy code
1 25544U 98067A   20301.54791667  .00001225  00000-0  29612-4 0  9993
2 25544  51.6442  39.6602 0001413  83.5395  39.6476 15.49371200236068

1 40909U 15049E   20301.21555556  .00000814  00000-0  44542-4 0  9997
2 40909  51.6425 103.7727 0002200 129.3107 230.8106 15.48914815186735
2. Run the Script
Update the input and output file paths in the script:

python
Copy code
input_file = 'path/to/your/input_file.txt'
output_file = 'path/to/your/output_file.txt'
Execute the script:

sh
Copy code
python tle_converter.py
3. Check the Output
The output file will be generated with the three-line element format:

yaml
Copy code
Satellite_25544
1 25544U 98067A   20301.54791667  .00001225  00000-0  29612-4 0  9993
2 25544  51.6442  39.6602 0001413  83.5395  39.6476 15.49371200236068

Satellite_40909
1 40909U 15049E   20301.21555556  .00000814  00000-0  44542-4 0  9997
2 40909  51.6425 103.7727 0002200 129.3107 230.8106 15.48914815186735
Script Details
get_satellite_name(ssc_number)
This function queries the Celestrak API to retrieve the satellite name based on the SSC number.

process_tle_file(input_file, output_file)
This function reads the input file, removes empty lines, processes the TLE data, and writes the three-line element data to the output file.

Error Handling
The script ensures the input file contains a valid number of TLE lines (multiples of 2).
It handles API response errors and provides a placeholder name for unknown satellites.
Debugging
The script includes debugging output to display the SSC number and retrieved satellite name. If the output file is empty or not as expected, check the console output for any errors or unexpected behavior.
