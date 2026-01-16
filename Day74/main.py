import pandas as pd
import matplotlib.pyplot as plt
colors = pd.read_csv("data/colors.csv")
print(colors.head())
number_of_unique_colors = colors["name"].nunique() # Count unique color names
print(f"Number of unique colors: {number_of_unique_colors}")
number_of_trans_color = colors.groupby("is_trans").count() # Count colors by transparency
number_of_trans_color_1 = colors.is_trans.value_counts() # Alternative way to count colors by transparency
print(number_of_trans_color_1)
sets = pd.read_csv("data/sets.csv")
print(sets.head())
sort_by_year = sets.sort_values("year") # Sort sets by year
print(sort_by_year.head())
different_sets = sets[sets["year"] == 1949 ] # Filter sets from the year 1949
print(different_sets.head())
largerst_number_of_part = sets.sort_values("num_parts", ascending=False) # Sort sets by number of parts in descending order
print(largerst_number_of_part.head())
sets_by_year = sets.groupby("year").count() # Count number of sets per year
print(sets_by_year["set_num"].head())
themes_by_year = sets.groupby("year").agg({"theme_id": pd.Series.nunique}) # Count unique themes per year
print(themes_by_year.head())
themes_by_year.rename(columns = {"theme_id": "nr_themes"}, inplace=True) # Rename column for clarity
print(themes_by_year.head())
print(themes_by_year.tail())
plt.figure(figsize=(10,6)) # Set figure size
ax1 = plt.gca() # Get current axes
ax2= ax1.twinx() # Create a second y-axis
ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color = 'g') # Plot number of sets per year
ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], 'r') # Plot number of unique themes per year
ax1.set_xlabel('Year', fontsize=14) # Set x-axis label
ax1.set_ylabel('Number of Sets', fontsize=14) # Set y-axis label for sets
ax2.set_ylabel('Number of Unique Themes', fontsize=14) # Set y-axis label for themes
# plt.show()
parts_per_set = sets.groupby("year").agg({"num_parts": pd.Series.mean}) # Calculate average number of parts per set each year
parts_per_set.rename(columns = {"num_parts": "avg_num_parts"}, inplace=True) # Rename column for clarity
print(parts_per_set.head())
plt.figure(figsize=(10,6)) # Set figure size
plt.scatter(parts_per_set.index[:-2], parts_per_set.avg_num_parts[:-2]) # Scatter plot of average number of parts per set each year
# plt.show()
set_theme_count = sets["theme_id"].value_counts() # Count number of sets per theme
print(set_theme_count[:5])
theme = pd.read_csv("data/themes.csv") # Read themes data
theme_correspond_star_wars = theme[theme["name"] == "Star Wars"] # Filter for Star Wars theme
print(theme_correspond_star_wars)
print(sets[sets["theme_id"] == 18]) # Display sets corresponding to Star Wars theme
print(sets[sets["theme_id"] == 209]) # Display sets corresponding to Star Wars theme
set_theme_count = pd.DataFrame({"id": set_theme_count.index, "set_count": set_theme_count.values}) # Convert to DataFrame
print(set_theme_count.head())
merged_df = pd.merge(set_theme_count, theme, on="id") # Merge with themes data
print(merged_df[:3])
plt.figure(figsize=(12,8)) # Set figure size
plt.xticks(fontsize=14, rotation=45) # Rotate x-axis labels for better readability
plt.yticks(fontsize=14) # Set y-axis tick font size
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
plt.bar(merged_df.name[:10], merged_df.set_count[:10]) # Bar plot of top 10 themes by number of sets
plt.show()