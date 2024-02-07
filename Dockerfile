FROM python

WORKDIR /the_menu

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
