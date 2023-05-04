from metronomeextraction import metronomes

boxWidth = 300
squareWidth = 30
distance = boxWidth - squareWidth
frameRate = 30

for metronome in range(0, len(metronomes), 2):
    if not metronome == len(metronomes)-1:
        print(f'note{metronome} = new Square({distance / (metronomes[metronome][1]*30)}, {distance / (metronomes[metronome+1][1]*30)}, {((distance / metronomes[metronome][1]) * metronomes[metronome][0]) + 50}, {((distance / metronomes[metronome+1][1]) * metronomes[metronome+1][0]) + 50})')
    else:
        print(f'note{metronome} = new Square({distance / (metronomes[metronome][1]*30)}, {distance / (metronomes[metronome][1]*30)}, {((distance / metronomes[metronome][1]) * metronomes[metronome][0]) + 50}, {((distance / metronomes[metronome][1]) * metronomes[metronome][0]) + 50})')