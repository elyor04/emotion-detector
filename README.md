# emotion-detector
* ### works on linux, windows, macos and other platforms


## Install for CPU
```
pip install --upgrade tensorflow opencv-python
```


## Install Tensorflow for GPU

### you can find the installations [here](https://www.tensorflow.org/install/pip)
since you have installed Tensorflow, it's time to install Opencv

## On Linux

### Install NVIDIA GPU driver and reboot, if you don't have it
* NOTE: you can choose the driver version yourself, by default I gave 510
* search for the driver versions by running `apt search nvidia-driver`
```
sudo apt -y install nvidia-driver-510
sudo reboot
```
* check the installation by running `nvidia-smi`

### Install OpenCL libraries to make OpenCV faster
```
sudo apt -y install opencl-headers ocl-icd-libopencl1 ocl-icd-opencl-dev
```

### Install OpenCV
```
pip install --upgrade tensorflow==2.13.* opencv-python
```
