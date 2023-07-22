

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('https://raw.githubusercontent.com/freeCodeCamp/boilerplate-medical-data-visualizer/main/medical_examination.csv')

# Add 'overweight' column
def calculate_bmi(row):
    height_m = row['height'] / 100
    bmi = row['weight'] / (height_m ** 2)
    return bmi
df['overweight'] = df.apply(lambda row: 1 if calculate_bmi(row) >= 25 else 0, axis=1)

df['cholesterol'] = df['cholesterol'].apply(lambda num: 0 if num == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda num: 0 if num == 1 else 1)

# Draw Categorical Plot
def draw_cat_plot():
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], var_name='Feature', value_name='Value')
    df_cat = df_cat.groupby(['cardio', 'Feature', 'Value']).size().reset_index(name='Count')

    sns.set(style='whitegrid')
    g = sns.catplot(x='Feature', y='Count', hue='Value', col='cardio', data=df_cat, kind='bar', height=4, aspect=1.5)
    fig = g.fig

    fig.savefig('catplot.png')

    plt.show()

    return fig
draw_cat_plot()



# Draw Heat Map
def draw_heat_map():
    height_percentile_2_5 = df['height'].quantile(0.025)
    height_percentile_97_5 = df['height'].quantile(0.975)

    weight_percentile_2_5 = df['weight'].quantile(0.025)
    weight_percentile_97_5 = df['weight'].quantile(0.975)
    df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) &
    (df['height'] >= height_percentile_2_5) &
    (df['height'] <= height_percentile_97_5) &
    (df['weight'] >= weight_percentile_2_5) &
    (df['weight'] <= weight_percentile_97_5)]

    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=np.bool))

    fig, ax = plt.subplots(figsize=(10, 8))

    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', mask=mask, square=True)

    # Set the title for the heatmap
    ax.set_title('Correlation Matrix Heatmap', fontsize=16)

    fig.savefig('heatmap.png')
    return fig

draw_heat_map()