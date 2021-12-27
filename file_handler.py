import csv
import os


class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as myfile:
                reader = csv.DictReader(myfile)
                return list(reader)
        else:
            return "path is incorrect"

    def write_file(self, info, mode="a"):
        if isinstance(info, dict):
            fields = info.keys()
            info = [info]
        elif isinstance(info, list):
            fields = info[0].keys()
        with open(self.file_path, mode=mode, newline='') as myfile:
            writer = csv.DictWriter(myfile, fieldnames=fields)
            if myfile.tell() == 0:
                writer.writeheader()
            writer.writerows(info)

    def edit_row(self, key, new_info, row_num):
        all_rows = self.read_file()
        final_rows = []
        for i in range(len(all_rows)):
            if i == row_num:
                all_rows[i][key] = new_info
            final_rows.append(all_rows[i])
        self.write_file(final_rows, mode="w")

    def delete_row(self, row_num):
        all_rows = self.read_file()
        final_rows = []
        for i in range(len(all_rows)):
            if i == row_num:
                continue
            final_rows.append(all_rows[i])
        self.write_file(final_rows, mode="w")

