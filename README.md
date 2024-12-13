# FASTQ to FASTA Converter

This repository provides a simple Python script to convert all .fastq files in a specified folder to .fasta files. The conversion leverages the Biopython library for seamless handling of biological sequence data.

## Features

1. Automatically processes all .fastq files in a given folder.

2. Converts each file into a .fasta format.

3. Maintains the original filenames with a new .fasta extension.

## Requirements

- Python 3.7+

- Biopython library

## Installation

Clone this repository:

git clone https://github.com/your-username/fastq-to-fasta.git
cd fastq-to-fasta

Install the required Python package:

pip install biopython

## Usage

Update the folder_path variable in the script to the path of the folder containing your .fastq files.

Run the script:

python fastq_to_fasta.py

Example

Assume you have the following folder structure:

/path_to_your_folder/
  sample1.fastq
  sample2.fastq

After running the script, the folder will contain:

/path_to_your_folder/
  sample1.fastq
  sample1.fasta
  sample2.fastq
  sample2.fasta

## Notes

Ensure that the .fastq files are properly formatted to avoid errors during conversion.

The script will output the converted .fasta files in the same directory as the input .fastq files.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

