FROM ubuntu:latest

RUN  apt-get update
RUN apt-get install python3 -y
RUN apt-get install libffi-dev libsndfile1 -y
RUN apt install python3-pip -y
RUN  pip3 install numpy scipy matplotlib
RUN  pip3 install cffi pysoundfile
WORKDIR /app
COPY ./8_1.py  8_1.py
COPY ./8_2_1.py 8_2_1.py
COPY ./8_2_3.py 8_2_3.py
COPY ./8_2_2.py 8_2_2.py
COPY ./Sound_Noise.wav  Sound_Noise.wav
RUN python3 8_2_1.py
RUN python3 8_2_2.py
RUN python3 8_2_3.py
CMD ["python3","8_1.py"]
