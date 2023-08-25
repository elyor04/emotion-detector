# emotion-detector
* ### Works on linux, windows, macos and other platforms


## Install for CPU
```
pip install --upgrade tensorflow opencv-python
```


## Install for GPU

* ### First install Tensorflow with GPU support [here](https://www.tensorflow.org/install/pip)
* ### Since you have installed Tensorflow, it's time to install OpenCV with GPU support

## On Linux

### Install NVIDIA GPU driver and reboot, if you still don't have it
* NOTE: you can choose the driver version yourself, by default I gave 510
* search for the driver versions by running `apt search nvidia-driver`
```
sudo apt -y install nvidia-driver-510
sudo reboot
```
* check the installation by running `nvidia-smi`

### Install OpenCL libraries to make OpenCV faster
```
sudo apt -y install opencl-headers ocl-icd-libopencl1 ocl-icd-opencl-dev intel-opencl-icd clinfo
```
* check GPU drivers list by running `clinfo -l` (at least you should have one)

### Install OpenCV
```
pip install --upgrade opencv-python
```
