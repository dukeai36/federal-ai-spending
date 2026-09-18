# Following the Federal AI Dollar

## Project Overview

This project uses USAspending data to explore where federal AI contract dollars are going, how spending has changed, which agencies drive it, who receives the money, and what the government is buying.

The goal is to tell a clear, accessible story about identifiable federal AI contracting.

## Key Findings

* Identified AI contract obligations increased from approximately $162 million in FY2020 to $384 million in FY2025, a 137% increase.
* The Department of Defense accounts for 72.9% of identified obligations.
* The top 10 recipients account for 35.2% of identified obligations.
* Many of the largest purchasing categories involve research, engineering, and technology development.

## Dataset

Source: [USAspending.gov](https://www.usaspending.gov/)

The source data consists of federal prime contract transactions returned by a search for "artificial intelligence" covering FY2020 through FY2026.

The original contract transaction file contains 2,732 rows. After cleaning, 2,726 transactions remain.

FY2026 data extends through September 4, 2026, and is incomplete. Growth comparisons therefore use FY2020 through FY2025.

## Methodology

The analysis follows five main steps:

1. Load the USAspending contract transaction data.
2. Select relevant fields, including fiscal year, obligation amount, awarding agency, recipient, transaction description, and product or service category.
3. Keep transactions whose descriptions explicitly contain "artificial intelligence," allowing spaces or hyphens between the words.
4. Calculate obligations by fiscal year, agency, recipient, and purchasing category.
5. Engineer an `agency_group` feature that separates the Department of Defense from all other agencies.

The analysis uses `federal_action_obligation` to calculate transaction level obligations, including adjustments.

Four visualizations illustrate spending growth, defense versus other agencies, top recipients, and purchasing categories.

## Repository Structure

federal-ai-spending/
├── data/
│   ├── raw/
│   └── processed/
│       └── ai_contracts_clean.csv
├── figures/
├── notebooks/
│   └── 01_eda.ipynb
├── scripts/
│   └── analysis.py
├── README.md
├── LICENSE
└── .gitignore
```

## Reproducing the Analysis

1. Clone this repository.

2. Install the required packages:

   pip install pandas matplotlib jupyter

3. Visit [USAspending.gov](https://www.usaspending.gov/), search for "artificial intelligence" across FY2020 through FY2026, and download the Contracts Prime Transactions CSV.

4. Place the file in `data/raw/` with this filename:

   `Contracts_PrimeTransactions_2026-09-07_H23M48S59_1.csv`

5. From the project folder, run:

   python scripts/analysis.py

The script performs preprocessing, exploratory analysis, feature engineering, and visualization. It also saves the cleaned dataset to `data/processed/ai_contracts_clean.csv`.

The notebook, `notebooks/01_eda.ipynb`, contains the same analysis with explanations and outputs. Generated charts are available in `figures/`.

The large raw CSV is excluded from GitHub. The cleaned dataset is included.

## Limitations and Ethical Considerations

This is not a measure of all federal AI spending. Keyword searches may miss relevant contracts or include contracts covering work beyond AI. Grants and other assistance awards are excluded. Obligations are funding commitments, not necessarily payments.

FY2026 is incomplete through September 4, 2026, so growth comparisons use FY2020–FY2025.

## Conclusion

Identifiable federal AI contracting has grown substantially, with the Department of Defense accounting for most obligations and research and development representing many of the largest purchasing categories.

## Data Source

[USAspending.gov](https://www.usaspending.gov/) U.S. Government federal spending data.
