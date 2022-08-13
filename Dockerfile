#Deriving the python 3.10 base image
FROM python:3.10-slim

#Labels as key value pair
LABEL Maintainer="soumyaXXXXXXX@gmail.com"

# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/sec
WORKDIR /usr/app/src

#to COPY the remote file at working directory in container
COPY features/ ./features
COPY behave.ini behave.ini
COPY requirements.txt requirements.txt
RUN ls -l
# Install dependencies
RUN pip install -r requirements.txt

#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

# To execute docker with diffrent feature file
# docker run -it bdd-test features/user_api.feature
# docker run -it bdd-test features/user_api.feature --tags=CreateUser
ENTRYPOINT ["behave"]
CMD [ "features"]