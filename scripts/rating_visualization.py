import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/processed/bank_reviews_with_sentiment.csv")

# Plot rating distribution by bank
plt.figure(figsize=(8, 5))

for bank in df["bank"].unique():
    bank_data = df[df["bank"] == bank]
    plt.hist(bank_data["rating"], alpha=0.5, label=bank)

plt.title("Rating Distribution by Bank")
plt.xlabel("Rating")
plt.ylabel("Number of Reviews")
plt.xticks([1, 2, 3, 4, 5])
plt.legend()

# Save figure
plt.savefig("data/processed/rating_distribution.png")

plt.show()