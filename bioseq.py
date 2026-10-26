from Bio import SeqIO
from Bio.SeqUtils import gc_fraction


def analyze_sequence_file(filepath):
  """Reads a FASTA file and prints basic information

  for each sequence (Length, GC content, Translation).
  """
  print(f"\n--- Analyzing File: {filepath} ---\n")

  try:
    for record in SeqIO.parse(filepath, "fasta"):
      print(f"Sequence ID: {record.id}")
      print(f"Description: {record.description}")
      seq_len = len(record.seq)
      print(f"Length: {seq_len} bp")

      # Calculate GC content
      gc = gc_fraction(record.seq) * 100
      print(f"GC-content: {gc:.2f}%")

      # Translate to protein (if DNA/RNA)
      try:
        protein_seq = record.seq.translate(to_stop=True)
        print(f"Protein length (amino acids): {len(protein_seq)}")
      except Exception:
        print("Translation not possible.")

      print("-" * 40)
  except FileNotFoundError:
    print(f"File {filepath} not found. Please create a sample FASTA file.")


if __name__ == "__main__":
  # Test with a local file
  analyze_sequence_file("sample.fasta")
