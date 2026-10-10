**'pipeline.py' Description:**

The 'pipeline.py' file is the end-to-end general organizer and processer that imports modules, defines parser arguments and 
establishes the order of runs based on the command prompt commands. This program allows the user to input data and process 
based on their own configuration rules all in one. Outputted data files have a wide range of processing 
from removing duplicates, outliers, and more.

Limited action is required from the user as the pipeline utilizes modules that will identify file types, 
and import according to those types.

Below are high level steps on the actions taken by this pipeline. 

Steps:

1. Establishes parser arguments into a variable 
2. Validates and loads inputs and outputs from the user 
3. Validates & processes the data being imported 
4. Saves processed data & exports as a CSV
5. Prints cleaning report
