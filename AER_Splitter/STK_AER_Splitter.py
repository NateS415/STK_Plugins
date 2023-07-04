def generate_files(main_file_path):
    with open(main_file_path, 'r') as main_file:
        lines = main_file.readlines()

    start_string = "AER reported in the object's default AER frame"
    end_string = "Section Statistics"
    no_access_string = "No Access Found"
    output_lines = []
    output_file_name = None

    for line in lines:
        if start_string in line:
            if output_file_name:
                write_output_file(output_file_name, output_lines)
            output_lines = [line]  # Include the start line in output
            output_file_name = line.split(start_string)[0].strip()[
                :-2]  # Modify filename here
        elif end_string in line:
            output_lines.append(line)
            output_lines.extend(
                lines[lines.index(line) + 1: lines.index(line) + 8])
            write_output_file(output_file_name, output_lines)
            output_file_name = None
            output_lines = []
        elif output_file_name:
            if no_access_string in line:
                output_file_name = None
                output_lines = []
            else:
                output_lines.append(line)


def write_output_file(file_name, lines):
    with open(file_name + '.txt', 'w') as output_file:
        output_file.writelines(lines)


# Usage example
generate_files(
    'Place-White_House_DC-To-Satellite-SPACEBEE-113_52024_AER.txt')
