import unittest
import algorithmsnim/sort

const LIST = @[4,5,9,3,7,7,3,2,8,7]

test "sort_checker":
  var l = @[1,2,3,4]
  check sorted(l)
test "merge_sort":
  check 0 == 0
  var l = @[1,2,3,4]
  merge_sort(l)

test "insertion_sort":
  var l = LIST
  insertion_sort(l)
  check sorted(l)
  