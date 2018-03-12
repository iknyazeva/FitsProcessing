import numpy as np

def save_do_dipha(img_data, filename):
    
    """
    save matrix data to dipha format 
    img_data: numpy array
    filename: path to output file
    """
    #import numpy as np
    num = np.array(8067171840).astype('int64') #magic dipha number
    fid = np.array(1).astype('int64') #another magic dipha number
    numel= np.array(img_data.size).astype('int64') #number of elements in array
    dim = np.array(len(img_data.shape)).astype('int64') # dimension of numpy array
    imshape = np.array(img_data.shape).astype('int64') # shape of numpy array
    data = img_data.reshape(-1, order = 'F').astype('float64') #data in x-fastest order
 
    with open(filename, 'wb') as f:
        num.tofile(f)
        fid.tofile(f)
        numel.tofile(f)
        dim.tofile(f)
        imshape.tofile(f)
        data.tofile(f)
    f.close()
    print('Image was saved to dipha compatible format with name '+filename)
    return 0

def read_PD_dipha(dgmfile):
    """
    load dipha persistence diagram to numpy arrays
    dgmfile: dipha file with PD
    """
    import numpy as np
    fd = open(dgmfile,'rb') 
    dipha_identifier, dgm_identifier = np.fromfile(fd, dtype = 'int', count = 2)
    fd.seek(16)
    num_pairs = np.fromfile(fd, dtype = 'int', count = 1).astype('int')
    fd.seek(24)
    dt = np.dtype("i8, f8, f8")
    whole_array = np.fromfile(fd, dtype = dt, count = num_pairs[0])
    fd.close()
    dims,birth,death = zip(*whole_array)
    dims = np.array(dims)
    birth = np.array(birth)
    death = np.array(death)
    return (dims,birth,death)
def run_dipha(dipha_img_path, dipha_dir):
    import numpy as np
    import subprocess
    dipha_res = subprocess.run(['mpiexec',
     '-n',
     '4',
     dipha_dir,
     dipha_img_path,
     dipha_img_path + '.dgm'])
    print(dipha_res)
    return 0 
    