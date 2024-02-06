import pandas as pd


def to_matrix(csv):
    csv_path = csv.get()
    try:
        if csv_path:
            print("CSV Loaded:")
            return get_matrix(pd.read_csv(csv_path, delimiter=';'))
        else:
            print("Please select a CSV file.")
            return None  # Return None to indicate that no CSV file was loaded
    except pd.errors.EmptyDataError:
        print("The selected CSV file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error parsing the CSV file. Please check the file format.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def get_matrix(dataset):
    x = []
    values = []
    [values.append(float(v)) for v in dataset.columns]
    x.append(values)
    [x.append(list(row)) for row in dataset.values]
    return x
