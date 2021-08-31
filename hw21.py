#!/usr/bin/python3

import itertools
import numpy


def merge(nums1, nums2):
    unsorted_array = numpy.array(list(itertools.chain(nums1, nums2)))
    sorted_array = numpy.sort(unsorted_array)
    return sorted_array.tolist()


print(merge((x for x in range(1, 4)), (x for x in range(2, 5))) == [1, 2, 2, 3, 3, 4])
print(merge((x for x in range(1, 4)), (x for x in range(2, 5))))
print(merge((x for x in range(13, 37, 3)), (y for y in range(12, 38, 2))))
