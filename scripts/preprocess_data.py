import os
from Bio import SeqIO

def preprocess_fasta(file_path, output_dir):
    """Preprocess raw FASTA data by removing unwanted sequences and saving clean data."""
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Open output file for cleaned sequences
    cleaned_fasta_path = os.path.join(output_dir, 'cleaned_sequences.fasta')
    
    with open(file_path, "r") as fasta_file, open(cleaned_fasta_path, "w") as output_file:
        for record in SeqIO.parse(fasta_file, "fasta"):
            # Example preprocessing: Only keep sequences longer than 100 nucleotides
            if len(record.seq) > 100:
                SeqIO.write(record, output_file, "fasta")
    
    print(f"Processed sequences saved to {cleaned_fasta_path}")

if __name__ == "__main__":
    input_file = "data/raw/ebola_sequences.fasta"  # Example file path
    output_directory = "data/processed"
    preprocess_fasta(input_file, output_directory)
