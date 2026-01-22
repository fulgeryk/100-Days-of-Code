import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

df_cost = pd.read_csv("cost_revenue_dirty.csv")
#Challenge 1
#How many rows and columns does the dataset contain?
print(df_cost.shape)
#Are there any NaN values present?
print(df_cost.isna().values.any())
#Are there any duplicate rows?
print(df_cost.duplicated().values.any())
#What are the data types of the columns?
print(df_cost.info())
#Challenge 2
#Convert the USD_Production_Budget, USD_Worldwide_Gross, and USD_Domestic_Gross columns to a numeric format by removing $ signs and ,.
chars_to_be_removed = ["$",","]
columns_to_be_removed = ["USD_Production_Budget",
                         "USD_Worldwide_Gross",
                         "USD_Domestic_Gross"]
for col in columns_to_be_removed:
    for char in chars_to_be_removed:
        #replace each character with empty string
        df_cost[col]=df_cost[col].astype(str).str.replace(char,"")
    #convert column to a numeric type
    df_cost[col] = pd.to_numeric(df_cost[col])

print(df_cost.head())

#Challenge 3
#Convert the Release_Date column to a Pandas Datetime type.
df_cost["Release_Date"] = pd.to_datetime(df_cost["Release_Date"])
print(df_cost["Release_Date"].head())

#Investigate the Films that had Zero Revenue
#Challange 1
#What is the average production budget of the films in the data set?
#What were the minimums for worldwide and domestic revenue?
#Are the bottom 25% of films actually profitable or do they lose money?
print(df_cost.describe())
#So which film was the lowest budget film in the dataset?
print(df_cost[df_cost["USD_Production_Budget"] == 1100])
#And the highest budget film in the dataset is:
print(df_cost[df_cost["USD_Production_Budget"] == 425000000])
#Challenge 2
#How many films grossed $0 domestically (i.e., in the United States)? What were the highest budget films that grossed nothing?
zero_domestic = df_cost[df_cost["USD_Domestic_Gross"] == 0]
print(f"Number of films that grossed 0$ domestically {len(zero_domestic)}")
print(zero_domestic.sort_values('USD_Production_Budget', ascending=False))
#Challenge 3
#How many films grossed $0 worldwide? What are the highest budget films that had no revenue internationally (i.e., the biggest flops)?
zero_worldwide = df_cost[df_cost["USD_Worldwide_Gross"] == 0]
print(f"Number of films that grossed 0$ Worldwide {len(zero_worldwide)}")
print(zero_worldwide.sort_values('USD_Worldwide_Gross', ascending=False))

#Filter on Multiple Conditions: International Films
international_releases = df_cost.loc[(df_cost["USD_Domestic_Gross"] == 0) & (df_cost["USD_Worldwide_Gross"] != 0)]
print(f"Number of international release: {len(international_releases)}")
print(international_releases.head())

#Challenge
#Use the Pandas .query() function to accomplish the same thing.
# Create a subset for international releases that had some worldwide gross revenue, but made zero revenue in the United States.
international_releases_with_query = df_cost.query("USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0")
print(f"Number of international release: {len(international_releases_with_query)}")
print(international_releases_with_query)
#Challenge
# Identify which films were not released yet as of the time of data collection (May 1st, 2018).
print(df_cost["Release_Date"].tail())
film_not_release = df_cost.loc[(df_cost["Release_Date"] > "2018-05-01")]
print(f"Number of unreleased movies: {len(film_not_release)}")
print(film_not_release)

#Create another DataFrame called data_clean that does not include these films.
data_clean = df_cost.drop(film_not_release.index)

#Bonus Challenge: Films that Lost Money
money_losing = data_clean.loc[data_clean["USD_Production_Budget"] > data_clean["USD_Worldwide_Gross"]]
print(len(money_losing)/len(data_clean))

#Seaborn Data Visualisation: Bubble Charts

#Seaborn Scatter Plots
#To create a .scatterplot(), all we need to do is supply our DataFrame and the column names that we'd like to see on our axes.

plt.figure(figsize=(8,4), dpi=200)
ax = sns.scatterplot(data = data_clean,
                x = "USD_Production_Budget",
                y = "USD_Worldwide_Gross")



#From Scatter Plot to Bubble Chart
#But the reason we're using Seaborn is because of the hue and size parameters that make it very easy to create a bubble chart

ax = sns.scatterplot(data=data_clean,
                         x="USD_Production_Budget",
                         y="USD_Worldwide_Gross",
                         hue="USD_Worldwide_Gross",  # colour
                         size="USD_Worldwide_Gross")  # dot sie

ax.set(ylim=(0, 3000000000),
        xlim=(0, 450000000),
        ylabel='Revenue in $ billions',
        xlabel='Budget in $100 millions')

