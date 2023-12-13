---
author: Aquiles Carattino
slug: python-tip-using-else-loops
date: 2020-05-25
description: Learn how to use the else block with for and while loops
image: '/images/else_in_loops.png'
subtitle: Learn how to use the else block with for and while loops
tags: [loops, for, while, else, tips] 
title: "Python Tip: Using Else with Loops"
---

Most likely, you are aware of how to use the ``else`` statement with an ``if`` clause. However, Python also allows us to use them with loops. They are straightforward to understand and open some exciting possibilities. Before continuing, remember that ``else`` in this context should be called ``no-break``. 

Let's quickly see how a for-loop works:

```python
start = 0
end = 10

for i in range(start, end):
    print(i)
else:
    print('End')
```

The code above will print the numbers from ``0`` to ``9`` and the ``End`` string. So far, nothing impressive, but check this out:

```python
start = 0  
end = 10  
break_point = 5  
  
for i in range(start, end):  
    print(i)  
    if i == break_point:  
        break  
else:  
    print('Nothing')
```

The output will be all the numbers from ``0`` to ``5``, but no string at the end. Now you can understand why it was called ``no-break``. The same approach also works for ``while`` loops:

```python
start = 0  
end = 10  
break_point = 5  
  
i = start  
  
while i < end:  
    print(i)  
    i += 1  
  if i == break_point:  
        break  
else:  
    print('Nothing')
```

The fair question is, when would you use this pattern. A clear situation is when you are looking for an element. For example, you may be looking for a specific line in a file, and want to raise an exception if not found:

```python
key_line = 'Key Line'
f = open('file.dat', 'r')
for line in f:
    if line == key_line:
        break
else:
    raise Exception('Line not Found')
```

Perhaps raising an exception is a bit extreme, but you see the pattern. It saves you from checking whether we found the line in the file or not using some extra variable to verify it. 

If you have used this pattern and have any helpful examples, you can always share it in the discussion below.