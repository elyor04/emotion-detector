# emotion-detector
* ### works on linux, windows, macos and other platforms


## Install for CPU
```
pip install --upgrade tensorflow opencv-python
```


## Install for GPU

## On Linux

### Install miniconda, if you don't have it
```
sudo apt -y install curl
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
source ~/.bashrc
```

### Install NVIDIA GPU driver and reboot, if you don't have it
* NOTE: you can choose the driver version yourself, by default I gave 450
* search for the driver versions by running `apt search nvidia-driver`
```
sudo apt -y install nvidia-driver-450
sudo reboot
```
* check the installation by running `nvidia-smi`

### Install CUDA and cuDNN with conda and pip
```
conda install -c conda-forge cudatoolkit=11.8.0
pip install --upgrade nvidia-cudnn-cu11==8.6.0.163
```

### Configure the system paths
```
mkdir -p $CONDA_PREFIX/etc/conda/activate.d
echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
echo 'export LD_LIBRARY_PATH=$CUDNN_PATH/lib:$CONDA_PREFIX/lib/:$LD_LIBRARY_PATH' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
source $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
```

### Upgrade your pip installation
```
python3 -m pip install --upgrade pip
```

### Install OpenCL libraries to make OpenCV faster
```
sudo apt -y install opencl-headers ocl-icd-libopencl1 ocl-icd-opencl-dev
```

### Install TensorFlow and OpenCV
```
pip install --upgrade tensorflow==2.13.* opencv-python
```
