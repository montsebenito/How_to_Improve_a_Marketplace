## How to improve a Marketplace: Project Overview
Segmented sellers based on sale/no_sale as well as on avg LTV (rmse ~BRL289) to find what characteristics makes a top seller, following **CRISP-DM** process model.
- **Business Understanding**
- **Data Understanding:** Explored and Wranged data from 9 datasets with +100k observations (one of the datasets have +1M observations!) and max 15 variables. Wordclouds of good/bad/neutral scored reviews
- **Data Preparation:** Engineered Features and cleaned city names. Dealt with missing values and encoded categorical data.
- **Data Modeling:** Optimized Random Forest Regressor and Classifier using GridCV.
- **Results Evaluation:** Extracted actionable insights from model with Partial Dependant Plots.


## Code and Resources Used
- Python Version: 3.8.5
- Packages: pandas, numpy, sklearn, matplotlib, seaborn, plotly, fuzzywuzzy, wordcloud, graphviz, pdpbox


## Repo Walk-Through
Please read this [project' post](https://montsebenito.github.io/improvemarketplace) for a business point of view
- [00byMontse.py:](https://github.com/montsebenito/How_to_Improve_a_Marketplace/blob/main/byMontse.py) A few auxiliary basic functions. i.e. Summary data function based on describe() method
- [01Olist_EDA:](https://github.com/montsebenito/How_to_Improve_a_Marketplace/blob/main/01Olist_EDA.ipynb) Explored data on each dataset individually to better understand the provided data. Looked at the distributions of the data and value counts. 
- [02Olist_DataWrangling:](https://github.com/montsebenito/How_to_Improve_a_Marketplace/blob/main/02Olist_DataWrangling.ipynb) Merged, Cleaned & Prepared Data to create a 'basic Seller Dataset' based on their characteristics, acquisition journey and sales to date. Also wranged a second version including (cleaned) location data.
- [03Olist_ProductBusinessSegments:](https://github.com/montsebenito/How_to_Improve_a_Marketplace/blob/main/03Olist_ProductBusinessSegments.ipynb) Answered business questions: 
    -Is there any Business Segment/Product Category doing particularly well ??? or particularly badly? (Sellers acquired between Dic,2017-Aug,2018)
- [04Olist_SellerSegmentation_Binary:](https://github.com/montsebenito/How_to_Improve_a_Marketplace/blob/main/04Olist_SellerSegmentation_SaleNoSale.ipynb) Seller Segmentation based on Sale/NoSale. What does it take to sell?
- [05Olist_SellerSegmentation_LTV:](https://github.com/montsebenito/How_to_Improve_a_Marketplace/blob/main/05Olist_SellerSegmentation_Regression.ipynb) Seller Segmentation based on avg LTV (1 month). What does it take to be a top seller?
- [06Olist Channels:](https://github.com/montsebenito/How_to_Improve_a_Marketplace/blob/main/06Olist_Channels.ipynb)What Channels bring in the most Top Sellers?


## Acknowledgements (and praise!):
- JungJoon Lee - on [EDA with eCommerce Marketplace (Seller Side)](https://www.kaggle.com/jungjoonlee/eda-with-ecommerce-marketplace-seller-side)
- Eduardo Cuducos - on getting a [clean list of Brazillian cities](https://github.com/cuducos/brazilian-cities/blob/master/cities.py)
- Gene Diaz jr - on [stopwords in Portuguese](https://github.com/stopwords-iso/stopwords-pt)
- Sankarshana Kadambari - on [how to clean city column](https://towardsdatascience.com/how-to-do-fuzzy-matching-in-python-pandas-dataframe-6ce3025834a6)

