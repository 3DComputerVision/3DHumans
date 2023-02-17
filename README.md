# 3DHumans
This repo contains post-processing scripts for 3DHumans Dataset.

Request the 3DHumans dataset from this [link](https://cvit.iiit.ac.in/research/projects/cvit-projects/3dhumans). Upon recieving the download link, download the dataset, unzip and put all the files inside "/path/to/3DHumans" directory

## Generating registered SMPL meshes
Download the SMPL models from [here](https://smpl.is.tue.mpg.de/index.html), and place the files inside "/path/to/models" directory.<br/>
<br/>
Install 'smplx' via pip.<br/>
``` pip install smplx[all] ```
<br/>
<br/>
Replace the paths mentioned in [pkl_to_mesh_3DHumans.py](https://github.com/3DComputerVision/3DHumans/blob/main/pkl_to_mesh_3DHumans.py) (lines 26 \& 27) with "/path/to/3DHumans" \& "/path/to/models", respectively.
