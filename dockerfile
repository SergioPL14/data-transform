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

#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "datatransform/data_transform.py"]