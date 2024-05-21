# Liberary
import csv

def txt2csv():
    # Define the input and output file paths
    input_file_path = 'data/AGL_001.TXT'
    output_file_path = 'date.csv'

    # Read the content of the text file
    with open(input_file_path, 'r') as txt_file:
        lines = txt_file.readlines()

    # Write the content to a csv file
    with open(output_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Write the header
        header = lines[0].strip().split('\t')
        csv_writer.writerow(header)
        
        # Write the data rows
        for line in lines[1:]:
            row = line.strip().split('\t')
            csv_writer.writerow(row)

    print(f"Data successfully converted to {output_file_path}")
