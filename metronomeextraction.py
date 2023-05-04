from timeinfo import output

times = output

for i in range(len(times)):
    times[i] = round(times[i], 7)
print(times)
metronomes = {} 
trash = []



for i in range(len(times)):
    if times[i] in trash:
        continue
    patterns = []
    for j in range(i+1, len(times)):
        if times[j] in trash:
            continue
        if 2*times[j] - times[i] in times:
            metronomes[times[i]] = times[j]-times[i]
            counter = 0
            while round(times[i] + (counter * metronomes[times[i]]), 7) in times and not round(times[i] + (counter * metronomes[times[i]]), 7) in trash:
                #trash.append(round(times[i] + (counter * metronomes[times[i]]), 7))
                counter += 1
            patterns.append((times[j]-times[i], counter))

    bestPattern = (0, -1)
    for pattern in patterns:
        if pattern[0] < times[i]:
            continue
        if pattern[1] > bestPattern[1]:
            bestPattern = pattern
    for j in range(bestPattern[1]):
        trash.append(round(times[i] + (j * bestPattern[0]), 7))
    metronomes[times[i]] = bestPattern
            

print(metronomes) #The key is the time the note first starts playing. The value is a tuple that looks like this (how often it's repeated, how many times it's repeated)

# For the pattern to be animate-able then the each key in the metronomes dictionary (starting time) <= the first value of the value tuple (time frequency of the note)