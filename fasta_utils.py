def read_fasta(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    header = lines[0].strip()[1:]
    sequence = ''.join(line.strip() for line in lines[1:]).upper()
    return header, sequence


def write_fasta(filename, header, sequence):
    with open(filename, 'w') as f:
        f.write(f'>{header}\n')
        for i in range(0, len(sequence), 70):
            f.write(sequence[i:i+70] + '\n')


def reverse_complement(seq):
    comp = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(comp.get(b, b) for b in reversed(seq))


def find_pattern(sequence, pattern):
    positions = []
    for i in range(len(sequence) - len(pattern) + 1):
        if sequence[i:i+len(pattern)] == pattern:
            positions.append(i)
    return positions
