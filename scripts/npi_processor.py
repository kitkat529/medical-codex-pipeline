import polars as pl
npi_file_path = "input\\npidata_pfile.csv"
npi = pl.read_csv(npi_file_path, n_rows=1000)
npi.describe()


print(f"Successfully loaded {len(npi)} records from NPI data")
print(f"Columns: {npi.columns}")
print(f"\nDataset shape: {npi.shape}")
print(f"\nFirst 5 rows:")
print(npi.head())

print(f"\nMemory usage (MB): {npi.estimated_size() / 1024**2:.2f}")

npi_small = npi.select([
    'NPI', 
    'Provider Last Name (Legal Name)'
])

npi_small = npi_small.with_columns(
    pl.lit('2025-09-17').alias('last_updated')
)

npi_small = npi_small.rename({
    'NPI': 'code',
    'Provider Last Name (Legal Name)': 'description',
    'last_updated': 'last_updated'
})
output_path = "output\\npi_small.csv"
npi_small.write_csv(output_path)