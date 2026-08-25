import pandas as pd


DATA_PATH = "data/raw"


def load_datasets():
    candidates = pd.read_csv(f"{DATA_PATH}/candidates.csv")
    applications = pd.read_csv(f"{DATA_PATH}/applications.csv")
    jobs = pd.read_csv(f"{DATA_PATH}/jobs.csv")
    interviews = pd.read_csv(f"{DATA_PATH}/interviews.csv")
    offers = pd.read_csv(f"{DATA_PATH}/offers.csv")

    return candidates, applications, jobs, interviews, offers


if __name__ == "__main__":
    candidates, applications, jobs, interviews, offers = load_datasets()

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

        print(f"Rows: {df.shape[0]}")
        print(f"Columns: {df.shape[1]}")

        print("\nColumn names:")
        print(df.columns.tolist())

        print("\nData types:")
        print(df.dtypes)

        print("\nMissing values:")
        print(df.isnull().sum())

        print(f"\nDuplicate rows: {df.duplicated().sum()}")

        print("\nFirst 5 rows:")
        print(df.head())