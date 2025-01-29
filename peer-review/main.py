import os
import pandas as pd
import sys
from config import *


def read_excel_sheets(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Filter only Excel files (assuming all files in the folder are Excel files)
    excel_files = [file for file in files if file.endswith('.xlsx') or file.endswith('.xls')]

    # Create an empty DataFrame to store the combined data
    combined_data = pd.DataFrame()

    # Loop through each Excel file and read each sheet
    for file in excel_files:
        file_path = os.path.join(folder_path, file)

        # Read all sheets from the Excel file, starting from the second row
        try:
            sheet = pd.read_excel(file_path, skiprows=1, header=None)
        except Exception as e:
            logging.info(f"Error reading file {file}: {e}")
            continue

        # Extract relevant information
        name_and_last_name = sheet.iloc[::2, 2].ffill().reset_index(drop=True)
        id_number = sheet.iloc[1::2, 2].ffill().reset_index(drop=True)

        # Extract grade columns
        grades = sheet.iloc[::2, 3:].reset_index(drop=True)

        # Combine extracted information into a new DataFrame
        extracted_data = pd.DataFrame({
            'Name': name_and_last_name,
            'ID': id_number
        })

        # Concatenate the extracted data with the grades
        extracted_data = pd.concat([extracted_data, grades], axis=1)

        # Drop rows with NaN values
        extracted_data = extracted_data.dropna()

        # Append the extracted data to the combined_data DataFrame
        combined_data = pd.concat([combined_data, extracted_data], ignore_index=True)

    return combined_data


if __name__ == "__main__":
    # Check if the folder path is provided as a command-line argument
    if len(sys.argv) != 2:
        logging.info("Usage: python script.py /path/to/your/excel/files")
        sys.exit(1)

    # Get the folder path from the command-line argument
    folder_path = sys.argv[1]

    # Call the function with the provided folder path
    result = read_excel_sheets(folder_path)

    logging.info(result)

    # Group by 'ID' and aggregate using majority voting for grade columns
    # and concatenate the text in column 8
    def majority_vote(series):
        mode_value = series.mode().iloc[0] if not series.mode().empty else None
        return mode_value

    def average(series):
        return series.mean()

    def concatenate_text(series):
        return ', '.join(series.dropna().astype(str))

    agg_functions = {
        3: [majority_vote, average],
        4: [majority_vote, average],
        5: [majority_vote, average],
        6: [majority_vote, average],
        7: [majority_vote, average],
        8: concatenate_text,
        'Name': 'first',  # Assuming 'Name' is the same for all rows with the same 'ID'
    }

    # Group by 'ID' and perform aggregation
    grouped_data = result.groupby('ID').agg(agg_functions).reset_index()

    grouped_data.columns = [f"{col[0]}_{col[1]}" if isinstance(col, tuple) else col for col in grouped_data.columns]

    # Calculate the final score using both majority voting and average on columns 3 to 7
    vote_columns = ['3_majority_vote', '4_majority_vote', '5_majority_vote', '6_majority_vote', '7_majority_vote']
    avg_columns = ['3_average', '4_average', '5_average', '6_average', '7_average']

    # Majority Vote
    grouped_data['Final_Score_Majority'] = grouped_data[vote_columns].mode(axis=1, dropna=True).iloc[:, 0]

    # Average
    grouped_data['Final_Score_Average'] = grouped_data[avg_columns].mean(axis=1)

    # Get the directory of the script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Export the grouped data with both final scores to a new Excel file in the script's directory
    output_file_path = os.path.join(script_directory, 'grouped_data_with_final_scores.xlsx')
    grouped_data.to_excel(output_file_path, index=False)
    
    logging.info(f"Grouped data with final scores exported to: {output_file_path}")