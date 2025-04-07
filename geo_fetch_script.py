from Bio import Entrez

# Ask user for email
Entrez.email = input("Your email ID: ")

# Ask user for cancer type
cancer_type = input("Provide the cancer type: ")

# Ask user for number of GEO IDs to fetch
num_ids = int(input("How many GEO IDs do you want to fetch? "))

# Search GEO database
handle = Entrez.esearch(db="gds", term=cancer_type, retmax=num_ids)
record = Entrez.read(handle)
handle.close()

# Extract the list of GEO IDs
geo_ids = record["IdList"]

if geo_ids:
    print("\nGEO IDs found:")
    print(geo_ids)
    print("\nFetching details for each GEO ID...\n")

    for geo_id in geo_ids:
        try:
            handle = Entrez.esummary(db="gds", id=geo_id)
            summary = Entrez.read(handle)
            handle.close()

            geo_summary = summary[0]
            title = geo_summary.get("title", "N/A")
            organism = geo_summary.get("organism", "N/A")
            platform = geo_summary.get("platform", "N/A")
            num_samples = geo_summary.get("n_samples", "N/A")

            print(f"GEO ID: {geo_id}")
            print(f"Title: {title}")
            print(f"Organism: {organism}")
            print(f"Platform: {platform}")
            print(f"Number of samples: {num_samples}")
            print("-" * 40)

        except Exception as e:
            print(f"An error occurred for GEO ID {geo_id}: {e}")
else:
    print("No GEO IDs found.")
