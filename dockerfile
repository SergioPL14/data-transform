#Deriving the latest base image
FROM python:latest

#Labels as key value pair
LABEL Maintainer="sergio.pina"

#to COPY code at working directory in container
COPY . ./

#Install requirements dependencies
RUN pip install -r requirements.txt

# RUN chmod +x inputs/cleaning_json

#CMD instruction to run the software
CMD [ "python", "./data_transform.py", "./resources/inputs/clean_bookings.json"]