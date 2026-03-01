import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# 1. Setup Connection
engine = create_engine('postgresql://postgres:1905@localhost:5432/cars_analysis')
sns.set_theme(style="whitegrid")

# 2. Extract Data using your SQL queries
df_trans = pd.read_sql("SELECT transmission, AVG(selling_price) as price FROM vehicles GROUP BY transmission", engine)
df_owner = pd.read_sql("SELECT owner, MAX(selling_price) as max_p, MIN(selling_price) as min_p FROM vehicles GROUP BY owner", engine)
df_seller = pd.read_sql("SELECT seller_type, COUNT(*) as count FROM vehicles GROUP BY seller_type", engine)
df_deprec = pd.read_sql("""
    SELECT year, AVG(selling_price) as price 
    FROM vehicles WHERE year > 2010 
    GROUP BY year ORDER BY year
""", engine)

# 3. Create the Layout (2x2 Grid)
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Used Car Market Executive Dashboard', fontsize=20, fontweight='bold')

# Plot 1: Transmission (Bar Chart)
sns.barplot(x='transmission', y='price', hue='transmission', data=df_trans, ax=axes[0,0], palette='Blues_d', legend=False)
axes[0,0].set_title('Avg Price: Automatic vs Manual', fontsize=14)

# Plot 2: Year-over-Year (Line Chart)
sns.lineplot(x='year', y='price', data=df_deprec, ax=axes[0,1], marker='o', color='red', linewidth=2.5)
axes[0,1].set_title('Market Depreciation Trend (Post-2010)', fontsize=14)

# Plot 3: Seller Type (Pie Chart)
axes[1,0].pie(df_seller['count'], labels=df_seller['seller_type'], autopct='%1.1f%%', colors=sns.color_palette('pastel'))
axes[1,0].set_title('Seller Distribution', fontsize=14)

# Plot 4: Owner Impact (Range Chart)
df_owner_melt = df_owner.melt(id_vars='owner', var_name='Type', value_name='Price')
sns.barplot(x='owner', y='Price', hue='Type', data=df_owner_melt, ax=axes[1,1])
axes[1,1].set_title('Price Range by Ownership History', fontsize=14)
plt.xticks(rotation=15)

# 4. Save and Finish
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('car_analysis_dashboard.png', dpi=300)
print("Dashboard saved as car_analysis_dashboard.png")