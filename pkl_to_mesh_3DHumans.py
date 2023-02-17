import sys
import pickle
import numpy as np
import smplx
import torch
import trimesh
from copy import deepcopy
from psbody.mesh import Mesh
import cv2
import os
import natsort
from tqdm import tqdm

def get_param(path):
    with open(path, 'rb') as fi:
        d = pickle.load(fi)
    scale = d['body_scale']
    pose = d['body_pose'][0]
    beta = d['betas'][0]
    trans = d['global_body_translation']
    pose_embedding = d['body_pose_embedding']
    return pose_embedding, scale, pose, beta, trans

if __name__ == '__main__':
    
    dataset_dir = '3DHumans' + '/'
    smpl_models_dir = 'models/' 

    scans = natsort.natsorted(os.listdir(dataset_dir))

    for scan in tqdm(scans):
        actual_scan = natsort.natsorted(os.listdir(dataset_dir + scan))
        id = actual_scan[0][:-4]
        scan_smpl_path = dataset_dir + scan + '/' + id + '_SMPL_neutral.pkl'

        model = smplx.create(smpl_models_dir, create_global_orient = True, create_body_pose = False, create_betas = True, model_type='smpl', gender='neutral', create_transl = False, create_left_hand_pose= True, create_right_hand_pose = True, create_expression = True, create_jaw_pose = True, create_leye_pose = True, create_reye_pose = True, )
        pose_embedding, scale,  pose, beta, trans = get_param(scan_smpl_path)
        go = torch.tensor(pose[:3]).unsqueeze(0)
        pose = torch.tensor(pose[3:]).float().unsqueeze(0)
        beta = torch.tensor(beta).float().unsqueeze(0)
        output = model(betas=beta,  body_pose = pose, global_orient=go, return_verts=True)
        vert = output.vertices[0]
        vert = vert.detach().numpy()

        outdir = dataset_dir + scan 

        mesh = Mesh()
        vert = vert*scale
        vert += trans
        mesh.v = vert
        mesh.f = model.faces
        mesh.write_obj(outdir + '/smpl_mesh_neutral.obj')
