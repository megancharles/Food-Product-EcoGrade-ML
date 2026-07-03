# Food-Product-EcoGrade-ML

**Can open food data predict environmental performance without costly LCA data collection?**

This project explores how much readily available data about food products can tell us about their environmental impact grade - starting with ingredient lists, the first data source tested. It's a continuation of research started during a PG Cert in Applied Data Science.

## The question

Life Cycle Assessments (LCA) remain the gold standard for measuring a food product's environmental footprint, and nothing here is trying to compete with that rigour. What LCA doesn't offer is scale - it's slow and resource-intensive, so most products never get assessed at all. Open Food Facts already publishes a [Green-Score](https://world.openfoodfacts.org/eco-score-the-environmental-impact-of-food-products) grade (A-plus through F) for many products - known as the Eco-Score until Open Food Facts renamed it in late 2024. This project asks a narrower, more exploratory question: **how much signal about environmental grade is already present in data that's cheap and readily available for most products?** Ingredient lists are the first such data source tested - not the only one this project is interested in. The value of that broader idea isn't fully settled yet - it's part of what this research is trying to figure out.

## Experiment 1 (this repo)

The first data source tested is ingredient lists - readily available for most products, unlike packaging or sourcing data.

*Research question:* To what extent can structured ingredient classification data predict the environmental performance of food products?

Working with ~32,000 products from Open Food Facts, ingredients were vectorised with TF-IDF and modelled with XGBoost, comparing a regression and a classification approach to the 7-grade Green-Score scale. The best model - an XGBoost multiclass classifier - achieved **74% accuracy** and a **weighted F1 of 0.73**, with an average error of less than one grade when wrong. The biggest gain came from switching to classification, which let the rarest grade (`a-plus`) get predicted at all, though it remains the hardest class to classify reliably.

This builds on an earlier experiment (Experiment 0, not in this repo) that used LLM-processed ingredient text and embeddings on a smaller dataset, reaching ~35-37% accuracy. Structuring the ingredient data more consistently was the main driver of the jump in performance. Full narrative, methodology, and results for both experiments are in the project's research overview document.

## Repo structure

```
Food-Product-EcoGrade-ML/
├── exp_1/                          # First experiment: full pipeline
│   ├── config.py                   # Path config (data dirs)
│   ├── requirements.txt            # Python dependencies
│   ├── notebooks/
│   │   ├── 01_explore_data.ipynb   # Cleaning, EDA, class distribution
│   │   └── 02_model_data.ipynb     # TF-IDF, balancing, XGBoost, evaluation
│   ├── src/
│   │   └── data.py                 # Data loading/cleaning helpers
│   ├── data/
│   │   ├── raw/                    # Raw Open Food Facts extract
│   │   └── processed/              # Cleaned dataset
│   └── outputs/
│       └── confusion_matrix.png
├── exp_2/                          # Follow-up experiment (in progress)
│   └── config.py
└── github_page/                    # Project write-up hosted via GitHub Pages
    ├── index.html
    ├── experiment-0.html
    └── experiment-1.html
```

## Open Food Facts

This project's data - ingredient lists and Green-Score labels for both experiments - was pulled directly from [Open Food Facts](https://world.openfoodfacts.org/), a free, crowdsourced database of food products from around the world. It covers ingredients, allergens, nutrition facts, and - for a subset of products - a Green-Score environmental grade (known as the Eco-Score before Open Food Facts renamed it in late 2024). It's run by a non-profit of volunteer contributors who add and edit product data (often via barcode scans), and as of 2025 the database holds over 4 million products from 150+ countries.

A few things worth knowing about it in the context of this project:

- **Open licensing.** The database is published under the [Open Database License](https://opendatacommons.org/licenses/odbl/), and product images under Creative Commons Attribution ShareAlike - reuse is permitted for any purpose provided the source is attributed and any improvements are shared back.
- **Crowdsourced, so uneven.** Because entries are added by volunteers rather than a single standardised process, coverage and data quality vary by product, country, and category. Ingredient lists in particular can be inconsistent, multilingual, or incompletely tagged - a large part of Experiment 0 and Experiment 1's work was cleaning and structuring this data before modelling.
- **Green-Score coverage is partial.** Not every product has a Green-Score grade, which is why the labelled dataset used for training (~32,000 rows in Experiment 1) is a fraction of the full database.
- **Nightly exports.** Open Food Facts publishes full database dumps (CSV, JSONL, Parquet) rather than expecting bulk scraping via the API, which is how the raw data for this project was sourced.

## Status & next steps

This is active research rather than a finished tool. `exp_2/` is an early start on the next planned experiments, which include:

1. **Deep learning** - benchmarking neural network approaches against the current XGBoost models.
2. **Feature augmentation** - testing which additional product attributes (packaging, category, origin, nutrition score) improve accuracy alongside ingredients.
3. **Explainability** - applying SHAP/LIME to check whether model reasoning aligns with known environmental impact factors.
4. **Unsupervised learning** - exploring whether clustering reveals environmental groupings beyond the existing Green-Score labels.

## Background

This project builds on research carried out for a PG Cert in Applied Data Science, extended here with a cleaner pipeline and further experimentation, in collaboration with Dr Mohamed Ragab (University of Birmingham) and Dr Haitham Mahmoud (Fujitsu Research). A full write-up, [Ingredient Lists as Environmental Predictors](https://megancharles.github.io/Food-Product-EcoGrade-ML/index.html), is also published via GitHub Pages (source in github_page/).