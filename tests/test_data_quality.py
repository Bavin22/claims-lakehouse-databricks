from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

def test_claim_id_not_null():
    df = spark.table("dev.claims_project.silver_claims")
    assert df.filter("ClaimID IS NULL").count() == 0

def test_claim_amount_not_negative():
    df = spark.table("dev.claims_project.silver_claims")
    assert df.filter("ClaimAmount < 0").count() == 0

def test_no_duplicate_claim_ids():
    df = spark.sql("""
        SELECT ClaimID
        FROM dev.claims_project.silver_claims
        GROUP BY ClaimID
        HAVING COUNT(*) > 1
    """)
    assert df.count() == 0

def test_suspicion_score_valid_range():
    df = spark.table("dev.claims_project.gold_suspicious_claims")
    assert df.filter("suspicion_score < 0 OR suspicion_score > 5").count() == 0

def test_paid_date_after_claim_date():
    df = spark.table("dev.claims_project.silver_claims")
    assert df.filter("paid_date < ClaimDate").count() == 0

def test_claim_received_after_claim_date():
    df = spark.table("dev.claims_project.silver_claims")
    assert df.filter("claim_received_date < ClaimDate").count() == 0

def test_valid_claim_status():
    df = spark.table("dev.claims_project.silver_claims")
    assert df.filter("""ClaimStatus NOT IN ('APPROVED', 'PENDING', 'REJECTED')""").count() == 0

def test_claim_date_not_future():
    df = spark.table("dev.claims_project.silver_claims")
    assert df.filter("ClaimDate > current_date()").count() == 0

def test_provider_id_not_null():
    df = spark.table("dev.claims_project.silver_claims")
    assert df.filter("ProviderID IS NULL").count() == 0

def test_patient_id_not_null():
    df = spark.table("dev.claims_project.silver_claims")
    assert df.filter("PatientID IS NULL").count() == 0
