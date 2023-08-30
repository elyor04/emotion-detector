# emotion-detector
* ### Works on Linux, Windows and MacOS


<div align="center">
<h2>How does the program look like?</h2>
<a href="https://imgtr.ee/image/AKxys"><img src="https://imgtr.ee/images/2023/08/30/978a55cda6c7d8415cc57f78eaf04324.th.gif" alt="Emotions" border="0" width="100%" height="100%"></a><br>
</div>


## Install for CPU

### Install the libraries
```
pip install --upgrade tensorflow opencv-python matplotlib scipy
```


## Install for GPU

* ### First install Tensorflow with GPU support [here](https://www.tensorflow.org/install/pip)
* ### Since you have installed Tensorflow, it's time to install OpenCV with GPU support

## On Linux

### Install NVIDIA GPU driver and reboot, if you still don't have it
* WARNING: if you don't have NVIDIA GPU, please skip this part
* NOTE: you can choose driver version yourself, by default I gave 525
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

### Install OpenCV and extra-libraries
```
pip install --upgrade opencv-python matplotlib scipy
```

## On the other platforms

### Install OpenCV and extra-libraries
```
pip install --upgrade opencv-python matplotlib scipy
```
