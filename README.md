# emotion-detector
* ### Works on Linux, Windows, MacOS and other platforms


## Install for CPU
```
pip install --upgrade tensorflow opencv-python
```


## Install for GPU

* ### First install Tensorflow with GPU support [here](https://medium.com/nerd-for-tech/installing-tensorflow-with-gpu-acceleration-on-linux-f3f55dd15a9) or [here](https://www.tensorflow.org/install/pip)
* ### Since you have installed Tensorflow, it's time to install OpenCV with GPU support

## On Linux

### Install NVIDIA GPU driver and reboot, if you still don't have it
* WARNING: if you don't have NVIDIA GPU, please skip this part
* NOTE: you should choose the latest driver version yourself, by default I gave 525
* search for the driver versions by running `apt-cache search --names-only "^nvidia-driver-[0-9]{3}$"`
```
sudo apt -y install nvidia-driver-525
sudo reboot
```
* check the installation by running `nvidia-smi`

### Install Intel GPU driver, just in case
* WARNING: if you don't have Intel GPU, please skip this part
```
sudo apt -y install intel-opencl-icd
```

### Install OpenCL libraries
```
sudo apt -y install opencl-headers ocl-icd-libopencl1 ocl-icd-opencl-dev clinfo
```
* check GPU drivers list by running `clinfo -l` (at least you should have one)

### Install OpenCV
```
pip install --upgrade opencv-python
```
