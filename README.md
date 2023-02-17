# 3DHumans
This repo contains post-processing scripts for 3DHumans Dataset.

Request the 3DHumans dataset from this [link](https://cvit.iiit.ac.in/research/projects/cvit-projects/3dhumans). Upon recieving the download link, download the dataset, unzip and put all the files inside "/path/to/3DHumans"

## Generating registered SMPL meshes
Download the SMPL models from [here](https://smpl.is.tue.mpg.de/index.html), and place the files inside "/path/to/models/" directory.<br/>
<br/>
Install 'smplx' via pip.<br/>
``` pip install smplx[all] ```
<br/>
<br/>
Modiy the lines 
