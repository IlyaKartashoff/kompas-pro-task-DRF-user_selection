FROM python

WORKDIR /usr/src/dp_rest

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . /usr/src/dp_rest

EXPOSE 8000

CMD [ "python", "manage.py", "migrate" ]

