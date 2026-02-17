#!/usr/bin/env python3

from fasta_utils import read_fasta
from plasmid_utils import RESTRICTION_ENZYMES


def test_plasmid(output_file):
    
    
    header, sequence = read_fasta(output_file)
    
    # Test 1: Size check
    
    size = len(sequence)
    if 2000 <= size <= 3000:
        print(f"  ✓ PASS: {size} bp (expected 2000-3000)")
    else:
        print(f"  ✗ FAIL: {size} bp (expected 2000-3000)")
    
    # Test 2: EcoRI removal
   
    ecori_count = sequence.count('GAATTC')
    if ecori_count == 0:
        print(f"  ✓ PASS: No EcoRI sites found")
    else:
        print(f"  ✗ FAIL: Found {ecori_count} EcoRI sites")
    
    # Test 3: Restriction sites
    
    expected_sites = ['BamHI', 'HindIII', 'PstI', 'SphI', 'SalI', 'XbaI', 'KpnI', 'SacI', 'SmaI']
    all_present = True
    for enzyme in expected_sites:
        site = RESTRICTION_ENZYMES[enzyme]
        count = sequence.count(site)
        if count > 0:
            print(f"  ✓ {enzyme}: {count}")
        else:
            print(f"  ✗ {enzyme}: missing")
            all_present = False
    
    if all_present:
        print("  ✓ PASS: All sites present")
    else:
        print("  ✗ FAIL: Some sites missing")
    
    # Test 4: Valid DNA
    
    valid_bases = set('ATGC')
    sequence_bases = set(sequence)
    if sequence_bases.issubset(valid_bases):
        print(f"  ✓ PASS: Valid DNA bases only")
    else:
        invalid = sequence_bases - valid_bases
        print(f"  ✗ FAIL: Invalid bases found: {invalid}")
    
    print("\n" + "="*50)
    if ecori_count == 0 and 2000 <= size <= 3000 and all_present:
        print("All tests PASSED!")
    else:
        print("Some tests FAILED!")


if __name__ == "__main__":
    test_plasmid("Output.fa")
