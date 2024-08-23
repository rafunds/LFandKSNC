def read_text_file(filepath):
    with open(filepath, 'r') as file:
        return [sorted(line.strip().split()) for line in file]

def compare_files(file1_path, file2_path):
    file1_rows = read_text_file(file1_path)
    file2_rows = read_text_file(file2_path)

    unmatched_in_file1 = []
    unmatched_in_file2 = set(range(len(file2_rows)))  # Assume all rows in file2 are unmatched initially

    # Find unmatched rows in file1
    for i, row1 in enumerate(file1_rows):
        match_found = False
        for j, row2 in enumerate(file2_rows):
            if j in unmatched_in_file2 and row1 == row2:
                match_found = True
                unmatched_in_file2.remove(j)  # Mark this row in file2 as matched
                break
        if not match_found:
            unmatched_in_file1.append((i + 1, row1))

    # Output unmatched rows in file1
    if unmatched_in_file1:
        print("Rows in File1 with no match in File2:")
        for row_num, row in unmatched_in_file1:
            print(f"File1 Row {row_num} -> {row}")
    else:
        print("All rows in File1 have a match in File2.")

    # Output unmatched rows in file2
    if unmatched_in_file2:
        print("\nRows in File2 with no match in File1:")
        for row_num in unmatched_in_file2:
            print(f"File2 Row {row_num + 1} -> {file2_rows[row_num]}")
    else:
        print("All rows in File2 have a match in File1.")
# Example usage
file1 = 'LF_Vrepresentation.txt'
file2 = 'OtherLF_Vrepresentation.txt'

compare_files(file1, file2)
