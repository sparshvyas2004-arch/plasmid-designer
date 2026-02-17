from fasta_utils import find_pattern

RESTRICTION_ENZYMES = {
    'EcoRI': 'GAATTC',
    'BamHI': 'GGATCC',
    'HindIII': 'AAGCTT',
    'PstI': 'CTGCAG',
    'SalI': 'GTCGAC',
    'SmaI': 'CCCGGG',
    'KpnI': 'GGTACC',
    'SacI': 'GAGCTC',
    'XbaI': 'TCTAGA',
    'SphI': 'GCATGC'
}

MARKERS = {
    'AmpR': (884, 1745),
    'AmpR_gene': (884, 1745),
    'lacZ': (146, 395),
    'lacZ_alpha': (146, 395),
    'ori_pMB1': (1998, 2587)
}


def parse_design(filename):
    mcs_enzymes = []
    markers = []
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            parts = [p.strip() for p in line.split(',')]
            if len(parts) == 2:
                feature, value = parts
                if 'site' in feature.lower():
                    mcs_enzymes.append(value)
                else:
                    markers.append(feature)
    
    return mcs_enzymes, markers


def build_mcs(enzymes):
    mcs = ''
    for enzyme in enzymes:
        if enzyme in RESTRICTION_ENZYMES:
            mcs += RESTRICTION_ENZYMES[enzyme]
    return mcs


def extract_markers(sequence, marker_names):
    marker_seqs = {}
    for marker in marker_names:
        if marker in MARKERS:
            start, end = MARKERS[marker]
            marker_seqs[marker] = sequence[start:end]
    return marker_seqs


def assemble_plasmid(ori_seq, marker_seqs, mcs_seq):
    plasmid = ori_seq
    
    for marker in ['AmpR', 'lacZ', 'ori_pMB1']:
        if marker in marker_seqs:
            plasmid += marker_seqs[marker]
    
    plasmid += mcs_seq
    return plasmid


def remove_sites(sequence, site):
    return sequence.replace(site, '')
