import os
os.system('source activate pytorch')

# os.system('python train.py --dataroot ./datasets/AF2HE_datasets --name AF2HE --model cycle_gan --input_nc 1 --output_nc 3 \
#  --lambda_identity 0.0 --gpu_ids 4 --load_size 512 --crop_size 512 --display_winsize 512')

os.system('python test.py --dataroot ./datasets/AF2HE_datasets --name AF2HE --model cycle_gan --input_nc 1 --output_nc 3 \
    --gpu_ids 4 --load_size 512 --crop_size 512 --display_winsize 512 --num_test 100')