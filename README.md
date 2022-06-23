# PCD-PCL
 A High-Quality Colored Point Cloud Dataset Provided by Peng Cheng Laboratory (mainly for AVS PCC and PCQA)

## How we get the colored point clouds? 
1. Open [SketchFab](https://sketchfab.com) -> Explore -> Downloadable -> Filters (LICENSES: CC BY & CC BY-SA & CC0) -> CATEGORIES (e.g., Cultural Heritage & History) -> Choose high-quality 3D mesh models with diverse contents -> Download glTF files
2. Open them with Blender and save them as *.obj file
3. Method 1: Use MeshLab GUI or command line to conduct **texel sampling** (where texture resolution=4096), and save the sampled point clouds as *.ply file, then remove the alpha information; Method 2: Use CloudCompare **Sample Points** to generate point clouds based on points number or density
4. To use them as the input for AVS-PCC PCRM or MPEG G-PCC, quantize them to a suitable level (where a further quantization will lose many points).

## Link to the dataset
url: [](), password: 