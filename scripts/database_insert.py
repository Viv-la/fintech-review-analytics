import pandas as pd
from sqlalchemy import create_engine, text

# Load analyzed dataset
df = pd.read_csv("data/processed/bank_reviews_analyzed.csv")

# Update these details based on your PostgreSQL setup
DB_USER = "postgres"
DB_PASSWORD = "Mumqueen123!"
DB_HOST = "localhost"
DB_PORT = "5433"
DB_NAME = "bank_reviews"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

with engine.begin() as conn:
    # Create tables
    with open("database/schema.sql", "r") as file:
        conn.execute(text(file.read()))

    # Insert banks
    banks = {
        "CBE": "Commercial Bank of Ethiopia Mobile",
        "BOA": "BOA Mobile Banking",
        "Dashen": "Dashen Super App"
    }

    for bank_name, app_name in banks.items():
        conn.execute(
            text("""
                INSERT INTO banks (bank_name, app_name)
                VALUES (:bank_name, :app_name)
                ON CONFLICT DO NOTHING;
            """),
            {"bank_name": bank_name, "app_name": app_name}
        )

    # Get bank IDs
    bank_ids = pd.read_sql("SELECT bank_id, bank_name FROM banks", conn)
    bank_map = dict(zip(bank_ids["bank_name"], bank_ids["bank_id"]))

    # Prepare review data
    df["bank_id"] = df["bank"].map(bank_map)

    review_df = df[[
        "bank_id",
        "review",
        "rating",
        "date",
        "sentiment_label",
        "sentiment_score",
        "identified_theme",
        "source"
    ]].rename(columns={
        "review": "review_text",
        "date": "review_date"
    })

    review_df.to_sql("reviews", conn, if_exists="append", index=False)

print("Data inserted into PostgreSQL successfully!")