# This file contains global functions used in all sorting algorithms


def swap(arr, a, b):
  temp = arr[a]
  arr[a] = arr[b]
  arr[b] = temp

  return arr


def ifelse(cond, t, f):
  if (cond):
    return t

  return f
