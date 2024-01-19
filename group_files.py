import os
import datetime
import csv
import shutil

def get_file_info(filepath):
    """
    Retrieve information about a file.
    Args:
        filepath (str): Path to the file.

    Returns:
        dict: Information about the file including filename, modification time, and size.
    """
    stats = os.stat(filepath)
    return {
        "filename": os.path.basename(filepath),
        "modification_time": datetime.datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
        "size": stats.st_size
    }

def save_to_csv(data, filename="file_info.csv"):
    """
    Save collected data to a CSV file.
    Args:
        data (list): List of dictionaries containing file information.
        filename (str): Name of the CSV file to save the data.
    """
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['filename', 'modification_time', 'size', 'group']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for entry in data:
            writer.writerow(entry)

def main():
    directory = 'timelaps'
    file_infos = []
    current_group = 1
    last_mod_time = None

    # Process all JPG files in the directory
    for file in sorted(os.listdir(directory)):
        if file.lower().endswith('.jpg'):
            filepath = os.path.join(directory, file)
            info = get_file_info(filepath)

            # Assign a group number based on modification time
            if last_mod_time is not None:
                current_mod_time = datetime.datetime.strptime(info['modification_time'], '%Y-%m-%d %H:%M:%S')
                if (current_mod_time - last_mod_time).total_seconds() > 3:
                    current_group += 1
            info['group'] = current_group
            last_mod_time = datetime.datetime.strptime(info['modification_time'], '%Y-%m-%d %H:%M:%S')

            # Create a directory for the group and copy the file into it
            group_directory = os.path.join(directory, f"group_{current_group}")
            if not os.path.exists(group_directory):
                os.makedirs(group_directory)
            shutil.copy2(filepath, group_directory)

            file_infos.append(info)

    # Save the file information to a CSV file
    save_to_csv(file_infos)
    print("File information has been saved to file_info.csv")

if __name__ == "__main__":
    main()
