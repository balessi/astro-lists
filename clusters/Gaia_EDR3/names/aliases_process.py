
def read():
    print('entering read()...')
    clusters = []
    with open(r'./aliases.txt', 'r', encoding='utf8') as f:
        for line in f:
            name, aliases, ref = [it.strip() for it in line.strip().split(';')]
            clusters.append((name, aliases, ref))
    return clusters

def process(cls):
    print('entering process()...')
    clusters = set()
    for name, aliases, ref in cls:
        if ',' in aliases:
            for alias in [it.strip() for it in aliases.split(',')]:
                clusters.add((name, alias, ref))
                clusters.add((alias, name, ref))
        else:
            clusters.add((name, aliases, ref))
            clusters.add((aliases, name, ref))
    return clusters        

def write(clusters):
    print('entering write()...')
    with open(r'./aliases2.txt', 'w', encoding='utf8') as f:
        for cl in clusters:
            name, alias, ref = cl
            line_out = f'{name:<40};'
            line_out += f'{alias:<40};'
            line_out += f'{ref}\n'
            f.write(line_out)

if __name__ == '__main__':
    aliases = read()
    splitted = process(aliases)
    write(splitted)
