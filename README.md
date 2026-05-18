# Fintech Review Analytics

## Project Overview
This project analyzes customer reviews from Ethiopian fintech mobile banking applications using Natural Language Processing (NLP) techniques.

The analysis focuses on:
- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The goal is to extract customer sentiment, identify recurring themes, and generate business recommendations for improving customer experience.

---

## Task 1: Data Collection and Preprocessing

### Data Source
Reviews were scraped from the Google Play Store using the `google-play-scraper` Python library.

### Fields Collected
The following fields were collected:
- Review Text
- Rating
- Review Date
- Bank Name
- Source

### Data Cleaning
The preprocessing pipeline included:
- Removing duplicate reviews
- Dropping missing review text or ratings
- Normalizing dates to YYYY-MM-DD format

### Dataset Summary
A total of 1180 cleaned reviews were collected:
- CBE: 383 reviews
- BOA: 399 reviews
- Dashen: 398 reviews

### Limitation
Some applications returned fewer than 400 reviews due to Google Play Store scraping limitations and review availability.

---

## Technologies Used
- Python
- pandas
- google-play-scraper
- Git & GitHub
- GitHub Actions

---

## Project Structure

```text
fintech-review-analytics/
├── data/
├── notebooks/
├── scripts/
├── src/
├── tests/
└── .github/

## Project Workflow

This project implements an end-to-end customer experience analytics pipeline:

1. Scrape Google Play Store reviews for three Ethiopian banking apps
2. Clean and preprocess review data
3. Perform sentiment analysis using VADER
4. Extract recurring customer experience themes
5. Store processed review data in PostgreSQL
6. Generate visualizations and business recommendations

## Key Outputs

- Cleaned review dataset
- Sentiment analysis results
- Theme classification results
- PostgreSQL database schema
- Dashboard visualizations
- Final insights and recommendations

## Main Scripts

| Script | Purpose |
|---|---|
| `scripts/scrape_reviews.py` | Scrapes and preprocesses Google Play reviews |
| `scripts/sentiment_analysis.py` | Performs sentiment analysis |
| `scripts/theme_extraction.py` | Identifies recurring review themes |
| `scripts/visualize_sentiment.py` | Generates sentiment distribution chart |
| `scripts/rating_visualization.py` | Generates rating distribution chart |
| `scripts/theme_visualization.py` | Generates theme frequency chart |
| `scripts/database_insert.py` | Inserts processed data into PostgreSQL |

## Database

The PostgreSQL database is named `bank_reviews` and contains two tables:

- `banks`
- `reviews`

The schema is available in:

```text
database/schema.sql