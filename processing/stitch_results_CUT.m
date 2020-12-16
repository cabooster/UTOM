clc;clear;
% stitch test results together
% overlap should be set

patch_size = 512;
overlap = 128;
fntif = './UTOM/images/';
fnrlt = './UTOM/';

% img_gt = im2uint8(loadtiff('./test-whole-slide/GT.tif'));

% get the list of all slides

for k = 1:14
    list = dir([fntif 'AF_' num2str(k) '_*.tif']);
    
    % figure out how many slides in the folder
    raw_name = list(end).name;
    % cell_str = strsplit(raw_name, '_');
    cell_str = strsplit(raw_name, '_');
    zs = 3;
    xs = str2num(cell_str{5});
    ys = str2num(cell_str{6});
    % buffer
    img_rlt = zeros(xs,ys,zs,'uint8');
    
    %% do stitching
    for i = 1:length(list)
        % stitching
        if mod(i, 100) ==0
            fprintf('Progress %d of %d ...\n', i, length(list))
        end
        
        img = imread(fullfile(list(i).folder, list(i).name));
        
        % get slide info;
        raw_name = list(i).name;
        cell_str = strsplit(raw_name, '_');
        
        xi = str2num(cell_str{3});
        yi = str2num(cell_str{4});
        
        if xi==1 || yi==1 || xi+patch_size-1==xs || yi+patch_size-1==ys
            
            xidx = xi;
            yidx = yi;
            imgP_net = img;
            img_rlt(xidx:xidx+patch_size-1, yidx:yidx+patch_size-1, :) = imgP_net;
            
        else
            
            xidx = xi+overlap/2;
            yidx = yi+overlap/2;
            imgP_net = img(overlap/2+1:end-overlap/2,overlap/2+1:end-overlap/2,:);
            img_rlt(xidx:xidx+patch_size-overlap-1, yidx:yidx+patch_size-overlap-1, :) = imgP_net;
        
        end
 
    end
    
    % save image
    name = [fnrlt 'AF_' num2str(k) '.tif'];
    fprintf('Save as %s.\n', name)
    imwrite(img_rlt, name);
end

