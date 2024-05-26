numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
print('\n'.join(numbers[int(i)] for i in input() if i.isdigit()))