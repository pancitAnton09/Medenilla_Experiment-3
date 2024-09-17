# Medenilla_Experiment-3

## PYTHON DATA ANALYSIS (PANDAS)

### Intended Learning Outcomes:
1. To identify the codes and functions incorporated in the Pandas library
2. To be able to apply and use the different codes and functions in creating a Python program using a
Pandas library

## PROBLEM 1
Using knowledge obtained from the experiment and demonstrations:
#### a. Load the corresponding .csv file into a data frame named cars using pandas
#### b. Display the first five and last five rows of the resulting cars

```python
#Access pandas' function
import pandas as pd

#Load the car.csv file into DataFrame carlist
carlist = pd.read_csv('cars.csv')

#Display the first five rows of the resulting carlist ( using .head())
carlist.head()

#Display the last five rows of the resulting carlist (using .tail())
carlist.tail()
```

## PROBLEM 2
#### Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and
indexing operations.
##### a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
##### b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
##### c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
##### d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

```python
#Access pandas' function
import pandas as pd

# Using DataFrame carlist, extract the .csv file 
carlist = pd.read_csv('cars.csv')

# Display the first five rows with odd-numbered columns of cars.
## Slice the DataFrame, starting from row 1 with an increment of 2
### Then, use .head() to display first five rows
carlist[1::2].head()

# Use .loc to display the row that contains the ‘Model’ of ‘Mazda RX4’
## In this case row [0], and the column ['Model'] will be extracted
carlist.loc[[0],['Model']]

# Use .loc to determine how many cylinders does the 'Camaro Z28' have
## In this case row [23], and the columns ['Model', 'cyl'] will be extracted
carlist.loc[[23],['Model','cyl']]

# Use .loc to determine how many cylinders and what gear type do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
## In this case, rows [1,28,18] and columns ['Model', 'cyl', 'gear'] will be extracted
carlist.loc[[1,28,18],['Model', 'cyl', 'gear']]
```

## To Save file as .py
1. Click File
2. Click Save and Export Notebook As...
3. Click Executable Script
   
## Author
Medenilla, Jose Anton M.