#To set the styling on a single chart (as opposed to all the charts in the entire notebook) we can use Python's with keyword.
#We've seen with used already when it comes to opening files in previous lessons.

# set styling on a single chart

with sns.axes_style("darkgrid"):
    ax = sns.scatterplot(data=data_clean,
                         x="USD_Production_Budget",
                         y="USD_Worldwide_Gross",
                         hue="USD_Worldwide_Gross",  # colour
                         size="USD_Worldwide_Gross")  # dot sie

    ax.set(ylim=(0, 3000000000),
           xlim=(0, 450000000),
           ylabel='Revenue in $ billions',
           xlabel='Budget in $100 millions')



#Challenge

with sns.axes_style("darkgrid"):
    ax = sns.scatterplot(data=data_clean,
                         x="Release_Date",
                         y="USD_Production_Budget",
                         hue="USD_Worldwide_Gross",  # colour
                         size="USD_Worldwide_Gross")  # dot sie

    ax.set(ylim=(0, 450000000),
           xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()),
           ylabel='Year',
           xlabel='USD_Production_Budget')

# plt.show()

#Floor Division: A Trick to Convert Years to Decades

#Challenge
#Can you create a column in data_clean that has the decade of the movie release.
dt_index = pd.DatetimeIndex(data_clean["Release_Date"])
years = dt_index.year
decades = years // 10 * 10
data_clean["Decade"] = decades
#Challenge
#Create two new DataFrames: old_films and new_films
old_film = data_clean[data_clean["Decade"] <= 1960]
new_films = data_clean[data_clean["Decade"] > 1960]
print(old_film.describe())
print(old_film.sort_values("USD_Production_Budget", ascending=False).head())

#Plotting Linear Regressions with Seaborn

plt.figure(figsize=(8,4), dpi=150)

with sns.axes_style("whitegrid"):
    ax = sns.regplot(data=old_film,
                     x="USD_Production_Budget",
                     y="USD_Worldwide_Gross",
                     scatter_kws= {"alpha": 0.4},
                     line_kws= {"color" : "black"})

# Challenge
#Use Seaborn's .regplot() to show the scatter plot and linear regression line against the new_films.
plt.figure(figsize=(8,4), dpi=150)
with (sns.axes_style("darkgrid")):
    ax_new = sns.regplot(data=new_films,
                         x = "USD_Production_Budget",
                         y = "USD_Worldwide_Gross",
                         scatter_kws = {"alpha": 0.4},
                         line_kws = {"color": "black"})
    ax_new.set(ylim=(0, 3000000000),
               xlim=(0, 450000000),
               xlabel= "Budget in $ millions",
               ylabel= "Revenue in $ billions")

plt.show()


#Use scikit-learn to Run Your Own Regression
#Now we can run a LinearRegression. First, let's create a LinearRegression object that will do the work for us.
regression = LinearRegression()

#Now we should specify our features and our targets (i.e., our response variable).
# You will often see the features named capital X and the target named lower case y:
# Explanatory Variable(s) or Feature(s)
x = pd.DataFrame(new_films, columns=["USD_Production_Budget"])
# Response Variable or Target
y = pd.DataFrame(new_films, columns=["USD_Worldwide_Gross"])
print(x)

#Our LinearRegression does not like receiving Pandas Series (e.g., new_films.USD_Production_Budget), so I've created some new DataFrames here.
regression.fit(x,y)

#That's it. Now we can look at the values of theta-one and theta-zero from the equation above.
#Theta zero
print(regression.intercept_)

#theta one
print(regression.coef_)

#R-Squared: Goodness of Fit
# R-squared
print(regression.score(x, y))

#Run a linear regression for the old_films. Calculate the intercept, slope and r-squared.
# How much of the variance in movie revenue does the linear model explain in this case?
# Explanatory Variable(s) or Feature(s)
x = pd.DataFrame(old_film, columns=["USD_Production_Budget"])
# Response Variable or Target
y = pd.DataFrame(old_film, columns=["USD_Worldwide_Gross"])

#That's it. Now we can look at the values of theta-one and theta-zero from the equation above.
#Theta zero
print(regression.intercept_[0])

#theta one
print(regression.coef_[0])

#R-Squared: Goodness of Fit
# R-squared
print(regression.score(x, y))

#Challenge
#You've just estimated the intercept and slope for the Linear Regression model.
# Now we can use it to make a prediction! For example, how much global revenue does our model estimate for a film with a budget of $350 million?

budget = 350000000
revenue_estimate = regression.intercept_[0] + regression.coef_[0,0]*budget
revenue_estimate = round(revenue_estimate, -6)
print(f'The estimated revenue for a $350 film is around ${revenue_estimate:.10}.')