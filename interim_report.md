# Interim Report – Customer Experience Analytics for Fintech Apps

## 1. Introduction

This project focuses on analyzing customer reviews from Ethiopian mobile banking applications to understand customer satisfaction, identify recurring issues, and generate actionable business insights.

The analysis covers three Ethiopian banks:
- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The primary objective is to build a structured analytics pipeline capable of collecting, preprocessing, and analyzing Google Play Store reviews using Natural Language Processing (NLP) techniques.

---

# 2. Data Collection Methodology

Customer reviews were collected from the Google Play Store using the Python library `google-play-scraper`.

The scraping pipeline extracted the following fields:
- Review text
- Rating
- Review date
- Bank name
- Source platform

The following mobile banking applications were analyzed:
| Bank | Application |
|---|---|
| CBE | Commercial Bank of Ethiopia Mobile |
| BOA | BOA Mobile Banking |
| Dashen | Dashen Super App |

The scraping process targeted approximately 400 reviews per bank.

---

# 3. Data Preprocessing

Several preprocessing steps were performed to prepare the dataset for analysis:

- Duplicate reviews were removed
- Missing review text and ratings were dropped
- Dates were normalized into YYYY-MM-DD format
- Data was exported into a cleaned CSV format

Final cleaned dataset summary:

| Bank | Reviews |
|---|---|
| BOA | 399 |
| Dashen | 398 |
| CBE | 383 |

Total reviews collected: **1180**

---

# 4. Early Sentiment Analysis Findings

A lexicon-based sentiment analysis approach using VADER Sentiment Analyzer was applied to classify reviews into:
- Positive
- Negative
- Neutral

Initial findings indicate that:
- Dashen Bank and CBE show stronger positive sentiment distribution
- BOA exhibits comparatively higher negative sentiment
- Positive reviews frequently reference ease of use, good service, and smooth transactions
- Negative reviews commonly mention login issues, transfer delays, and OTP-related problems

Sentiment distribution summary:

| Bank | Positive | Neutral | Negative |
|---|---|---|---|
| BOA | 210 | 120 | 69 |
| CBE | 258 | 82 | 43 |
| Dashen | 266 | 79 | 53 |

---

# 5. Visualization

The following visualizations were created:
- Sentiment distribution by bank
- Rating distribution by bank

These visualizations provide an early understanding of customer perception across the three banking applications.

---

# 6. Challenges and Limitations

Some applications returned slightly fewer than the target 400 reviews due to Google Play Store review availability and scraping limitations.

Additionally:
- Some reviews contained extremely short text with limited analytical value
- User-generated text included spelling inconsistencies and mixed language usage

These limitations will be addressed further during thematic analysis and preprocessing refinement.

---

# 7. Next Steps

The remaining project tasks will focus on:
- Advanced thematic analysis using TF-IDF and keyword extraction
- Identifying recurring customer experience themes
- PostgreSQL database design and implementation
- Building stakeholder-focused visualizations
- Generating business recommendations for each bank

---

# 8. Technologies Used

- Python
- pandas
- google-play-scraper
- VADER Sentiment Analysis
- Matplotlib
- Git & GitHub
- GitHub Actions