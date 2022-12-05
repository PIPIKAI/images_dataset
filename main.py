import hashlib
import os

#获取文件的MD5值，适用于小文件
def getFileMD5(self,filepath):
    if self.isFile(filepath):
        f = open(filepath,'rb')
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        f.close()
        return str(hash).upper()
    return None

def unique_img(src):
    file_list = os.listdir(src)
    
    pass