1. Download and Install Driver at: https://www.geforce.com/drivers
2. Download and Install Visual Studio 2013 or 2015:
3. Download and Install Cuda and Cuda patch update:
Cuda 80: https://developer.nvidia.com/cuda-80-ga2-download-archive
Or Cuda 90: https://developer.nvidia.com/cuda-90-download-archive
! Notice: When install cuda, Make sure to select custom installation to NOT re-install Nvidia Driver.
4. Download and Copy Cudnn with respond to Cuda to Cuda installed folder: 
5. Config the Environment Variables according this: https://medium.com/@minhplayer95/how-to-install-tensorflow-with-gpu-support-on-windows-10-with-anaconda-4e80a8beaaf0
6. Download and Install Anaconda:
7. Create new environment then activate it:
conda create --name NAME python=3.6 numpy scipy matplotlib pandas
activate NAME
8. Install tensorflow:
pip install http://download.pytorch.org/whl/cu90/torch-0.4.1-cp36-cp36m-win_amd64.whl
pip install torchvision
pip install keras
pip install autokeras
pip install --upgrade tensorflow-gpu