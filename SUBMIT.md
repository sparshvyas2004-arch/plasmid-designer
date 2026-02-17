# GitHub Submission Instructions

## Files Ready for Submission ✅

All files in this folder are ready to upload to GitHub.

## Quick Submission Steps

### 1. Create GitHub Repository
- Go to https://github.com/new
- Repository name: `plasmid-designer` (or any name you prefer)
- Make it **Public**
- Don't initialize with README (you already have one)
- Click "Create repository"

### 2. Upload from This Folder

```bash
cd "/Users/sparshvyas/Downloads/bioinfo assignment/github-submission"

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Plasmid designer with GC skew ORI finding"

# Connect to your repo (replace USERNAME and REPO)
git remote add origin https://github.com/USERNAME/REPO.git

# Push
git branch -M main
git push -u origin main
```

### 3. Submit the Link

Submit your repository URL:
```
https://github.com/USERNAME/REPO
```

## Files Included

- **plasmid_designer.py** - Main program
- **fasta_utils.py** - FASTA file utilities
- **ori_utils.py** - ORI finding algorithms
- **plasmid_utils.py** - Plasmid assembly
- **test_plasmid.py** - Test suite
- **README.md** - Documentation
- **pUC19.fa** - Test input
- **Design_pUC19.txt** - Design specification
- **Output.fa** - Expected output
- **markers.tab** - Marker reference

## Quick Test

```bash
python3 plasmid_designer.py pUC19.fa Design_pUC19.txt Output.fa
python3 test_plasmid.py
```

Should show EcoRI sites: 0 ✅
