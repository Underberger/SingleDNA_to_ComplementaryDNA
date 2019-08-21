import pyperclip # needed module to copy mRNA sequence to clipboard
# User input DNA sequence
try:
    DNA_sequence = input("Please enter the DNA sequence below: \n")
except:
    print("Invalid, please enter a valid DNA sequence.")
# DNA sequence to uppercase
DNA = DNA_sequence.upper()
# add complementary base pair to every nucleotide -> AT GC
compDNA = ""
for nuc in DNA:
    if nuc == "A":
        compDNA = compDNA + "T" # adenine -> thymine
    elif nuc == "T":
        compDNA = compDNA + "A" # thymine -> adenine
    elif nuc == "G":
        compDNA = compDNA + "C" # guanine -> cytosine
    else:
        compDNA = compDNA + "G" # cytosine -> guanine

print("Success! Complementary DNA sequence copied to clipboard and shown below:\n" + compDNA) # give back the complementary DNA sequence
pyperclip.copy(compDNA) # copy complementary DNA sequence on the clipboard