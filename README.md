# Exercise 5.1 One minute

The exercise template comes with the "ClockHand" class described in the material. Implement a `Timer` class based on the material's `Clock` class. You will need to create a file called `timer.py` where the class is implemented. 

The timer has two hands, one for hundredths of a second and one for seconds. As it progresses, the number of hundredths of a second grows by one. When the hand corresponding to hundredths of a second reaches a value of 100, its value is set to zero, and the number of seconds grows by one. In the same way, when the value of the hand corresponding to seconds reaches the value of sixty, its value is set to zero.

- `timer = Timer()` creates a new timer.
- `def __str__()` returns a string representation of the timer. The string representation should be in the form "seconds: hundredths of a second", where both the seconds and the hundredths of a second are represented by two numbers. For example, "19:83" would represent the time 19 seconds, 83 hundredths of a second.
- `def advance()` moves the timer forward by a hundredth of a second.

Once you've completed the task, return it to Github.

You can test out the timer's functionality in the main program whenever you like. The example code below provides you with a program where the timer is printed and it advances once every hundredth of a second.

```python
timer = Timer()

while True:
    print(timer)
    timer.advance()
```

NB! The program above will never stop running by itself. Press Ctrl-C to cancel the execution.
