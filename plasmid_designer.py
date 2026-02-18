#!/usr/bin/env python3

import sys
from fasta_utils import read_fasta, write_fasta
from ori_utils import find_ori
from plasmid_utils import parse_design, build_mcs, extract_markers, assemble_plasmid, remove_sites, RESTRICTION_ENZYMES


def main():
    if len(sys.argv) < 4:
        print("Usage: python3 plasmid_designer.py <input.fa> <design.txt> <output.fa>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    design_file = sys.argv[2]
    output_file = sys.argv[3]
    

    header, sequence = read_fasta(input_file)
    
   
    ori_seq, ori_pos = find_ori(sequence)
    
    
   
    mcs_enzymes, markers = parse_design(design_file)
    
    
    marker_seqs = extract_markers(sequence, markers)
    
    
    mcs_enzymes_filtered = [e for e in mcs_enzymes if e != 'EcoRI']
    mcs_seq = build_mcs(mcs_enzymes_filtered)
    
    
    plasmid = assemble_plasmid(ori_seq, marker_seqs, mcs_seq)
    
    
    if 'EcoRI' in RESTRICTION_ENZYMES:
        plasmid = remove_sites(plasmid, RESTRICTION_ENZYMES['EcoRI'])
    
    
    write_fasta(output_file, "Designed_Plasmid", plasmid)
    
    print(f"\n Plasmid size: {len(plasmid)} bp")
    print(f"EcoRI sites in output: {plasmid.count('GAATTC')}")


if __name__ == "__main__":
    main()
