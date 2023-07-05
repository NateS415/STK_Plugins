import os

def generate_files():
    while True:
        main_file_path = input("Enter the path to the main AER Report file: ")

        if not os.path.exists(main_file_path):
            print("Invalid file path. Please provide a valid path to the main AER Report file.")
        else:
            break

    with open(main_file_path, 'r') as main_file:
        lines = main_file.readlines()

    # Specific variables it looks for to process the text file
    start_string = "AER reported in the object's default AER frame"
    end_string = "Section Statistics"
    no_access_string = "No Access Found"
    output_lines = []
    output_file_name = None

    # Get directory path of input file
    script_dir = os.path.dirname(os.path.abspath(main_file_path))

    for line in lines:
        if start_string in line:
            if output_file_name:
                write_output_file(os.path.join(
                    script_dir, output_file_name), output_lines)
            output_lines = [line]  # Include the start line in output
            output_file_name = line.split(start_string)[0].strip()[
                :-2]  # Modify filename here
        elif end_string in line:
            output_lines.append(line)
            output_lines.extend(
                lines[lines.index(line) + 1: lines.index(line) + 8])
            write_output_file(os.path.join(
                script_dir, output_file_name), output_lines)
            output_file_name = None
            output_lines = []
        elif output_file_name:
            if no_access_string in line:
                output_file_name = None
                output_lines = []
            else:
                output_lines.append(line)


def write_output_file(file_path, lines):
    with open(file_path + '.txt', 'w') as output_file:
        output_file.writelines(lines)


# Usage example
generate_files()
print("\nSuccesfully split AER report per satellite.\n")
