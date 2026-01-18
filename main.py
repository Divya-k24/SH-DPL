from ingestion.ingest import load_data
from processing.noise_filter import remove_duplicates
from processing.self_healing import heal_missing_values
from processing.correlation import correlate
from aiops.anomaly_model import confidence_score

df = load_data('data/logs.csv')
df = remove_duplicates(df)
df = heal_missing_values(df)
df = correlate(df)
df = confidence_score(df)

print(df)
