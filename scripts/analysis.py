#!/usr/bin/env python
# coding: utf-8

# # Following the Federal AI Dollar
# 
# This project explores federal AI contracts to understand how spending has changed, which agencies drive it, who receives the money, and what the government is buying.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

print("Libraries imported successfully")


# ## 1. Load and Inspect the Data
# 
# Load the USAspending data and review its structure.

# In[2]:


contracts = pd.read_csv(
    "data/raw/Contracts_PrimeTransactions_2026-09-07_H23M48S59_1.csv",
    low_memory=False
)

print("Contracts loaded successfully")
print("Rows and columns:")
print(contracts.shape)


# In[3]:


print("First 5 rows:")
print(contracts.head())


# In[4]:


print("Column names:")

for column in contracts.columns:
    print(column)


# ## 2. Data Cleaning
# 
# Select relevant fields and identify explicit AI contract transactions.

# In[5]:


ai_contracts = contracts[
    [
        "award_id_piid",
        "action_date",
        "action_date_fiscal_year",
        "federal_action_obligation",
        "awarding_agency_name",
        "awarding_sub_agency_name",
        "recipient_name",
        "transaction_description",
        "product_or_service_code_description",
        "naics_description"
    ]
].copy()

print("New dataset shape:")
print(ai_contracts.shape)

print("\nFirst 5 rows:")
print(ai_contracts.head())


# In[6]:


ai_match = ai_contracts[
    "transaction_description"
].str.contains(
    "artificial intelligence",
    case=False,
    na=False
)

print("Total transactions:")
print(len(ai_contracts))

print("\nTransactions containing 'artificial intelligence':")
print(ai_match.sum())

print("\nTransactions NOT containing 'artificial intelligence':")
print((~ai_match).sum())


# In[7]:


not_ai_match = ai_contracts[~ai_match]

print("Transactions without the exact phrase 'artificial intelligence':")
print(
    not_ai_match[
        [
            "action_date",
            "recipient_name",
            "transaction_description"
        ]
    ].to_string(index=False)
)


# In[8]:


ai_match_clean = ai_contracts[
    "transaction_description"
].str.contains(
    r"artificial[\s-]+intelligence",
    case=False,
    na=False,
    regex=True
)

print("Total transactions:")
print(len(ai_contracts))

print("\nTransactions matching our improved AI rule:")
print(ai_match_clean.sum())

print("\nTransactions not matching our improved AI rule:")
print((~ai_match_clean).sum())


# In[9]:


unmatched = ai_contracts[~ai_match_clean]

print("Remaining unmatched transactions:")
print(
    unmatched[
        [
            "action_date",
            "recipient_name",
            "transaction_description"
        ]
    ].to_string(index=False)
)


# ## 4. Feature Engineering
# 
# Group contracts into DoD and other federal agencies.

# In[10]:


ai_clean = ai_contracts[ai_match_clean].copy()

print("Original transactions:")
print(len(ai_contracts))

print("\nClean AI transactions:")
print(len(ai_clean))

print("\nTransactions removed:")
print(len(ai_contracts) - len(ai_clean))


# ## 3. Exploratory Analysis
# 
# Explore spending trends, agencies, and recipients.

# In[11]:


spending_by_year = (
    ai_clean
    .groupby("action_date_fiscal_year")["federal_action_obligation"]
    .sum()
)

print("AI contract obligations by fiscal year:")
print(spending_by_year)


# In[12]:


spending_millions = spending_by_year / 1_000_000

print("AI contract obligations by fiscal year, in millions:")
print(spending_millions.round(1))


# In[13]:


print("Earliest transaction date:")
print(ai_clean["action_date"].min())

print("\nLatest transaction date:")
print(ai_clean["action_date"].max())


# In[14]:


transactions_by_year = (
    ai_clean
    .groupby("action_date_fiscal_year")
    .size()
)

print("AI contract transactions by fiscal year:")
print(transactions_by_year)


# In[15]:


