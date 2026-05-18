import pandas as pd
import matplotlib.pyplot as plt

# Load analyzed dataset
df = pd.read_csv("data/processed/bank_reviews_analyzed.csv")

# Count themes by bank
theme_counts = pd.crosstab(df["identified_theme"], df["bank"])

# Plot
theme_counts.plot(
    kind="barh",
    figsize=(10, 6)
)

plt.title("Theme Frequency by Bank")
plt.xlabel("Number of Reviews")
plt.ylabel("Identified Theme")
plt.tight_layout()

# Save chart
plt.savefig("data/processed/theme_frequency_by_bank.png")

plt.show()