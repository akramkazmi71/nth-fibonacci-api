FROM django

WORKDIR /home

RUN apt-get update && apt-get install -y git

RUN git clone https://github.com/akramkazmi71/nth-fibonacci-api

WORKDIR /home/nth-fibonacci-api

#RUN pip3 install -r requirements.txt
#RUN pip3 install django --upgrade

CMD [ "python3", "manage.py runserver 0.0.0.0:8000" ]

