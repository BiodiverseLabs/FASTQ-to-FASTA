import os
from Bio import SeqIO

def convert_fastq_to_fasta(folder_path):
    """
    Converts all .fastq files in the given folder to .fasta files.

    Parameters:
        folder_path (str): Path to the folder containing .fastq files.
    """
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    # Get all .fastq files in the folder
    fastq_files = [f for f in os.listdir(folder_path) if f.endswith(".fastq")]

    if not fastq_files:
        print("No .fastq files found in the folder.")
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
    # Change this to the path of your working folder
    folder_path = "./path_to_your_folder"
    convert_fastq_to_fasta(folder_path)