top_recipients = (
    ai_clean
    .groupby("recipient_name")["federal_action_obligation"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("Top 10 recipients by AI contract obligations:")
print((top_recipients / 1_000_000).round(1))


# In[16]:


total_spending = ai_clean["federal_action_obligation"].sum()

top_10_spending = top_recipients.sum()

top_10_share = (top_10_spending / total_spending) * 100

print("Total AI contract obligations:")
print(round(total_spending / 1_000_000, 1), "million")

print("\nTop 10 recipient obligations:")
print(round(top_10_spending / 1_000_000, 1), "million")

print("\nShare going to top 10 recipients:")
print(round(top_10_share, 1), "%")


# In[17]:


agency_spending = (
    ai_clean
    .groupby("awarding_agency_name")["federal_action_obligation"]
    .sum()
    .sort_values(ascending=False)
)

print("AI contract obligations by agency, in millions:")
print((agency_spending / 1_000_000).round(1))


# In[18]:


dod_spending = agency_spending["Department of Defense"]

dod_share = (dod_spending / total_spending) * 100

print("Department of Defense AI contract obligations:")
print(round(dod_spending / 1_000_000, 1), "million")

print("\nDoD share of total AI contract obligations:")
print(round(dod_share, 1), "%")


# In[19]:


ai_clean["agency_group"] = ai_clean["awarding_agency_name"].apply(
    lambda x: "Department of Defense"
    if x == "Department of Defense"
    else "Other Agencies"
)

dod_by_year = (
    ai_clean
    .groupby(
        ["action_date_fiscal_year", "agency_group"]
    )["federal_action_obligation"]
    .sum()
    .unstack()
)

print("AI contract obligations by year and agency group, in millions:")
print((dod_by_year / 1_000_000).round(1))


# ## 5. Key Findings and Visualizations
# 
# ### Finding 1: AI Contract Obligations Are Growing
# 
# AI contract obligations increased substantially from FY2020 to FY2025.

# In[20]:


chart1_data = spending_millions.loc[2020:2026]

plt.figure(figsize=(8, 5))

plt.plot(
    chart1_data.index,
    chart1_data.values,
    marker="o"
)

plt.title("Federal AI Contract Obligations Have Grown Sharply")
plt.xlabel("Fiscal Year")
plt.ylabel("Obligations ($ Millions)")

plt.grid(alpha=0.3)

plt.text(
    2026,
    chart1_data.loc[2026],
    "  FY2026 partial*",
    fontsize=9
)

plt.figtext(
    0.5,
    -0.02,
    "*FY2026 data through September 4, 2026",
    ha="center",
    fontsize=9
)

plt.tight_layout()

plt.show()

print("Chart 1 complete")


# ### Finding 2: Defense Dominates AI Contracting
# 
# DoD accounts for 72.9% of identified AI contract obligations.

# In[21]:


chart2_data = dod_by_year / 1_000_000

plt.figure(figsize=(8, 5))

plt.plot(
    chart2_data.index,
    chart2_data["Department of Defense"],
    marker="o",
    label="Department of Defense"
)

plt.plot(
    chart2_data.index,
    chart2_data["Other Agencies"],
    marker="o",
    label="Other Agencies"
)

plt.title("Defense Drives Federal AI Contract Spending")
plt.xlabel("Fiscal Year")
plt.ylabel("Obligations ($ Millions)")

plt.legend()
plt.grid(alpha=0.3)

plt.figtext(
    0.5,
    -0.02,
    "*FY2026 data through September 4, 2026",
    ha="center",
    fontsize=9
)

plt.tight_layout()

plt.show()

print("Chart 2 complete")


# ### Finding 3: Who Receives the Money?
# 
# The top 10 recipients account for 35.2% of identified AI contract obligations.

# In[22]:


chart3_data = (top_recipients / 1_000_000).sort_values()

plt.figure(figsize=(9, 6))

plt.barh(
    chart3_data.index,
    chart3_data.values
)

plt.title("Top Recipients of Federal AI Contract Obligations")
plt.xlabel("Obligations ($ Millions)")
plt.ylabel("")

plt.tight_layout()

plt.show()

print("Chart 3 complete")


# In[23]:


service_spending = (
    ai_clean
    .groupby("product_or_service_code_description")["federal_action_obligation"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("Top 10 products and services by AI contract obligations:")
print((service_spending / 1_000_000).round(1))


# ### Finding 4: AI Spending Is Tied to R&D
# 
# Many of the largest contract categories involve research and technology development.

# In[24]:


chart4_data = service_spending.copy()

short_names = [
    "Defense Applied Research",
    "Military Applied Research",
    "Professional Support",
    "IT Application Development",
    "Military Experimental Development",
    "Military Basic Research",
    "Engineering R&D",
    "Defense Advanced Development",
    "Defense Engineering Development",
    "General Science Basic Research"
]

chart4_data.index = short_names

chart4_data = (chart4_data / 1_000_000).sort_values()

plt.figure(figsize=(9, 6))

plt.barh(
    chart4_data.index,
    chart4_data.values
)

plt.title("AI Contract Dollars Are Heavily Tied to R&D")
plt.xlabel("Obligations ($ Millions)")
plt.ylabel("")

plt.tight_layout()

plt.show()

print("Chart 4 complete")


# ## 6. Limitations and Ethical Considerations
# 
# This analysis captures contracts explicitly referencing artificial intelligence, not all federal AI spending. FY2026 is also incomplete.

# In[25]:


ai_clean.to_csv(
    "data/processed/ai_contracts_clean.csv",
    index=False
)

print("Cleaned dataset saved successfully")
print("Rows saved:", len(ai_clean))


# ## 7. Conclusion
# 
# Federal AI contracting has grown substantially, with DoD driving much of the identified spending.
