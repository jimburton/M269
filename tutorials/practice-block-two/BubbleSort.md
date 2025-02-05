# Pseudocode for Bubble Sort
   
```
procedure bubbleSort(A : list of sortable items)
    n := length(A)
    for i := 0 to n-1
        swapped := false
        for j := 0 to n-i-1
            # if this pair is out of order 
            if A[j] > A[j+1] then
                # swap the values
                swap(A[j], A[j+1]) # you need to decide how to do this
                swapped := true
            end if
        end for
        if swapped = false then
            break
        endif
    end for
    return 
end procedure
```