FROM tensorflow/tensorflow:latest

RUN apt-get update && apt-get install -yq python3 python3-dev nvidia-361-dev
RUN DEBIAN_FRONTEND=noninteractive apt-get -yq install python3-pip
RUN apt install -y nvidia-kernel-source-460
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
# RUN mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
# RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub
# RUN add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
# RUN apt-get update


COPY . .

EXPOSE 5000

CMD ["python3", "uploader.py"]