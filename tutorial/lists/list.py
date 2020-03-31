bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
# add items
bicycles.append('جديد')
print(bicycles[-1])
bicycles.insert(0,'سيناء')

# remove an item
del bicycles[0]
bicycles.pop()
# sort
bicycles.reverse()
bicycles.sort()
# passing list to function
d = [1,2,3]
def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor
scale(d,5)