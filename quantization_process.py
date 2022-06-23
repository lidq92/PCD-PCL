import os
from pyntcloud import PyntCloud
import numpy as np
from glob import glob


def process(path, vox=12, is_mesh=False):
    pc_mesh = PyntCloud.from_file(path)
    mesh = pc_mesh.mesh
    coords = ['x', 'y', 'z']
    pc_mesh.points[coords] = pc_mesh.points[coords].astype('float64', copy=False)
    pc_mesh.mesh = mesh
    if is_mesh:
        pc = pc_mesh.get_sample("mesh_random", n=500000, as_PyntCloud=True)
    else:
        pc = pc_mesh
    points = pc.points[coords].values
    print(np.min(points, axis=0))
    points = points - np.min(points, axis=0, keepdims=True)
    print(np.min(points, axis=0))
    print(np.max(points, axis=0))
    print(np.max(points))
    points = points / np.max(points) # comment this to avoid the max dimension always equals to (2 ** vox - 1)
    points = points * (2 ** vox - 1)
    points = np.round(points) # after that, determine the geometry precision = np.log2(np.max(points)) ...
    # print(pc.points[coords])
    # print(points)
    pc.points[coords] = points
    colors = ['red', 'green', 'blue'] # ['green', 'blue', 'red'] it is order-sensitive, here needs the original order.
    other_scalars = list(set(pc.points.columns) - set(coords) - set(colors))
    # print(pc.points.shape)
    pc.points = pc.points.drop(columns=other_scalars)
    # print(pc.points.shape)
    pc.points[colors] = pc.points.groupby(by=coords).transform('mean').astype('uint8', copy=False)
    pc.points = pc.points.drop_duplicates()
    pc.to_file('{}_vox{}.ply'.format(path[:-4], vox))


print('Start!')
#seqs = glob('raw/*.ply', recursive=True)
for path in seqs:
    print(path)
    for vox in range(9,12):
        process(path, vox)