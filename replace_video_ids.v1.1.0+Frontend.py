#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog, messagebox
import re
import os

# Function to read the replacement strings from a file
def load_replacement_strings(replacement_file, verbose=False):
    if verbose:
        print(f"Loading replacement strings from: {replacement_file}")
        
    try:
        with open(replacement_file, 'r') as file:
            # Read all lines, strip extra whitespace/newlines
            lines = [line.strip() for line in file.readlines()]
            if verbose:
                print(f"Loaded {len(lines)} replacement strings.")
            return lines
    except Exception as e:
        if verbose:
            print(f"Error loading replacement file: {str(e)}")
        raise e

# Regex pattern to find the "videoId" field in the JSON-like structure
pattern = r'("videoId":"[^"]*")'

# Function to process the input file and replace videoIds with pre-made data
def replace_video_id(input_file, output_file, replacement_strings, verbose=False):
    if verbose:
        print(f"Processing file: {input_file} and saving results to: {output_file}")

    if not os.path.exists(input_file):
        print(f"Error: The input file {input_file} does not exist.")
        return
    
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    replacement_index = 0
    total_replacements = len(replacement_strings)

    # Open output file to write modified content
    with open(output_file, 'w') as outfile:
        for line in lines:
            # Function to perform replacement for each match
            def replacement(match):
                nonlocal replacement_index
                if replacement_index < total_replacements:
                    new_string = f'"videoId":"{replacement_strings[replacement_index]}"'
                    replacement_index += 1
                    if verbose:
                        print(f"Replacing: {match.group(0)} with {new_string}")
                    return new_string
                else:
                    # If we run out of replacements, keep the original videoId
                    return match.group(0)

            # Perform the replacement on the line
            new_line = re.sub(pattern, replacement, line)
            outfile.write(new_line)

    if verbose:
        print(f"Replacement completed for {input_file}")

# Function to handle file selection and processing
def process_files(verbose=False):
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()
    replacement_file = replacement_file_entry.get()

    # Check if all fields are filled
    if not input_file or not output_file or not replacement_file:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Load replacement strings from the provided file
    try:
        replacement_strings = load_replacement_strings(replacement_file, verbose)
    except Exception as e:
        messagebox.showerror("Error", f"Error loading replacement file: {str(e)}")
        return

    # Perform the replacement and save to output file
    try:
        replace_video_id(input_file, output_file, replacement_strings, verbose)
        messagebox.showinfo("Success", f"Replacement completed and saved to {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Error processing files: {str(e)}")

# Function to browse and select input file
def browse_input_file():
    filename = filedialog.askopenfilename(title="Select Input File")
    if filename:
        input_file_entry.delete(0, tk.END)
        input_file_entry.insert(0, filename)

# Function to browse and select output file
def browse_output_file():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", title="Select Output File")
    if filename:
        output_file_entry.delete(0, tk.END)
        output_file_entry.insert(0, filename)

# Function to browse and select replacement file
def browse_replacement_file():
    filename = filedialog.askopenfilename(title="Select Replacement File")
    if filename:
        replacement_file_entry.delete(0, tk.END)
        replacement_file_entry.insert(0, filename)

# Create the main window
root = tk.Tk()
root.title("Video ID Replacer")

# Set window size
root.geometry("600x420")  # Initial window size (width x height)
root.minsize(600, 420)    # Minimum window size to prevent shrinking

# Create and place labels and entries
tk.Label(root, text="Input File:").pack(pady=10)
input_file_entry = tk.Entry(root, width=50)
input_file_entry.pack(pady=5, padx=10, fill='x', expand=True)
tk.Button(root, text="Browse", command=browse_input_file).pack(pady=5)

tk.Label(root, text="Output File:").pack(pady=10)
output_file_entry = tk.Entry(root, width=50)
output_file_entry.pack(pady=5, padx=10, fill='x', expand=True)
tk.Button(root, text="Browse", command=browse_output_file).pack(pady=5)

tk.Label(root, text="Replacement File:").pack(pady=10)
replacement_file_entry = tk.Entry(root, width=50)
replacement_file_entry.pack(pady=5, padx=10, fill='x', expand=True)
tk.Button(root, text="Browse", command=browse_replacement_file).pack(pady=5)

# Button to start processing
process_button = tk.Button(root, text="Start Processing", command=process_files)
process_button.pack(pady=20)

# Start the main loop
root.mainloop()
 
