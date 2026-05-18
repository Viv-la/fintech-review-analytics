import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load cleaned reviews
df = pd.read_csv("data/processed/bank_reviews_clean.csv")

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

def classify_sentiment(text):
    score = analyzer.polarity_scores(str(text))["compound"]

    if score >= 0.05:
        label = "positive"
    elif score <= -0.05:
        label = "negative"
    else:
        label = "neutral"

    return label, score

# Apply sentiment analysis
df[["sentiment_label", "sentiment_score"]] = df["review"].apply(
    lambda x: pd.Series(classify_sentiment(x))
)

# Save output
df.to_csv("data/processed/bank_reviews_with_sentiment.csv", index=False)

print("Sentiment analysis completed successfully!")
print(df[["bank", "review", "rating", "sentiment_label", "sentiment_score"]].head())

print("\nSentiment distribution by bank:")
print(pd.crosstab(df["bank"], df["sentiment_label"]))