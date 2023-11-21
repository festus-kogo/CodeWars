# https://www.codewars.com/kata/5556282156230d0e5e000089/train/python
# DNA to RNA Conversion

def dna_to_rna(dna):
    
    rna = []
    
    for i, l in enumerate(dna):
        if l == 'G':
            rna.append(l)
        elif l == 'C':
            rna.append(l)
        elif l == 'A':
            rna.append(l)
        elif l == 'T':
            rna.append('U')
            
    return ''.join(rna)

print(dna_to_rna("TTTT"))
print(dna_to_rna("GCAT"))
print(dna_to_rna("GACCGCCGCC"))