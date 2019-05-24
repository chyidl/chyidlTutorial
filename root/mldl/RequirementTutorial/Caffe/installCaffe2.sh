sudo apt-get -y update
sudo apt-get install -y --no-install-recommends \
      build-essential \
      git \
      libgoogle-glog-dev \
      libgtest-dev \
      libiomp-dev \
      libleveldb-dev \
      liblmdb-dev \
      libopencv-dev \
      libopenmpi-dev \
      libsnappy-dev \
      libprotobuf-dev \
      openmpi-bin \
      openmpi-doc \
      protobuf-compiler \
      python3-dev \
      python3-pip
sudo -H python3 -m pip install \
      future \
      numpy \
      protobuf \
      typing \
      hypothesis

# for Ubuntu 18.04
sudo apt-get install -y --no-install-recommends \
    libgflags-dev \
    cmake

