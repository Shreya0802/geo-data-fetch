# geo-data-fetch
python script to fetch and summarize GEO datasets using Entrez
# GEO Data Fetch Script 🧬

This Python script uses **Biopython's Entrez module** to fetch GEO dataset information from NCBI.

## 🔍 What it does:
- Takes user input for:
  - Email ID (for NCBI access)
  - Cancer type or disease keyword
- Searches the GEO database (GDS)
- Returns top 10/50 GEO IDs
- Fetches and prints summary info:
  - Title
  - Organism
  - Platform
  - Number of samples

## 🚀 Example Usage:
```python
Your email ID: youremail@example.com  
Provide the cancer type: breast cancer  
