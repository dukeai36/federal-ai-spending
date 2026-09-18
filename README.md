# Following the Federal AI Dollar

## Project Overview

This project uses USAspending data to explore where federal AI contract dollars are going, which agencies drive the spending, and who receives the money.

## Key Findings

- AI contract obligations grew from about $162M in FY2020 to $384M in FY2025.
- The Department of Defense accounts for 72.9% of identified obligations.
- The top 10 recipients account for 35.2% of identified obligations.
- Many of the largest contract categories involve research and development.

## Dataset

Data comes from [USAspending.gov](https://www.usaspending.gov/) and includes prime contract transactions returned by a search for "artificial intelligence" from FY2020 through FY2026.

The cleaned dataset contains 2,726 transactions. FY2026 is partial through September 4, 2026.

## Methodology

Transactions were kept when their descriptions explicitly contained "artificial intelligence," allowing spaces or hyphens between the words.

The analysis examines spending over time, agencies, recipients, and product and service categories.

## Repository Structure

```text
federal-ai-spending/
├── data/
│   ├── raw/
│   └── processed/
│       └── ai_contracts_clean.csv
├── notebooks/
│   └── 01_eda.ipynb
├── README.md
├── LICENSE
└── .gitignore
```

## Reproducing the Analysis

1. Clone the repository.
2. Install `pandas`, `matplotlib`, and `jupyter`.
3. Download the USAspending source data.
4. Place the contract transactions CSV in `data/raw/`.
5. Run `notebooks/01_eda.ipynb` from top to bottom.

## Limitations

This analysis captures contracts explicitly referencing "artificial intelligence," not all federal AI spending. It excludes grants and other assistance awards. FY2026 is incomplete.

## Ethical Considerations

Keyword based analysis may miss relevant contracts and provide an incomplete picture of federal AI activity. Results should be interpreted as identifiable AI related contract obligations rather than total federal AI spending.

## Conclusion

Federal AI contracting has grown substantially, with obligations rising from about $162M in FY2020 to $384M in FY2025. The Department of Defense dominates this activity, accounting for 72.9% of identified obligations.

Overall, the data suggests that federal AI contracting growth is strongly connected to defense and research activities.

## Data Source

[USAspending.gov](https://www.usaspending.gov/)  
U.S. Government federal spending data