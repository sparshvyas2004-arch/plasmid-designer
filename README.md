# Plasmid Designer

A tool to design synthetic plasmids from bacterial genome sequences using GC skew analysis.

## Usage

```bash
python3 plasmid_designer.py <input.fa> <design.txt> <output.fa>
```

Example:
```bash
python3 plasmid_designer.py pUC19.fa Design_pUC19.txt Output.fa
```

## Testing

```bash
python3 test_plasmid.py
```

## Files

- `plasmid_designer.py` - Main program
- `fasta_utils.py` - FASTA utilities
- `ori_utils.py` - ORI finding
- `plasmid_utils.py` - Plasmid assembly
- `test_plasmid.py` - Tests
