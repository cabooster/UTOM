# Data download guide
## Demo data
The data used for *in silico* histogical staining come in three sets: **trainA, trainB, testA**. We provide download links for each set.
- trainA (URL: https://cloud.tsinghua.edu.cn/f/fa25d75a1fcd41cc88d5/?dl=1)
- trainB (URL: https://cloud.tsinghua.edu.cn/f/6e6d6fbc588b4719a9c0/?dl=1)
- testA (URL https://cloud.tsinghua.edu.cn/f/bc51e8062b6940db8abf/?dl=1)

Once downloaded, these compressed files (.zip) should be extracted into this directory for model training. A Matlab script describing how we split original big images were also provided here for reference, which can be used for image stitching with minor modifications.
- stitch_testA.m (URL: https://cloud.tsinghua.edu.cn/f/a76d60ebb00240129511/?dl=1)

## Complete dataset
The complete **raw data** without screening and preprocessing can be downloaded from:
- Colorectal-AF&HE (URL: https://cloud.tsinghua.edu.cn/f/6d17f1c642d442afbe65/?dl=1)
You can use the [QuPath](https://qupath.github.io/) software to open and view these files. 

If your Chrome misunderstands the security of the download, you can change its security settings or use other browsers.

## Citation
If you use these data, please cite the corresponding paper: 

["Li, X., Zhang, G., Qiao, H., Bao, F., Deng, Y., Wu, J., ... & Dai, Q. (2021). Unsupervised content-preserving transformation for optical microscopy. Light: Science & Applications, 10(1), 1-11.".](https://www.nature.com/articles/s41377-021-00484-y)

