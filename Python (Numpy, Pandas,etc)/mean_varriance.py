import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
    return  
    
  np_array = np.array(list).reshape((3,3))
  
  calculations = {
    'mean': [np.mean(np_array, axis = 0),np.mean(np_array, axis = 1),np.mean(np_array) ],
    'variance': [np.var(np_array, axis = 0),np.var(np_array, axis = 1),np.var(np_array)],
    'standard deviation': [np.std(np_array, axis = 0),np.std(np_array, axis = 1),np.std(np_array)],
    'max': [np.max(np_array, axis = 0),np.max(np_array, axis = 1),np.max(np_array)],
    'min': [np.min(np_array, axis = 0),np.min(np_array, axis = 1),np.min(np_array)],
    'sum': [np.sum(np_array, axis = 0),np.sum(np_array, axis = 1),np.sum(np_array)],
  }

  for key, value in calculations.items():
    updated_value = [item.tolist() if isinstance(item, np.ndarray) else item for item in value]
    calculations[key] = updated_value
  return calculations