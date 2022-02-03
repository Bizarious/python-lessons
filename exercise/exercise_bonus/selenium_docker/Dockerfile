FROM archlinux:latest

RUN pacman -Sy --noconfirm
RUN pacman -S python python-pip --noconfirm

WORKDIR /home/tom
RUN mkdir volume
RUN touch volume/prices.txt
RUN mkdir src
WORKDIR src

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY main.py main.py
# COPY geckodriver geckodriver

# CMD ["python", "-u", "main.py"]