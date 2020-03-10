#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The while loop uses n * n * n which would mean we'd run it 3 to the 3rd power of n times but the while loop is resolved by 'a' which is set to 3 to the 2nd power which divides into the result causing your while loop only to be run exactly n amount of times. The result of which would be writen as the linear line O(n)

b) The for loop takes the range of n which would give us a runtime of n. The inner while loop runs off of a variable j being less than n but the while loop resovles by j being multiplied by 2 which in all cases but a few will result in a faster resolution than n. That said first loop n and second log n would give use the linearithmic line of O(n log n)

c) The recursive function returns 2 + itself minues one. The function is only being run n amount of times. It adds two each time which basically makes it a very advance x * 2 mathematical calculator but still only runs n times making it a linear line O(n).

## Exercise II

```python

function (n)
  onFloorF = false
  currentFloor = c
  brokeOnPreviousFloor = False
  while !onFloorF {
    if dropEgg() == True:
      brokeOnPreviousFloor = True
      if brokeOnPreviousFloor:
        currentFloor -= 1
      else:
        onFloorF = True
    else:
      brokeOnPreviousFloor = False
      if brokeOnPreviousFloor:
        currentFloor += 1
        onFloorF = True
      else:
        currentFloor += 1
  }

```

Either way you do it, with a for loop or a while loop it seems the maximum amount of times you would run the function is n. I would even go as far as to say that you will always solve it slightly faster than n as your f will most likely not be the roof or ground floor. This means the function comes out to a linear line O(n).