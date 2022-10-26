You have been asked to design and develop a prototype application that demonstrates 
how data form the given data set can be formatted, cleaned, and used to generate 
specific outputs (as listed below).

Functional requirements

The application should provide the following functionality:

 A means to load the initial data set (which consists of three CSV files) and translate it 
into a suitable format, either XML, or JSON or an entity relationship structure (not 
CSV) 

 A means to back up the data in this format using either files or a database. This 
should preserve the current state of the data when the program is closed, and make 
it available when the program is reopened. 

 A process for cleaning and preparing the initial data set, managing inconsistences, 
errors, missing values and any specific changes required by the client (see below).

 A graphical user interface(s) for interacting with the data that enables the user to:

o Load and clean an initial data set (from the CV format)

o Load and save a prepared data set (from its translated format)

o Use the prepared data set to generate output and visualisations

o Manipulate the range of values used to generate output and visualisations

It should be assumed that this program will be able to handle other sets of data 
generated from the same source, i.e. data with the same column row headings but 
containing different values and anomalies. However, the application is not required to be 
generic (work with multiple unknown data sets). Given this best practice regarding code 
reuse, encapsulation and a well-defined programming interface should be applied where 
applicable.

Data manipulation and outputs:

The client initially wants the application to perform the following actions on the data:

1. Outputs should not include any data from airports that have a ‘type’ ‘closed’

2. The ‘type’ column contains information of the type of airport. Extract this out into

a new column, one for each category of airport, for:

a. all UK(GB) airports, that are , large_airport, medium_airport, small 
airport

b. join each category, large_airport, medium_airport, small airport
to the communication frequencies ‘ frequency_mhz’ that the airport uses 
for communication ensuring that each airport in all categories is correctly 
matched with its communication frequencies.

3. The client initially needs information to generate the following and output the 
results using appropriate representation:

a. Produce the mean, mode and median for the ‘frequency_mhz’
i. For large_airport

ii. For frequencies more than 100 mhz

4. Produce a suitable graph that display the communication frequencies used by 
‘small_airport’ You may need to consider how you group this data to make 
visualisation feasible

5. Determine if there is any significant correlation between the communication 
frequencies used by the 3 different categories of airport. ‘Are some frequencies 
used more than others?’. You will need to select an appropriate visualisation to 
demonstrate this.

Non-functional requirements
• The GUI interface provides appropriate feedback to confirm or deny a user’s actions
• The application manages internal and user-generated errors
