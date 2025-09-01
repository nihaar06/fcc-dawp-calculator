import numpy as np

def calculate(list):
    if(len(list)!=9):
        raise ValueError("List must contain nine numbers.")
    arr=np.array(list).reshape(3,3)
    calculations={
        'mean':[np.mean(arr,axis=0).tolist(),np.mean(arr,axis=1).tolist(),arr.mean()],
        'variance':[np.var(arr,axis=0).tolist(),np.var(arr,axis=1).tolist(),arr.var()],
        'standard deviation':[np.std(arr,axis=0).tolist(),np.std(arr,axis=1).tolist(),arr.std()],
        'sum':[np.sum(arr,axis=0).tolist(),np.sum(arr,axis=1).tolist(),arr.sum()],
        'min':[np.min(arr,axis=0).tolist(),np.min(arr,axis=1).tolist(),arr.min()],
        'max':[np.max(arr,axis=0).tolist(),np.max(arr,axis=1).tolist(),arr.max()]
    }
    return calculations