import re
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_to_abp_syntax(filter_rule):
    """
    Converts a given adblock filter rule into Adblock Plus (ABP) syntax.
    """
    # Handle special cases for known adblocker syntaxes
    if filter_rule.startswith("||"):
        abp_rule = filter_rule
    elif "$badfilter" in filter_rule:
        abp_rule = filter_rule.replace("$badfilter", "")
    elif filter_rule.startswith("##") or filter_rule.startswith("#@#"):
        abp_rule = filter_rule.replace("#@#", "@@##")
    else:
        abp_rule = filter_rule

    # Remove unnecessary spaces or line breaks
    abp_rule = abp_rule.strip()
    return abp_rule

def convert_filter_list_to_abp(filter_list):
    """
    Converts a list of filter rules to Adblock Plus (ABP) syntax.
    """
    abp_filter_list = [convert_to_abp_syntax(rule) for rule in filter_list]
    return abp_filter_list

def load_filter_list(file_path):
    """
    Loads a filter list from a file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        filter_list = file.readlines()
    return filter_list

def save_filter_list(filter_list, output_path):
    """
    Saves a list of filter rules to a file.
    """
    with open(output_path, 'w', encoding='utf-8') as file:
        for rule in filter_list:
            file.write(f"{rule}\n")

def select_input_file():
    """
    Prompts user to select an input filter file.
    """
    file_path = filedialog.askopenfilename(title="Select Input Filter File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if not file_path:
        messagebox.showerror("Error", "No file selected!")
        return None
    return file_path

def select_output_file():
    """
    Prompts user to select an output file location.
    """
    file_path = filedialog.asksaveasfilename(title="Save Output Filter File", defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if not file_path:
        messagebox.showerror("Error", "No file selected for output!")
        return None
    return file_path

def process_filters():
    """
    The main function that handles the file selection, conversion, and saving.
    """
    input_file = select_input_file()
    if input_file is None:
        return

    output_file = select_output_file()
    if output_file is None:
        return

    try:
        filter_list = load_filter_list(input_file)
        abp_filter_list = convert_filter_list_to_abp(filter_list)
        save_filter_list(abp_filter_list, output_file)
        messagebox.showinfo("Success", f"Filters successfully converted and saved to {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Main GUI setup
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Process filters with GUI prompts
    process_filters()
