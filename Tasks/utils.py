class TaskObject:
    def __init__(self, model, task_type, color=None ):
        self.model = model
        self.task_type = task_type
        task_types = {'Other': 'black', 'Exam': 'red', 'Assignment': 'rgb(80, 5, 5)', 'Coding Challenge': '#590c47'}
        self.color = task_types[task_type]

def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves   
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
        i = j = k = 0
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i].model.due_by < R[j].model.due_by: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1