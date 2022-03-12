Data tansformation application
==============================


What Is This?
-------------

This is a simple Python application intended to provide a library of text based files transformations.
This application takes a JSON configuration file and a CSV file as inputs and generates an output file in JSONL or Parquet formats with the applied transformations to the original file.


How To Use This
---------------

1. Download or copy the repository from: https://github.com/SergioPL14/data-transform.git
2. Prepare the directory you will have the input and output files with the following structure:
    Directory
        inputs
        outputs
3. Prepare the JSON config file with the needed parameters (see example in /resources/inputs/clean_bookings.json
4. Install Docker (if needed in the host you are working).
5. Open a Windows CMD as administrator, run the following commands to build the image and run the application in Windows:
    a. docker build -t datatransform [path_to_the_repo]
        Example: docker build -t datatransform C:/Users/YourUser/Documents/data-transform
    b. docker run -d -v [path_to_local_directory]:/resources -t datatransform:latest
6. You should find the output file in the outputs folder.
