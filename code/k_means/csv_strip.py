import csv
import pathlib

filepath = pathlib.Path(__file__).with_name("output.csv")

data = []
cleaned_data = []

remove_idexes = {0,1,2,3,4}
drop_last_n = 3

try:    
    with filepath.open("r") as measurement:
        reader = csv.reader(measurement, delimiter=',')
        for row in reader:
            if not row:
                continue
            row = [cell.strip() for cell in row]
            retained_cells = [cell for idx, cell in enumerate(row) if idx not in remove_idexes]
            if drop_last_n:
                retained_cells = retained_cells[:-drop_last_n] if len(retained_cells) > drop_last_n else []
            cleaned_data.append(retained_cells)
            data.append(row)

except FileNotFoundError:
    print("File not found")

print(f"Original: {data[0]}\n")
print(f"Clean: {cleaned_data[0]}\n")

def get_cleaned_data(save=False, out_name="cleaned_data.csv"):
    if save:
        out_path = filepath.with_name(out_name)
        with out_path.open("w", newline='') as out_file:
            writer = csv.writer(out_file, delimiter=';')
            for row in cleaned_data:
                writer.writerow(row)
    return cleaned_data

if __name__ == "__main__":
    get_cleaned_data(save=True)
