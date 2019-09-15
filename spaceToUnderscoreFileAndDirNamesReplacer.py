#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" spaceToUnderscoreReplacer 1.0
Script to replace spaces with underscores in file and dir names.
"""

import os
import sys


def replace_spaces_with_underscores(current_dir):
    dirs_and_files = os.scandir(current_dir)

    for entry in dirs_and_files:
        # Get dir or file name
        entry_path_list = entry.path.split('/')
        entry_name = entry_path_list[len(entry_path_list) - 1]

        # Replace spaces with underscores in files' and dirs' names
        result_name = entry_name.replace(' ', '_')

        # Rename fields and folders accordingly
        os.rename(entry.path, os.path.join(current_dir, result_name))


if __name__ == '__main__':
    destination_folder = sys.argv[1]
    replace_spaces_with_underscores(destination_folder)
