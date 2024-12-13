import os
from Bio import SeqIO

def convert_fastq_to_fasta():
    """
    Converts all .fastq files in the current working directory to .fasta files.
    """
    # Get the current working directory
    folder_path = os.getcwd()

    # Get all .fastq files in the folder
    fastq_files = [f for f in os.listdir(folder_path) if f.endswith(".fastq")]

    if not fastq_files:
        print("No .fastq files found in the current working directory.")
        return

    for fastq_file in fastq_files:
        input_path = os.path.join(folder_path, fastq_file)
        output_path = os.path.join(folder_path, os.path.splitext(fastq_file)[0] + ".fasta")

        try:
            # Convert FASTQ to FASTA
            with open(input_path, "r") as input_handle, open(output_path, "w") as output_handle:
                SeqIO.convert(input_handle, "fastq", output_handle, "fasta")

            print(f"Converted: {fastq_file} -> {os.path.basename(output_path)}")
        except Exception as e:
            print(f"Error converting {fastq_file}: {e}")

if __name__ == "__main__":
    convert_fastq_to_fasta()


if __name__ == "__main__":
    # Change this to the path of your working folder
    folder_path = "./path_to_your_folder"
    convert_fastq_to_fasta(folder_path)
