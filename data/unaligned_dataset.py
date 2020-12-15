import os.path
from data.base_dataset import BaseDataset, get_transform, new_transformA, new_transformB
from data.image_folder import make_dataset
from PIL import Image
import random
from libtiff import TIFF, TIFFimage
import tifffile as tiff
import torch
import numpy as np


class UnalignedDataset(BaseDataset):
    """
    This dataset class can load unaligned/unpaired datasets.

    It requires two directories to host training images from domain A '/path/to/data/trainA'
    and from domain B '/path/to/data/trainB' respectively.
    You can train the model with the dataset flag '--dataroot /path/to/data'.
    Similarly, you need to prepare two directories:
    '/path/to/data/testA' and '/path/to/data/testB' during test time.
    """

    def __init__(self, opt):
        """Initialize this dataset class.

        Parameters:
            opt (Option class) -- stores all the experiment flags; needs to be a subclass of BaseOptions
        """
        BaseDataset.__init__(self, opt)
        self.dir_A = os.path.join(opt.dataroot, opt.phase + 'A')  # create a path '/path/to/data/trainA'
        self.dir_B = os.path.join(opt.dataroot, opt.phase + 'B')  # create a path '/path/to/data/trainB'

        self.A_paths = sorted(make_dataset(self.dir_A, opt.max_dataset_size))   # load images from '/path/to/data/trainA'
        self.B_paths = sorted(make_dataset(self.dir_B, opt.max_dataset_size))    # load images from '/path/to/data/trainB'
        self.A_size = len(self.A_paths)  # get the size of dataset A
        self.B_size = len(self.B_paths)  # get the size of dataset B
        btoA = self.opt.direction == 'BtoA'
        input_nc = self.opt.output_nc if btoA else self.opt.input_nc       # get the number of channels of input image
        output_nc = self.opt.input_nc if btoA else self.opt.output_nc      # get the number of channels of output image
        self.transform_A = get_transform(self.opt, grayscale=(input_nc == 1))
        self.transform_B = get_transform(self.opt, grayscale=(output_nc == 1))
        self.new_transform_A = new_transformA(self.opt, grayscale=(input_nc == 1))
        self.new_transform_B = new_transformB(self.opt, grayscale=(output_nc == 1))
        self.opt = opt

    def __getitem__(self, index):
        """Return a data point and its metadata information.

        Parameters:
            index (int)      -- a random integer for data indexing

        Returns a dictionary that contains A, B, A_paths and B_paths
            A (tensor)       -- an image in the input domain
            B (tensor)       -- its corresponding image in the target domain
            A_paths (str)    -- image paths
            B_paths (str)    -- image paths
        """
        A_path = self.A_paths[index % self.A_size]  # make sure index is within then range
        if self.opt.serial_batches:   # make sure index is within then range
            index_B = index % self.B_size
        else:   # randomize the index for domain B to avoid fixed pairs.
            index_B = random.randint(0, self.B_size - 1)
        B_path = self.B_paths[index_B]
        # A_img = Image.open(A_path).convert('RGB')
        # B_img = Image.open(B_path).convert('RGB')

        # print('A_path ----->',A_path)
        # print('B_path ----->',B_path)
        A_img = tiff.imread(A_path).astype(np.float32)
        B_img = tiff.imread(B_path).astype(np.float32)
        # print('A_path ----->',A_path)
        # print('B_path ----->',B_path)
        # apply image transformation
        # A = self.transform_A(A_img)
        # B = self.transform_B(B_img)

        A_img1 = torch.from_numpy(A_img)
        B_img1 = torch.from_numpy(B_img)
        # print('A_img1_shape ----->',A_img1.shape)
        # print('B_img1_shape ----->',B_img1.shape)
        # print('A_img1_shape ----->',len(A_img1.shape))
        # print('A_img1_shape ----->',len(B_img1.shape))

        if len(A_img1.shape)==3:
            # A_img2 = A_img1.permute(1, 2, 0).numpy()
            A_img2 = A_img1.numpy()/(self.opt.trainA_normalize/255)
        elif len(A_img1.shape)==2:
            A_img2 = A_img1.unsqueeze(2).numpy()/(self.opt.trainA_normalize/255)

        if len(B_img1.shape)==3:
            # B_img2 = B_img1.permute(1, 2, 0).numpy()
            B_img2 = B_img1.numpy()/(self.opt.trainB_normalize/255)
        elif len(B_img1.shape)==2:
            B_img2 = B_img1.unsqueeze(2).numpy()/(self.opt.trainB_normalize/255)
        # print('A_img2_shape ----->',A_img2.shape)
        # print('B_img2_shape ----->',B_img2.shape)
        # print('A_img2 -----> ',A_img2.max(),' ----- ',A_img2.min())
        # print('B_img2 -----> ',B_img2.max(),' ----- ',B_img2.min())

        # A = self.new_transform_A(A_img2)
        # B = self.new_transform_B(B_img2)
        A_img2 = A_img2/127.5-1
        B_img2 = B_img2/127.5-1
        A = torch.from_numpy(A_img2).permute(2, 0, 1)
        B = torch.from_numpy(B_img2).permute(2, 0, 1)
        # print('A shape ----->',A.shape)
        # print('B shape ----->',B.shape)
        # print('A -----> ',A.max(),' ----- ',A.min())
        # print('B -----> ',B.max(),' ----- ',B.min())

        return {'A': A, 'B': B, 'A_paths': A_path, 'B_paths': B_path}

    def __len__(self):
        """Return the total number of images in the dataset.

        As we have two datasets with potentially different number of images,
        we take a maximum of
        """
        return max(self.A_size, self.B_size)
