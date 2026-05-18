import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/processed/bank_reviews_with_sentiment.csv")

# Count sentiments by bank
sentiment_counts = pd.crosstab(df["bank"], df["sentiment_label"])

# Plot
sentiment_counts.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Sentiment Distribution by Bank")
plt.xlabel("Bank")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=0)

# Save figure
plt.savefig("data/processed/sentiment_distribution.png")

plt.show()