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