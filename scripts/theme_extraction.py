import pandas as pd
import re

# Load sentiment dataset
df = pd.read_csv("data/processed/bank_reviews_with_sentiment.csv")

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def identify_theme(review):
    review = clean_text(review)

    if any(word in review for word in ["login", "log in", "password", "pin", "fingerprint", "access"]):
        return "Account Access Issues"

    elif any(word in review for word in ["otp", "verification", "code", "sms"]):
        return "OTP and Verification Issues"

    elif any(word in review for word in ["transfer", "transaction", "send", "payment", "money"]):
        return "Transaction Performance"

    elif any(word in review for word in ["slow", "crash", "error", "bug", "fail", "failed", "loading", "network"]):
        return "App Reliability and Performance"

    elif any(word in review for word in ["ui", "interface", "design", "easy", "simple", "user friendly"]):
        return "User Interface and Experience"

    elif any(word in review for word in ["support", "service", "customer", "help", "call center"]):
        return "Customer Support"

    elif any(word in review for word in ["feature", "fingerprint", "update", "improve", "option"]):
        return "Feature Requests"

    else:
        return "General Feedback"

# Apply cleaning and theme classification
df["clean_review"] = df["review"].apply(clean_text)
df["identified_theme"] = df["review"].apply(identify_theme)

# Save final analyzed dataset
df.to_csv("data/processed/bank_reviews_analyzed.csv", index=False)

print("Theme extraction completed successfully!")
print("\nTheme distribution by bank:")
print(pd.crosstab(df["bank"], df["identified_theme"]))

print("\nTop themes overall:")
print(df["identified_theme"].value_counts())