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
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

### Install NVIDIA GPU driver and reboot, if you don't have it
* NOTE: you can choose the driver version yourself, by default I gave 450
* search for the driver versions by running `apt search nvidia-driver`
```
sudo apt -y install nvidia-driver-450
sudo reboot
```
* check the installation by running `nvidia-smi`
