# %%
import hashlib
import os
import time
from imagededup.methods import PHash
from shutil import copyfile

# %%
#统计文件夹下的文件个数
def file_count_recursice(path):
    if os.path.isdir(path)==False:
        return 1
    file_list=os.listdir(path)
    cnt = 0 
    for i in file_list:
        path_now = path + "/" + i
        
        cnt += file_count_recursice(path_now)
    
    return cnt


# %%
origin_dir ="./kunkun"

# %%
out_dir = origin_dir
if os.path.isdir(out_dir)==False:
    os.mkdir(out_dir)

# %%
phasher = PHash()
encodings = phasher.encode_images(image_dir=origin_dir,recursive=True)

# %%
print(f"去重前图片 {file_count_recursice(origin_dir)}张")

# %%
remove_origin = True
for k in encodings.keys() :
    v = encodings[k]
    ext = os.path.splitext(k)
    origin_path = os.path.join(origin_dir,k)
    new_path = os.path.join(out_dir,v + ext[1])
    if not os.path.exists(new_path) :
        copyfile( origin_path,new_path)
    if remove_origin and origin_path != new_path:
        os.remove(origin_path)

# %%
print(f"去重后图片 {file_count_recursice(out_dir)}张")



