import pandas as pd

DATA_PATH = "data/raw"


def load_datasets():
    candidates = pd.read_csv(f"{DATA_PATH}/candidates.csv")
    applications = pd.read_csv(f"{DATA_PATH}/applications.csv")
    jobs = pd.read_csv(f"{DATA_PATH}/jobs.csv")
    interviews = pd.read_csv(f"{DATA_PATH}/interviews.csv")
    offers = pd.read_csv(f"{DATA_PATH}/offers.csv")

    return candidates, applications, jobs, interviews, offers


def clean_datasets():
    candidates, applications, jobs, interviews, offers = load_datasets()

    # Convert timestamp columns to datetime
    applications["applied_at"] = pd.to_datetime(
        applications["applied_at"], errors="coerce"
    )

    jobs["posted_at"] = pd.to_datetime(
        jobs["posted_at"], errors="coerce"
    )

    interviews["scheduled_at"] = pd.to_datetime(
        interviews["scheduled_at"], errors="coerce"
    )

    offers["offered_at"] = pd.to_datetime(
        offers["offered_at"], errors="coerce"
    )

    offers["accepted_at"] = pd.to_datetime(
        offers["accepted_at"], errors="coerce"
    )

    # Remove completely duplicated rows
    candidates = candidates.drop_duplicates()
    applications = applications.drop_duplicates()
    jobs = jobs.drop_duplicates()
    interviews = interviews.drop_duplicates()
    offers = offers.drop_duplicates()

    return candidates, applications, jobs, interviews, offers


def validate_datasets(datasets):
    for name, df in datasets.items():
        print("\n" + "=" * 50)
        print(name)
        print("=" * 50)

        print(f"Rows: {df.shape[0]}")
        print(f"Columns: {df.shape[1]}")

        print("\nMissing values:")
        print(df.isnull().sum())

        print(f"\nDuplicate rows: {df.duplicated().sum()}")

        print("\nData types:")
        print(df.dtypes)

        print("\nInvalid datetime values:")
        datetime_columns = df.select_dtypes(
            include=["datetime"]
        ).columns

        if len(datetime_columns) == 0:
            print("No datetime columns.")
        else:
            for column in datetime_columns:
                print(f"{column}: {df[column].isna().sum()} missing/invalid")


if __name__ == "__main__":
    (
        candidates,
        applications,
        jobs,
        interviews,
        offers,
    ) = clean_datasets()

    datasets = {
        "Candidates": candidates,
        "Applications": applications,
        "Jobs": jobs,
        "Interviews": interviews,
        "Offers": offers,
    }

    validate_datasets(datasets)