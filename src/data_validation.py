import pandas as pd

DATA_PATH = "data/raw"


def load_datasets():
    candidates = pd.read_csv(f"{DATA_PATH}/candidates.csv")
    applications = pd.read_csv(f"{DATA_PATH}/applications.csv")
    jobs = pd.read_csv(f"{DATA_PATH}/jobs.csv")
    interviews = pd.read_csv(f"{DATA_PATH}/interviews.csv")
    offers = pd.read_csv(f"{DATA_PATH}/offers.csv")

    return candidates, applications, jobs, interviews, offers


def validate_datasets(
    candidates,
    applications,
    jobs,
    interviews,
    offers,
):
    print("\n" + "=" * 60)
    print("DATA VALIDATION")
    print("=" * 60)

    # 1. Missing values and duplicate rows
    datasets = {
        "Candidates": candidates,
        "Applications": applications,
        "Jobs": jobs,
        "Interviews": interviews,
        "Offers": offers,
    }

    for name, df in datasets.items():
        print("\n" + "=" * 50)
        print(name)
        print("=" * 50)

        print(f"Rows: {len(df)}")
        print(f"Columns: {len(df.columns)}")

        print("\nMissing values:")
        print(df.isnull().sum())

        print(f"\nDuplicate rows: {df.duplicated().sum()}")

    # 2. Primary key validation
    print("\n" + "=" * 50)
    print("PRIMARY KEY VALIDATION")
    print("=" * 50)

    primary_keys = {
        "Candidates": (candidates, "candidate_id"),
        "Applications": (applications, "application_id"),
        "Jobs": (jobs, "job_id"),
        "Interviews": (interviews, "interview_id"),
        "Offers": (offers, "offer_id"),
    }

    for name, (df, column) in primary_keys.items():
        duplicate_count = df[column].duplicated().sum()
        null_count = df[column].isnull().sum()

        print(
            f"{name} - {column}: "
            f"duplicates={duplicate_count}, nulls={null_count}"
        )

    # 3. Numeric validation
    print("\n" + "=" * 50)
    print("NUMERIC VALIDATION")
    print("=" * 50)

    print(
        "Candidates - negative years_experience:",
        (candidates["years_experience"] < 0).sum(),
    )

    print(
        "Applications - negative scores:",
        (applications["score"] < 0).sum(),
    )

    print(
        "Jobs - negative salary_low:",
        (jobs["salary_low"] < 0).sum(),
    )

    print(
        "Jobs - negative salary_high:",
        (jobs["salary_high"] < 0).sum(),
    )

    print(
        "Jobs - salary_low greater than salary_high:",
        (jobs["salary_low"] > jobs["salary_high"]).sum(),
    )

    print(
        "Offers - negative base_salary:",
        (offers["base_salary"] < 0).sum(),
    )

    # 4. Foreign key validation
    print("\n" + "=" * 50)
    print("FOREIGN KEY VALIDATION")
    print("=" * 50)

    invalid_candidate_ids = ~applications["candidate_id"].isin(
        candidates["candidate_id"]
    )

    invalid_job_ids = ~applications["job_id"].isin(
        jobs["job_id"]
    )

    invalid_application_interviews = ~interviews[
        "application_id"
    ].isin(applications["application_id"])

    invalid_application_offers = ~offers[
        "application_id"
    ].isin(applications["application_id"])

    print(
        "Applications with invalid candidate_id:",
        invalid_candidate_ids.sum(),
    )

    print(
        "Applications with invalid job_id:",
        invalid_job_ids.sum(),
    )

    print(
        "Interviews with invalid application_id:",
        invalid_application_interviews.sum(),
    )

    print(
        "Offers with invalid application_id:",
        invalid_application_offers.sum(),
    )

    # 5. Date validation
    print("\n" + "=" * 50)
    print("DATE VALIDATION")
    print("=" * 50)

    date_columns = [
        ("Applications", applications, "applied_at"),
        ("Jobs", jobs, "posted_at"),
        ("Interviews", interviews, "scheduled_at"),
        ("Offers", offers, "offered_at"),
        ("Offers", offers, "accepted_at"),
    ]

    for name, df, column in date_columns:
        converted_dates = pd.to_datetime(
            df[column],
            errors="coerce",
        )

        invalid_dates = (
            converted_dates.isnull() & df[column].notnull()
        ).sum()

        print(
            f"{name} - {column} invalid dates:",
            invalid_dates,
        )

    # 6. Offer validation
    print("\n" + "=" * 50)
    print("OFFER VALIDATION")
    print("=" * 50)

    accepted_without_date = (
        offers["accepted"] & offers["accepted_at"].isnull()
    ).sum()

    rejected_with_date = (
        ~offers["accepted"] & offers["accepted_at"].notnull()
    ).sum()

    print(
        "Accepted offers without accepted_at:",
        accepted_without_date,
    )

    print(
        "Rejected offers with accepted_at:",
        rejected_with_date,
    )


if __name__ == "__main__":
    (
        candidates,
        applications,
        jobs,
        interviews,
        offers,
    ) = load_datasets()

    validate_datasets(
        candidates,
        applications,
        jobs,
        interviews,
        offers,
    )