# An Infinite Scrolling Pad Wigit

Hopefully fairly self explanatory. For anyone trying to work out the details,
the follwoing table shows how thigs work.

This is if height = 5
top is the first row of the pad that is shown
pos is the row written to
pos_b is a second row written to

Input Row | top | pos | pos_b
----------|-----|-----|------
 0        | 0   | 0   | 
 1        | 0   | 1   | 
 2        | 0   | 2   | 
 3        | 0   | 3   | 
 4        | 0   | 4   | 
 5        | 1   | 5   | 0
 6        | 2   | 6   | 1
 7        | 3   | 7   | 2
 8        | 4   | 8   | 3
 9        | 5   | 9   | 4
 10       | 1   | 5   | 0
 11       | 2   | 6   | 1

Once the position we get to is twice the height, we can
cycle round to the start of the pad again.

