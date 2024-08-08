# **01 - Introduction to Visualization Tools**
## Matplotlib : Standard Python Visualization Library
- Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms

### Layers in Matplotlib
1. **Scripting Layer**
    - This is the highest-level interface where users write scripts to create visualizations It includes functions from the `pyplot` module (e.g., `plt.plot()`, `plt.scatter()`, `plt.show()`)
    - This layer is user-friendly and designed for quick and easy plotting
2. **Object-Oriented Layer**
    - This layer provides a more complex and powerful way to create plots using object-oriented programming
    - Users can create figure and axes objects explicitly, giving more control over the plot elements and layout
    - For example, you can create a figure and add axes with `fig = plt.figure()` and `ax = fig.add_subplot()`
3. **Artist Layer**
    - The artist layer consists of all the drawable elements (artists) in the plot
    - Each artist can be modified individually (e.g., changing colors, adding annotations), allowing for detailed customization of the plot
4. **Backend Layer**
    - The backend layer is responsible for rendering the figure to a specific format or display
    - It translates the high-level plotting commands into lower-level rendering commands
    - Users can switch backends as needed based on the environment (e.g., saving to a file or displaying in a window)

![matplotlib](https://miro.medium.com/v2/resize:fit:705/0*DBsvGcupUm28IRCS.png)

### Matplotlib.Pyplot
- One of the core aspects of Matplotlib is `matplotlib.pyplot`
- It is Matplotlib's scripting layer which we studied in details in the videos about Matplotlib
- Recall that it is a collection of command style functions that make Matplotlib work like MATLAB 
- Each `pyplot` function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc

```python
# we are using the inline backend
%matplotlib inline

import matplotlib as mpl
import matplotlib.pyplot as plt
```

```python
print('Matplotlib version : ', mpl.__version__)  # >= 2.0.0
```

```python
print(plt.style.available)
mpl.style.use(['ggplot']) # optional: for ggplot-like style
```

### Two types of plotting
- There are two styles/options of plotting with `matplotlib`， plotting using the Artist layer and plotting using the scripting layer.
#### 01 Scripting layer (procedural method) 
- using `matplotlib.pyplot` as `plt`
- use `plt` i.e. `matplotlib.pyplot` and add more elements by calling different methods procedurally
- for example, `plt.title(...)` to add title or `plt.xlabel(...)` to add label to the x-axis

```python
# Option 1: This is what we have been using so far
df.plot(kind='line', figsize=(20, 10)) 
plt.title('Option 1')
plt.xlabel('Labels')
plt.ylabel('Values')
```

`annotate` method of the **scripting layer** or the **pyplot interface**. 
- `s`: str, the text of annotation
- `xy`: Tuple specifying the (x,y) point to annotate (in this case, end point of arrow)
- `xytext`: Tuple specifying the (x,y) point to place the text (in this case, start point of arrow)
- `xycoords`: The coordinate system that xy is given in - 'data' uses the coordinate system of the object being annotated (default)
- `arrowprops`: Takes a dictionary of properties to draw the arrow
    - `arrowstyle`: Specifies the arrow style, `'->'` is standard arrow
    - `connectionstyle`: Specifies the connection type. `arc3` is a straight line
    - `color`: Specifies color of arrow
    - `lw`: Specifies the line width
#### 02 Artist layer (Object oriented method) 
- using an `Axes` instance from `Matplotlib`
- use an `Axes` instance of your current plot and store it in a variable (eg. `ax`)
- add more elements by calling methods with a little change in syntax (by adding "`set_`" to the previous methods)
- for example, use `ax.set_title()` instead of `plt.title()` to add title,  or `ax.set_xlabel()` instead of `plt.xlabel()` to add label to the x-axis.

```python
# option 2: preferred option with more flexibility
ax = df.plot(kind='line', figsize=(20, 10))
ax.set_title('Option 2')
ax.set_xlabel('Labels')
ax.set_ylabel('Values')
```
## Some Pandas
```python
import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library
```

```python
df.head()
# tip: You can specify the number of rows you'd like to see as follows: df_can.head(10)
```

```python
# view the bottom 5 rows of the dataset
df.tail()
```

```python
# short Summary of the dataframe
df.info(verbose=False)
```

```python
# to get the list of column headers
df.columns
```

```python
# to get the list of indices
df.index
```

```python
# The default type of intance variables index & columns are NOT list
df.columns.tolist()
df.index.tolist()
```

```python
# size of dataframe (rows, columns)
df.shape
```

```python
# in pandas axis=0 represents rows (default) and axis=1 represents columns
df.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
```

```python
df.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
```

```python
df['Total'] = df.sum(axis=1)
```

```python
# to check how many null objects in the dataset
df.isnull().sum()
```

```python
# view a quick summary of each column in dataframe
df.describe()
```

```python
df.column_name # returns series
df['column']
df[['column1', 'column2']] # returns dataframe
```

```python
df.loc[label]    # filters by the labels of the index/column
df.iloc[index]   # filters by the positions of the index/column
```

```python
df.set_index('Country', inplace=True)
# tip: The opposite of set is reset. So to reset the index, we can use df.reset_index()
```

```python
# optional: to remove the name of the index
df.index.name = None
```

```python
# 1. the full row data (all columns)
df.loc['Japan']
```

```python
# 2. for year 2013
df.loc['Japan', 2013]
```

```python
# 3. for years 1980 to 1985
df.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]]
```

```python
# to avoid this ambuigity, let's convert the column names into strings
df.columns = list(map(str, df.columns))
```

```python
# we can pass multiple criteria in the same line.
# let's filter for AreaNAme = Asia and RegName = Southern Asia

df[(df['Continent']=='Asia') & (df['Region']=='Southern Asia')]

# note: When using 'and' and 'or' operators, pandas requires we use '&' and '|' instead of 'and' and 'or'
# don't forget to enclose the two conditions in parentheses
```

```python
df.sort_values(['Total'], ascending=False, axis=0, inplace=True)
```

# **02 Basic & Specialized Visualization Tools**
## Types of Plots
* `line` for line plots
* `bar` for vertical bar plots
* `barh` for horizontal bar plots
* `hist` for histogram
* `box` for boxplot
* `kde` or `density` for density plots
* `area` for area plots
* `pie` for pie plots
* `scatter` for scatter plots
* `hexbin` for hexbin plot


## 01 Line Plots
- A line chart or line plot is a type of plot which displays information as a series of data points called 'markers' connected by straight line segments
- It is a basic type of chart common in many field
- Use line plot when you have a continuous data set
- These are best suited for trend-based visualizations of data over a period of time

```python
# Data
years = [2000, 2005, 2010, 2015, 2020]
values = [100, 200, 300, 400, 500]

# Create a line plot
plt.plot(years, values)
plt.xlabel('Years')
plt.ylabel('Values')
plt.title('Growth Over Years')
plt.show()
```
### Customizing Line Plots
- To use `kind="line"` in your code, you would leverage the Pandas DataFrame `plot` method, which simplifies the process of creating various types of plots
- This method internally uses Matplotlib for plotting but provides a more convenient and consistent interface for plotting data directly from Pandas DataFrame

```python
# Data
data = { 'Years': [2000, 2005, 2010, 2015, 2020], 
		'Values': [100, 200, 300, 400, 500] 
}
df = pd.DataFrame(data) 

# Create a line plot using Pandas
df.plot(x='Years', y='Values', kind='line', marker='o') 
plt.xlabel('Years') 
plt.ylabel('Values') 
plt.title('Growth Over Years') 
plt.show()
```
![Line Plot](https://i0.wp.com/ajaytech.co/wp-content/uploads/2019/08/standard_plot.png?resize=737%2C500&ssl=1)

## 02 Area Plots
- Visualize plot as a cumulative plot, also knows as a **Stacked Line Plot** or **Area plot**
- Area plots are stacked by default
- To produce a stacked area plot, each column must be either all positive or all negative values (any `NaN`, i.e. not a number, values will default to 0)
- To produce an unstacked plot, set parameter `stacked` to value `False`
- The unstacked plot has a default transparency (alpha value) at 0.5

```python
# Data
years = [2000, 2005, 2010, 2015, 2020]
values = [100, 200, 300, 400, 500]

# Create an area plot using fill_between
plt.fill_between(years, values, color='skyblue', alpha=0.5)
plt.xlabel('Years')
plt.ylabel('Values')
plt.title('Growth Over Years')
plt.show()
```
### Customizing Area Plots
```python
# Data
data = {
    'Years': [2000, 2005, 2010, 2015, 2020],
    'Values': [100, 200, 300, 400, 500]
}
df = pd.DataFrame(data)

# Create an area plot
df.plot(x='Years', y='Values', kind='area', alpha=0.5)
plt.xlabel('Years')
plt.ylabel('Values')
plt.title('Growth Over Years')
plt.show()
```
![Area Plot](https://python-charts.com/en/evolution/area-plot-matplotlib_files/figure-html/area-plot-alpha-matplotlib.png)

## 03 Bar Charts (Dataframe)
- A bar plot is a way of representing data where the _length_ of the bars represents the magnitude/size of the feature/variable
- bar graphs usually represent numerical and categorical variables grouped in intervals
- To create a bar plot, we can pass one of two arguments via `kind` parameter in `plot()`
	- `kind=bar` creates a _vertical_ bar plot
	- `kind=barh` creates a _horizontal_ bar plot
#### Bar Plot (`bar`)
- A bar plot displays categorical data with rectangular bars with lengths proportional to the values they represent
- The bars can be oriented vertically

```python
# Sample data
categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

# Create a bar plot
plt.bar(categories, values, color='lightblue')
plt.title('Vertical Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()
```

#### Horizontal Bar Plot (`barh`)
- A horizontal bar plot is similar to a bar plot but displays the bars horizontally
- This is particularly useful when you have long category names or when you want to emphasize the comparison of values

```python
# Data
data = { 'Years': [2000, 2005, 2010, 2015, 2020], 
		'Values': [100, 200, 300, 400, 500] 
}
df = pd.DataFrame(data) 

# Create a line plot using Pandas
df.plot(x='Years', y='Values', kind='barh') 
plt.xlabel('Years') 
plt.ylabel('Values') 
plt.title('Growth Over Years') 
plt.show()
```
![bar](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQQAAADCCAMAAACYEEwlAAAAllBMVEX///8fd7ShoaGkpKSivtkCcbGDqs4ceLcoVHYAbK/j6/MAbrDE1eYAaq7v8/j09/qbudZzoMg9g7pqamrz8/P5+fmQkJDe3t5paWmXl5eqqqp4eHhxcXHq6uqKiori4uK4uLhgYGDS0tKAgIC+0eTGxsYAYKq8vLxISEhYWFgkJCQZTXOSlpuAiZM1WnpRaoJsfIw9PT2ADCDSAAADF0lEQVR4nO3da1PaQBiG4cdQrKh4aAIhCQEEQVt7/P9/rpMXizq2ZbNgSjf3/UEZ591M9hrADxgjERERERERERERERFRE0XBlO+AsD/Pf1zHfykIAsFqMUKeK83S6lGLEZJCscZeSw+2+jtZaFghpFH8Bqezn86vXLrdzNdGGIwVJwf+TLjqd7fXO97M197JXb5MOmX16HDfE951j7bX3QHhKRAEggWCQLBAEAgWCALBAkEgWCAIBAsEgWCBIBAsEASCBYJAsEAQCFbLEdJB9bXdCMVy5Lu0mZpAiLKJlEyH3id54dTA+/hNIIwVS+Vy4XuOp6u+Q6vb7Uf6Q408E4YT36XWac/hHI/Ozn2P/1/8dgBBIFggCAQLBIFggSAQLBAEggWCQLBAEAgWCALBAkEgWCAIBAsEgWCBoFAQ7ubV13YjTO6mvkutIBDuZ0V1cejI9xyDQPi442XCQSCkk1n1rd3vCY+BIBAsEASCBYJAsEAQCBYIAsECQSBYIAgECwSBYIEgECwQBIIFgkCwQFDrEdJP3kurwkDICmlafSDpVxAIWXSfapBkvucYBIJ0479UwSDsdtV8IAgWCALBAkEgWCAIBAsEgWCBIBCsJ4RLpzbjQSJcrHoOrTYLw0Tou2yqv1kIgkCwQBAIFggCwQJBIFggCAQrCIRpNAOhHAzL1iNUN858fufQViIk4+TF0lYipFHOy+ExEASCBYJAsEAQCBYIAsECQSBYIKhJhONrl67CRvjQdejsOnAEl/kuCCCsNwUCCOtNgQDCelMggLDeFAjNIyQJCNOiKJ8vvey9d+g5gsv8cwSX+RcILvM73i+ynOfVZ5HRuk72cPKq1z966Pya/+w2/2Wz4KvL/Mm3zfz33xztL/NR7oGQl/PZlpFk28Ar2Dee3/sNb5NRvO3+rsmy5jFnBzZPtL/iWa3x+XhYb0E2tD+Wce5HHtea30fTWb1L6ueLrNabyCDePvOiQjvcBtuzLLuZ1pmf50mtbQ3q/h/5QmnjCGOVkzrz89Gw3lMnW0zqvRyi5l8OREREREREreon+NWASEdug9kAAAAASUVORK5CYII=)

## 04 Histogram
- A histogram is a way of representing the _frequency_ distribution of numeric dataset
- The way it works is it partitions the x-axis into _bins_, assigns each data point in our dataset to a bin, and then counts the number of data points that have been assigned to each bin
- **Bins** : The range of values is divided into intervals known as bins. Each bin has a certain width, and the bins are contiguous
- **Frequency** : The height of each bar represents the number of data points that fall within that bin
- **Density** : Sometimes, histograms are normalized to show densities instead of frequencies, where the area of each bin represents the proportion of the data

```python
# Generate random data 
data = np.random.randn(1000)
# Create a histogram
plt.hist(data, bins=30, edgecolor='black')

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')
plt.show()
```
![hist](data:image/png;base64,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)

## 05 Pie Plots
- A pie chart is a circular statistical graphic that is divided into slices to illustrate numerical proportions
- Each slice of the pie represents a category's contribution to the total, making it easy to visualize the relative sizes of different parts in comparison to the whole
- **Slices**
    - Each slice represents a category's proportion relative to the whole dataset
    - The angle of each slice is proportional to the quantity it represents
- **Total** : The total of all the slices equals 100%, which corresponds to the whole pie
- **Labels** : Each slice is often labeled with the category name and its corresponding percentage or value to provide clarity
- **Colors** : Different colors are usually used for each slice to enhance visual distinction and make the chart easier to read

```python
# Sample data
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [15, 30, 45, 10]  # Values representing each category
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
explode = (0.1, 0, 0, 0)  # explode the 1st slice (Category A)

# Create the pie chart
# plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.title('Pie Chart Example')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
```

- `kind = 'pie'` keyword, along with the following additional parameters
- `autopct` - is a string or function used to label the wedges with their numeric value. The label will be placed inside the wedge. If it is a format string, the label will be `fmt%pct`
- `startangle` - rotates the start of the pie chart by angle degrees counterclockwise from the x-axis
- `shadow` - Draws a shadow beneath the pie (to give a 3D feel)
- `pctdistance` - Push out the percentages to sit just outside the pie chart 

![pie](data:image/png;base64,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)

## 06 Box Plots
- A box plot (or whisker plot) is a standardized way to display the distribution of a dataset based on a five-number summary: minimum, first quartile (Q1), median (Q2), third quartile (Q3), and maximum

![Box Plots](https://media.geeksforgeeks.org/wp-content/uploads/20201223024124/img.jpg)

- It provides a visual representation of the central tendency, variability, and potential outliers in the data
	- **Minimum :** The smallest number in the dataset excluding the outliers
	- **First quartile :** Middle number between the `minimum` and the `median`
	- **Second quartile (Median) :** Middle number of the (sorted) dataset
	- **Third quartile :** Middle number between `median` and `maximum`
	- **Maximum :** The largest number in the dataset excluding the outliers

```python
# Sample data
data = {
    'Group A': [12, 15, 14, 10, 14, 13, 15, 16, 20, 19],
    'Group B': [22, 21, 20, 24, 25, 21, 20, 22, 30, 29],
    'Group C': [32, 31, 30, 29, 35, 33, 28, 30, 40, 38]
}
df = pd.DataFrame(data)

# Create a box plot
# plt.figure(figsize=(10, 6))

# df.boxplot()
df.plot(kind='box', grid=True)

plt.title('Box Plot Example')
plt.ylabel('Values')
plt.xlabel('Groups')
plt.grid(axis='y')
plt.show()
```

- `vert` parameter in the **plot** function and assign it to `False` for horizontal box plots
- `color` to specify a different color 


## 07 Scatter Plots
- A `scatter plot` (2D) is a useful method of comparing variables against each other
- `Scatter` plots look similar to `line plots` in that they both map independent and dependent variables on a 2D graph
- With further analysis using tools like regression, we can mathematically calculate this relationship b/w points and use it to predict trends outside the dataset
- To investigate the relationship or correlation between two continuous variables
- To identify patterns, trends, clusters, and outliers in the data
- To visualize the distribution of data points in two dimension

```python
# Sample data
data = {
'Height': [150, 160, 170, 180, 190, 200, 210, 220],
'Weight': [50, 55, 60, 70, 75, 85, 90, 95]
}
df = pd.DataFrame(data)

# Create a scatter plot
# plt.figure(figsize=(10, 6))
# df.plot(kind='scatter', x='Height', y='Weight', color='blue')
plt.scatter(df['Height'], df['Weight'], color='blue', alpha=0.5)

plt.title('Scatter Plot of Height vs. Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()
```
![scatter](data:image/png;base64,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)

## 08 Bubble Plots
- A `bubble plot` is a variation of the `scatter plot` that displays three dimensions of data (x, y, z)
- The data points are replaced with bubbles, and the size of the bubble is determined by the third variable `z`, also known as the weight
- In `maplotlib`, we can pass in an array or scalar to the parameter `s` to `plot()`, that contains the weight of each point

```python
# Sample data
data = {
    'Years': [2000, 2005, 2010, 2015, 2020],
    'Values': [100, 200, 300, 400, 500],
    'Growth': [1.2, 2.5, 3.0, 4.2, 5.5]  # This will be represented by bubble size
}
df = pd.DataFrame(data)

# Create a bubble plot
# ax = df.plot(kind='scatter', x='Years', y='Values', s=df['Growth']*100, alpha=0.5, c='blue', edgecolor='w', linewidth=1.2)

plt.scatter(df['Years'], df['Values'], s=df['Growth']*100, alpha=0.5, c='blue', edgecolors='w', linewidth=1.5)

# plt.figure(figsize=(10, 6))
plt.xlabel('Years')
plt.ylabel('Values')
plt.title('Bubble Plot of Growth Over Years')
plt.show()
```
![bubble](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXYxaGkzy6WTwyLlCvgKv3QRXjQM3yO6Evng&s)

# **03 Extra Visualization Tools**
## Waffle Charts
- A waffle chart is a type of visualization that uses a grid of squares to represent data in a percentage format
- Each square in the grid represents a fraction of the total, making it easy to visualize parts-to-whole relationships
- Waffle charts are particularly useful for displaying progress towards a goal, comparing different categories, or illustrating proportions
#### Structure of a Waffle Chart
- **Grid Layout** : Typically a 10x10 grid (100 squares) is used, where each square represents 1% of the total. This can be adjusted based on the desired precision and visual preference.
- **Colored Squares** : Different colors are used to represent different categories or segments.
- **Labels** : Categories and percentages are often labeled for clarity

![Waffle Chart](https://python-charts.com/en/part-whole/waffle-chart-matplotlib_files/figure-html/waffle-chart-title-matplotlib.png)
#### Steps to create Waffle Charts
- The first step into creating a waffle chart is determing the proportion of each category with respect to the total
- The second step is defining the overall size of the `waffle` chart
- The third step is using the proportion of each category to determe it respective number of tiles
- The fourth step is creating a matrix that resembles the `waffle` chart and populating it
- Map the `waffle` chart matrix into a visual
- Prettify the chart
- Create a legend and add it to chart

```python
# Define the data
data = {
    'Asia Pacific': 32,
    'Australasia': 6,
    'Eastern Europe': 6,
    'Latin America': 8,
    'Middle East and Africa': 9,
    'North America': 10,
    'Western Europe': 29
}

# Define the color for each category
colors = {
    'Asia Pacific': '#17becf',
    'Australasia': '#ff7f0e',
    'Eastern Europe': '#2ca02c',
    'Latin America': '#d62728',
    'Middle East and Africa': '#9467bd',
    'North America': '#8c564b',
    'Western Europe': '#1f77b4'
}

# Create the waffle chart
fig, ax = plt.subplots(figsize=(10, 6))

# Number of rows and columns
n_rows = 10
n_cols = 10

# Plot each category
category_index = 0
current_pos = 0
for category, count in data.items():
    for i in range(count):
        row = current_pos // n_cols
        col = current_pos % n_cols
        rect = patches.Rectangle((col, n_rows - 1 - row), 1, 1, facecolor=colors[category], edgecolor='black', linewidth=1)
        ax.add_patch(rect)
        current_pos += 1
    category_index += 1

# Create legend
legend_handles = [patches.Patch(color=color, label=category) for category, color in colors.items()]
ax.legend(handles=legend_handles, loc='upper right', bbox_to_anchor=(1.3, 1))

# Set limits and aspect
ax.set_xlim(0, n_cols)
ax.set_ylim(0, n_rows)
ax.set_aspect('equal')

# Remove axes
ax.set_xticks([])
ax.set_yticks([])

plt.title('Where Are the Top 100 City Destinations?')
plt.show()
```


## WordClouds
- A word cloud (or tag cloud) is a visual representation of text data, where the size of each word indicates its frequency or importance within a given dataset
- Words that appear more frequently in the source text are displayed in larger fonts, while less common words are shown in smaller sizes
- Word clouds are often used to highlight prominent themes, topics, or keywords in various types of content
- **Social media posts :** To visualize popular topics or sentiments
- **Survey responses :** To summarize open-ended feedback
- **Articles or essays :** To highlight main ideas or topics
- Creating a word cloud typically involves text processing steps like tokenization (splitting text into words), removing common stop words (like "the," "and," etc.), and counting the occurrences of each word

```python
from wordcloud import WordCloud
```

```python
# Sample text
text = """
Artificial intelligence is transforming industries. Machine learning is a key component of AI. 
Many companies are adopting AI technologies to enhance efficiency and innovation.
"""

# Create a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide the axes
plt.show()
```
![word cloud](https://python-charts.com/en/ranking/wordcloud-matplotlib_files/figure-html/wordcloud-matplotlib.png)

## Regression plots
- Graphical representations that illustrate the relationship between a dependent variable and one or more independent variables using regression analysis
- These plots help visualize how the dependent variable changes as the independent variable(s) vary, allowing for better understanding and interpretation of the underlying patterns in the data
- Types of Regression plots
	- Scatter Plot with Regression Line
	- Multiple Regression Plots
	- Residual Plots

![reg plot](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlP51ss6cM-QchVDLHBkXYpn4fVTi15r27ig&s)
# **04 Creating Maps and Visualizing Geospatial Data**
## Folium
- Folium is a powerful Python library that helps you create several types of Leaflet maps
- The fact that the Folium results are interactive makes this library very useful for dashboard building
- Folium builds on the data wrangling strengths of the Python ecosystem and the mapping strengths of the Leaflet.js library. Manipulate your data in Python, then visualize it in on a Leaflet map via Folium
- Folium makes it easy to visualize data that's been manipulated in Python on an interactive Leaflet map. It enables both the binding of data to a map for choropleth visualizations as well as passing Vincent/Vega visualizations as markers on the map
- The library has a number of built-in tilesets from OpenStreetMap, Mapbox, and Stamen, and supports custom tilesets with Mapbox or Cloudmade API keys. Folium supports both GeoJSON and TopoJSON overlays, as well as the binding of data to those overlays to create choropleth maps with color-brewer color schemes

```python
import folium
```

```python
# define the world map
world_map = folium.Map()

# display world map
world_map
```

```python
# define the world map centered around India with a low zoom level
world_map = folium.Map(location=[20.5937, 78.9629], zoom_start=4)

# display world map
world_map
```

### Stamen Toner Maps
- These are high-contrast B+W (black and white) maps
- They are perfect for data mashups and exploring river meanders and coastal zones

![stamen toner](https://media.geeksforgeeks.org/wp-content/uploads/20200527003144/ss12.jpg)

```python
india_map = folium.Map(location=[20.5937, 78.9629], zoom_start=4, tiles='Stamen Toner', attr='Stamen Toner')

india_map
```

### Stamen Terrain Maps
- These are maps that feature hill shading and natural vegetation colors
- They showcase advanced labeling and linework generalization of dual-carriageway roads

![stamen terrain](https://media.geeksforgeeks.org/wp-content/uploads/20200527003147/ss23.jpg)

```python
india_map = folium.Map(location=[20.5937, 78.9629], zoom_start=4, tiles='Stamen Terrain', attr='Stamen Terrain')
```

### Maps with Markers

```python
# Create a map centered on India
india_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)
# Add markers to the map
folium.Marker( 
	location=[8.5241, 76.9366], 
	popup='Thiruvananthapuram', 
	icon=folium.Icon(icon='cloud') 
).add_to(kerala_map)
```

## Choropleth Maps
- A `Choropleth` map is a thematic map in which areas are shaded or patterned in proportion to the measurement of the statistical variable being displayed on the map, such as population density or per-capita income
- The choropleth map provides an easy way to visualize how a measurement varies across a geographic area, or it shows the level of variability within a region

![Choropleth Map](data:image/jpeg;base64,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)

```python
import folium
import pandas as pd
import requests

# Sample data for state populations (example values)
data = {
    'State': ['Kerala', 'Maharashtra', 'Tamil Nadu', 'Karnataka', 'Uttar Pradesh'],
    'Population_Density': [859, 365, 550, 319, 828]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a base map centered on India
india_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Download the GeoJSON data for Indian states
geojson_url = 'https://raw.githubusercontent.com/geohacker/india/master/state/india_telengana.geojson'
geojson_data = requests.get(geojson_url).json()

# Add the Choropleth layer
choropleth = folium.Choropleth(
    geo_data=geojson_data,
    data=df,
    columns=['State', 'Population_Density'],
    key_on='feature.properties.NAME_1',
    fill_color='YlGnBu',  # Color palette
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Population Density (per sq. km)',
).add_to(india_map)

# Add layer control
folium.LayerControl().add_to(india_map)
india_map
```