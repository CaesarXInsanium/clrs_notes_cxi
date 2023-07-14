import unittest
import algorithmsnim/sort
import std/options

test "merge sort":
  check 0 == 0
  var l = @[1,2,3,4]
  merge_sort(l)
