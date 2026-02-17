from fasta_utils import reverse_complement


def gc_skew(sequence):
    skew = [0]
    for base in sequence:
        if base == 'G':
            skew.append(skew[-1] + 1)
        elif base == 'C':
            skew.append(skew[-1] - 1)
        else:
            skew.append(skew[-1])
    return skew


def find_ori(sequence, window=500):
    skew = gc_skew(sequence)
    min_val = min(skew)
    min_pos = skew.index(min_val)
    
    start = max(0, min_pos - window//2)
    end = min(len(sequence), min_pos + window//2)
    
    return sequence[start:end], min_pos


def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def find_frequent_kmers(sequence, k=9, max_mismatch=1, min_freq=3):
    kmer_counts = {}
    
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        rev_kmer = reverse_complement(kmer)
        
        matched = False
        for existing_kmer in kmer_counts:
            if hamming_distance(kmer, existing_kmer) <= max_mismatch:
                kmer_counts[existing_kmer] += 1
                matched = True
                break
            if hamming_distance(rev_kmer, existing_kmer) <= max_mismatch:
                kmer_counts[existing_kmer] += 1
                matched = True
                break
        
        if not matched:
            kmer_counts[kmer] = 1
    
    return {k: v for k, v in kmer_counts.items() if v >= min_freq}
