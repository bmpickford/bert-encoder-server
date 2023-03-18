FROM nvidia/cuda:12.1.0-base-ubuntu18.04

# Install some basic utilities
RUN apt-get update && apt-get install python3 python3-pip -y

# Install some basic utilities
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    sudo \
    git \
    bzip2 \
    libx11-6 \
    build-essential \
    wget \
    unzip \
 && rm -rf /var/lib/apt/lists/*

# Install OpenCV3 Python bindings
RUN sudo apt-get update

# Create a working directory
RUN mkdir /app

# Add requirements file
WORKDIR /app/
ADD requirements.txt /app/

# Install requirements
RUN pip3 install pip -U
RUN pip3 install -r requirements.txt

# Download Sentence Transformers Model
RUN python3 -c "import os; from sentence_transformers import SentenceTransformer; SentenceTransformer(os.environ.get('MODEL', 'all-MiniLM-L6-v2'));"

# Move required resources                     
ADD app.py /app/

EXPOSE 5000

# Run flask api
ENTRYPOINT ["python3"]
CMD ["app.py"]
