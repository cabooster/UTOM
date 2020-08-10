% transform all images in a folder
% save as uint8 *.png files
clc;clear;

src = './0-whole_slide/AF';
dst = './trainA/';
if ~exist(dst); mkdir(dst);end

patch_size = 512;

list = dir([src '/*.tif']);

kk=0;
for k = 1:length(list)
    fprintf('%d of %d...\n', k, length(list));
    imgS = loadtiff(fullfile(list(k).folder, list(k).name));
    [xs, ys, zs] = size(imgS);
    
    nb_per_slide = floor(xs*ys/patch_size/patch_size*7.0);
    
%     imgS = double(imgS);
%     imgS = imgS - min(imgS(:));
%     imgS = imgS/max(imgS(:));
%     imgS = uint8(imgS * 255);
    
    
    cord = zeros((xs-patch_size+1)*(ys-patch_size+1), 2);
    for i = 1:(xs-patch_size+1)
        for j = 1:(ys-patch_size+1)
            
            cord(j+(i-1)*(ys-patch_size+1), 1) = i;
            cord(j+(i-1)*(ys-patch_size+1), 2) = j;
            
        end
    end
    
    for ss = 1:zs
        sp = randperm(size(cord, 1), nb_per_slide);
        img = imgS(:,:,ss);
        
        for jj = 1:nb_per_slide
            kk=kk+1;
            xi = cord(sp(jj), 1);
            yi = cord(sp(jj), 2);
            imgP = img(xi:xi+patch_size-1,yi:yi+patch_size-1);
            
%             if mean(mean(double(imgP)))<2
%                 continue;
%             end
            
            imwrite(imgP, [dst num2str(kk) '.png']);
        end
        
    end
    
end


