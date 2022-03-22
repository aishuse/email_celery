
#Use the Python3.7.2 container image


#Copy the current directory contents into the container.
COPY . /usr/src/app   

#Set the working directory to /usr/src/app
WORKDIR /usr/src/app

#Install the dependencies
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput
