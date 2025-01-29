import pandas as pd

# File paths
input_csv_path = "input.csv"
excel_file_path = "grouped_data_with_final_scores.xlsx"
output_csv_path = "final.csv"

# Load input CSV (no header assumed, using column indices)
input_df = pd.read_csv(input_csv_path, header=None)

# Load Excel file
excel_df = pd.read_excel(excel_file_path)

# Column indices
STUDENT_ID_COL = 55  # Adjust based on input.csv, column 55 (zero-based index 54)
START_COL = 39       # Adjust based on input structure, starting column for inserting data

# Columns in the Excel file to map
excel_columns = [
    "3_majority_vote", "3_average", 
    "4_majority_vote", "4_average", 
    "5_majority_vote", "5_average", 
    "6_majority_vote", "6_average", 
    "7_majority_vote", "7_average", 
    "8_concatenate_text"  # Comments
]

# Use the first column of the Excel file as the key for mapping, cast to string
first_column_name = excel_df.columns[0]
excel_mapping = excel_df.set_index(first_column_name)[excel_columns].to_dict(orient="index")

# Ensure all keys in excel_mapping are strings
excel_mapping = {str(k): v for k, v in excel_mapping.items()}

# Update the input DataFrame with data from the Excel file
for index, row in input_df.iterrows():
    student_id = str(row[STUDENT_ID_COL])  # Cast student_id to string
    if student_id in excel_mapping:
        print(1)
        for col_offset, col_name in enumerate(excel_columns):
            input_df.at[index, START_COL + col_offset] = excel_mapping[student_id][col_name]

# Save the updated DataFrame to final.csv
input_df.to_csv(output_csv_path, index=False, header=False)

print(f"Updated file saved as {output_csv_path}")
