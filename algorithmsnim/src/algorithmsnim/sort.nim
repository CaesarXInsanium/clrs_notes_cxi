## This Module Will Contain Sorting Algorithms and related utilities

proc sorted*[T](a: openArray[T]): bool = 
  ## Checks if seq is sorted
  var x = a[0]
  for i in a:
    if x > i:
      return false
    x = i
  return true

proc merge_sort*[T](a: var openArray[T]) = 
  ## Not implemented
  for i in a:
    echo i

proc insertion_sort*[T](a: var openArray[T]) =
  ## openArray denotes any array type in Nim that has lenght and can be indexed
  for j in 1..(a.len() - 1):
    var key = a[j]
    var i = j - 1
    while i >= 0 and a[i] > key:
      a[i + 1] = a[i]
      i = i - 1
    a[i + 1] = key
  
