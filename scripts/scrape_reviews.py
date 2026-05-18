from google_play_scraper import reviews
import pandas as pd

# App IDs for Ethiopian Banks
apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []

# Loop through each bank app
for bank, app_id in apps.items():

    print(f"Scraping reviews for {bank}...")

    result, continuation_token = reviews(
        app_id,
        lang='en',
        country='et',
        count=400
    )

    # Extract required fields
    for review in result:
        all_reviews.append({
            "review": review["content"],
            "rating": review["score"],
            "date": review["at"].strftime("%Y-%m-%d"),
            "bank": bank,
            "source": "Google Play"
        })

# Convert to DataFrame
df = pd.DataFrame(all_reviews)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove missing values
df.dropna(subset=["review", "rating"], inplace=True)

# Save cleaned dataset
df.to_csv("data/processed/bank_reviews_clean.csv", index=False)

print("Scraping and preprocessing completed successfully!")
print(df.head())