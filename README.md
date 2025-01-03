# replace_video_ids

![replace_video_ids v1 1 0+Frontend](https://github.com/user-attachments/assets/805e776a-8266-43a1-8fe0-9e071d8eca24)


Summary of the Python Script:
This Python script replaces specific videoId values in a text file (which likely contains JSON-like data) with predefined values from another file. This is great for making a playlist logged into youtube, exporting the playlist as a ".cvs" file. Copying all the ids into a another file (additionally running the script to generate the updated playlist.db), and importing a (newly updated) template exported playlist.db from freetube app. I created the script using ChatGPT 4o mini. It can be modified to take any list of line by line data and import it into a newly generated file.

Here’s a breakdown of what each part of the script does:

Dependancies:
tkinter
python3
YouTube Advanced Playlist Export (chrome webstore)
FreeTube (application)

I haven't tested windows release yet. Appears to run (function not tested yet), If you test it please let me know of any bugs by filing a report via github. It was generated by pyinstaller.

1. Script Purpose:
The script searches for all occurrences of videoId fields in an input file.
It replaces each videoId with a corresponding string from a list of predefined replacement values stored in a separate file.
How It Works:
Input Files:

Input file: A text file containing lines with videoId values (e.g., {"videoId":"xxxxxxxxxxx"}).
Replacement file: A text file containing predefined videoId replacement values. Each line in this file represents one replacement value.
Regex Search:

The script uses the following regular expression to search for the videoId field in the input file:
regex
Copy code
"videoId":"[^"]*"
This pattern matches strings of the form "videoId":"xxxxxxxxxxx", where xxxxxxxxxxx is an alphanumeric string.
Replacing videoId:

For each occurrence of videoId in the input file, the script replaces the xxxxxxxxxxx part with a value from the replacement file.
The first replacement value from the replacement file is used for the first match, the second for the second match, and so on.
If there are more videoId fields in the input file than replacement values, the remaining videoId fields are left unchanged.
Writing the Output:

The script writes the modified content (with replaced videoId values) to an output file.
Command-Line Arguments:

The script is executed with the following arguments:
input_file: Path to the input file (containing the original videoId values).
output_file: Path where the modified content will be saved.
replacement_file: Path to the file containing the predefined replacement videoId values.

Example Usage:

python replace_video_ids.py ./playlistExp.db ./playlistExpOutput.db ./replacement_data.txt

playlistExp.db: Input file with original videoId values.
playlistExpOutput.db: Output file where the modified content will be saved.
replacement_data.txt: File containing predefined replacement videoId values.

Steps in the Script:
Load Replacement Strings: The script reads the replacement values from the replacement_data.txt file.
Process the Input File: It reads the input file line by line and uses the regex pattern to identify and replace videoId values.
Write to Output: The modified content is written to the output file.

Key Features:
Regex Search: Finds all occurrences of videoId in the input file.
Replacement Logic: Replaces each found videoId with a corresponding value from the replacement file.
Command-Line Interface: Allows users to specify file paths for the input, output, and replacement data.

Use Case:
This script is useful for bulk processing of JSON-like data where you need to update or anonymize videoId values using a list of predefined replacements.
