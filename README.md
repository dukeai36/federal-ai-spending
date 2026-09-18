# Following the Federal AI Dollar

## Project Overview

This project uses USAspending data to explore how federal AI contracting has changed, which agencies drive spending, who receives the money, and what the government is buying.

## Key Findings

* Identified AI contract obligations grew from $162M in FY2020 to $384M in FY2025.
* The Department of Defense accounts for 72.9% of identified obligations.
* The top 10 recipients account for 35.2%.
* Many major contract categories involve research and development.

## Data and Methodology

Source: [USAspending.gov](https://www.usaspending.gov/)

The dataset contains prime contract transactions from a search for "artificial intelligence" covering FY2020 through FY2026.

We retained transactions whose descriptions explicitly contain "artificial intelligence," allowing spaces or hyphens. This produced 2,726 transactions.

The analysis examines obligations by year, agency, recipient, and service category. An engineered `agency_group` feature separates the Department of Defense from other agencies.

## Reproducing the Analysis

1. Clone this repository.
2. Install dependencies: `pip install pandas matplotlib jupyter`
3. Search USAspending.gov for "artificial intelligence" across FY2020–FY2026 and download the Contracts Prime Transactions CSV.
4. Save it in `data/raw/` as `Contracts_PrimeTransactions_2026-09-07_H23M48S59_1.csv`.
5. Run `python scripts/analysis.py` from the project folder.

The script generates the cleaned dataset in `data/processed/`. The notebook is available at `notebooks/01_eda.ipynb`, and charts are in `figures/`. The large raw CSV is excluded from GitHub.

## Limitations and Ethics

This is not a measure of all federal AI spending. Keyword searches may miss relevant contracts or include contracts covering work beyond AI. Grants and other assistance awards are excluded. Obligations are funding commitments, not necessarily payments.

FY2026 is incomplete through September 4, 2026, so growth comparisons use FY2020–FY2025.

## Conclusion

Identifiable federal AI contracting has grown substantially, with the Department of Defense accounting for most obligations and research and development representing many of the largest purchasing categories.
