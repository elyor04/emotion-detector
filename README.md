# emotion-detector
* ### works on linux, windows, macos and other platforms


## Install for CPU
```
pip install --upgrade tensorflow opencv-python
```


## Install for GPU

## On Linux (Ubuntu 16.04 64-bit or higher)

### Install miniconda, if you don't have it
```
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

### Install NVIDIA GPU driver and reboot
* NOTE: you should choose the driver version yourself, by default I gave 450
* you can see the available driver versions by running ``
```
sudo apt -y install nvidia-driver-450
sudo reboot
```
