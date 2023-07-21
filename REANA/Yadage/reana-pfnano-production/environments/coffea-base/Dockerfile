# Start from the ROOT6 base image:
FROM coffeateam/coffea-base:0.7.21-fastjet-3.4.0.1

RUN apt-get -y update && \
    apt-get -y install \
       libyaml-dev \
       python-numpy \
       zip && \
    apt-get autoremove -y && \
    apt-get clean -y
RUN pip install hftools==0.0.6

# Mount our code:
ADD code /code
WORKDIR /code