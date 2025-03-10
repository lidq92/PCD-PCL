# PCD-PCL
 A High-Quality Colored Point Cloud Dataset Provided by Peng Cheng Laboratory (mainly for AVS PCC and PCQA)

## How we get the colored point clouds? 
1. Open [SketchFab](https://sketchfab.com) -> Explore -> Downloadable -> Filters (**LICENSES: CC BY & CC BY-SA & CC0**) -> CATEGORIES (e.g., Cultural Heritage & History) -> Choose high-quality 3D mesh models with diverse contents -> Download glTF files (Thanks for the providers of these 3D models!)
2. Open them with *Blender* and save them as *.obj file
3. Method 1: Use *MeshLab* **texel sampling** (where texture resolution=*4096*) to generate the sampled point clouds, and save them as *.ply files (with the alpha information removed); Method 2: Use *CloudCompare* **Sample Points** to generate point clouds based on *Points Number* or *Density*
4. To use them as the input for AVS-PCC PCRM or MPEG G-PCC, use `quantization_process.py` for quantizing them to a suitable level (where a further quantization will lose many points).

## Link to download the dataset
url: [PCD-PCL](https://pan.baidu.com/s/1I2hgnW4Xepaq6oMTVtAT0g?pwd=cyb5) includes a total of 80 static point clouds.

## Citation
If you use this dataset for your research, please cite it as follows.
```
@misc{pcd-pcl,
    author= {Li, Dingquan and Wang, Jing and Li, Ge},
    year  = {2022},
    title = {A High-Quality Colored Point Cloud Dataset},
    note  = {\url{https://github.com/lidq92/PCD-PCL}, 
             Last accessed on 2022-06-23},
}
```
