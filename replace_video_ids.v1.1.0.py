#!/usr/bin/env python3

import re
import argparse

# Function to read the replacement strings from a file
def load_replacement_strings(replacement_file):
    with open(replacement_file, 'r') as file:
        # Read all lines, strip extra whitespace/newlines
        return [line.strip() for line in file.readlines()]

# Regex pattern to find the "videoId" field in the JSON-like structure
pattern = r'("videoId":"[^"]*")'

# Function to process the input file and replace videoIds with pre-made data
def replace_video_id(input_file, output_file, replacement_strings):
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
                    return new_string
                else:
                    # If we run out of replacements, keep the original videoId
                    return match.group(0)

            # Perform the replacement on the line
            new_line = re.sub(pattern, replacement, line)
            outfile.write(new_line)

# Command-line argument parsing
if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Replace videoId values in a file with pre-made strings.")
    
    # Define command-line arguments
    parser.add_argument("input_file", help="Path to the input file to process")
    parser.add_argument("output_file", help="Path to the output file to save the results")
    parser.add_argument("replacement_file", help="Path to the file containing the replacement strings")

    # Parse arguments from command-line
    args = parser.parse_args()

    # Load replacement strings from the provided file
    replacement_strings = load_replacement_strings(args.replacement_file)

    # Perform the replacement in the input file and write to the output file
    replace_video_id(args.input_file, args.output_file, replacement_strings)

    print(f"Replacement completed and saved to {args.output_file}")
