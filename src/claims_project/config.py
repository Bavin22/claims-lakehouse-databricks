CATALOG = "dev"
SCHEMA = "claims_project"

RAW_PATH = "/Volumes/dev/claims_project/raw"
CHECKPOINT_PATH = "/Volumes/dev/claims_project/checkpoints"

TABLES = {
    "bronze_claims": "dev.claims_project.bronze_claims",
    "bronze_providers": "dev.claims_project.bronze_providers",
    "silver_claims": "dev.claims_project.silver_claims",
    "silver_providers": "dev.claims_project.silver_providers",
    "silver_claims_enriched": "dev.claims_project.silver_claims_enriched",
    "gold_provider_monthly": "dev.claims_project.gold_provider_monthly",
    "gold_claim_lag": "dev.claims_project.gold_claim_lag",
    "gold_suspicious_claims": "dev.claims_project.gold_suspicious_claims",
}