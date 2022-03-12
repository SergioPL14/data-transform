#Deriving the latest base image
FROM python:latest


#Labels as key value pair
LABEL Maintainer="sergio.pina"


# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /usr/src/app

#to COPY code at working directory in container
COPY . /usr/src/app/

#Install requirements dependencies
RUN pip install -r requirements.txt

# RUN chmod +x inputs/cleaning_json

#CMD instruction to run the software
CMD [ "python", "datatransform/data_transform.py", "inputs/cleaning.json"]