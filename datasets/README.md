# Data download guide
## Demo data
The data used for *in silico* histopathological staining come in three sets: **trainA, trainB, testA**. We provide a download link for each set.
- trainA (URL: https://zenodo.org/record/8375712/files/trainA.rar?download=1)
- trainB (URL: https://zenodo.org/record/8375712/files/trainB.rar?download=1)
- testA (URL: https://zenodo.org/record/8375712/files/testA.rar?download=1)

Once downloaded, these compressed files (`*.rar`) should be extracted into this directory (`/UTOM/datasets`) for model training. A Matlab script describing how we split original big images is also provided here for reference, which can be used to stitch together those small images in **testA** without any modification.
- stitch_testA.m (URL: https://zenodo.org/record/8375712/files/stitch_testA.m?download=1).

## Complete dataset
1. Images (tif files of relevant tissue cores) after format conversion and screening can be downloaded from:
- Colorectal-AF&HE-tif (URL: https://zenodo.org/record/8375712/files/Colorectal-AF%26HE-tif.rar?download=1)

2. **Whole-slide pathological images** (colorectal cancer, only partially used in this study) without screening and preprocessing can be downloaded from:
- Colorectal-AF&HE-raw (URL: https://zenodo.org/record/8375712/files/Colorectal-AF-HE-raw.rar?download=1)
You can use the [QuPath](https://qupath.github.io/) software to open and view these files. 

3. **Whole-slide pathological images of various kinds of cancers** (not used in this study) can be downloaded from:
- All-AF&HE-raw (URL: https://cloud.tsinghua.edu.cn/d/94a403f5bcea49fba572/)
You can use the [QuPath](https://qupath.github.io/) software to open and view these files. 

If your Chrome misunderstands the security of the download, you can change its security settings or use other browsers.

## Citation
If you use these data, please cite the corresponding paper: 

["Li, X., Zhang, G., Qiao, H., ..., Wang, H., & Dai, Q. (2021). Unsupervised content-preserving transformation for optical microscopy. Light: Science & Applications, 10(1), 1-11.".](https://www.nature.com/articles/s41377-021-00484-y)
