def read_expected_line(file, expected):
    line = file.readline().strip()
    if line != expected:
        print(f"line = {line} expected = {expected}")
        raise NotImplementedError

def from_source_to_destination(source_set, the_map):
    print(f"source_set = {source_set} the_map = {the_map}")
    processed_set = set()
    result = set()
    for item in source_set:
        print(f"item = {item}")
        flag = False
        for dst,src,rng in the_map:
            if src<=item<src+rng:
                print(f"Found {dst,src,rng} => {dst-src+item}")
                result.add(dst-src+item)
                processed_set.add(item)
                if flag:
                    raise NotImplementedError
                flag = True
    for item in source_set:
        if item not in processed_set:
            result.add(item)
    return result

def main():
    with open('input.txt', 'r') as file:
    #with open('demo.txt', 'r') as file:
        seeds = set(map(int,file.readline().split(":")[1].strip().split(" ")))
        print(f"seeds = {seeds}")
        read_expected_line(file,"")
        read_expected_line(file,"seed-to-soil map:")
        the_map = set()
        while True:
            line = file.readline().strip()
            if len(line) == 0:
                break
            the_map.add(tuple(map(int,line.split(" "))))
        soils = from_source_to_destination(seeds, the_map)
        print(f"soils = {soils}")
        print("="*20)
        read_expected_line(file,"soil-to-fertilizer map:")
        the_map = set()
        while True:
            line = file.readline().strip()
            if len(line) == 0:
                break
            the_map.add(tuple(map(int,line.split(" "))))
        fertilizers = from_source_to_destination(soils, the_map)
        print(f"fertilizers = {fertilizers}")        
        print("="*20)
        read_expected_line(file,"fertilizer-to-water map:")
        the_map = set()
        while True:
            line = file.readline().strip()
            if len(line) == 0:
                break
            the_map.add(tuple(map(int,line.split(" "))))
        waters = from_source_to_destination(fertilizers, the_map)
        print(f"waters = {waters}")        
        print("="*20)
        read_expected_line(file,"water-to-light map:")
        the_map = set()
        while True:
            line = file.readline().strip()
            if len(line) == 0:
                break
            the_map.add(tuple(map(int,line.split(" "))))
        lights = from_source_to_destination(waters, the_map)
        print(f"lights = {lights}")
        print("="*20)
        read_expected_line(file,"light-to-temperature map:")
        the_map = set()
        while True:
            line = file.readline().strip()
            if len(line) == 0:
                break
            the_map.add(tuple(map(int,line.split(" "))))
        temperatures = from_source_to_destination(lights, the_map)
        print(f"temperatures = {temperatures}")           
        print("="*20)
        read_expected_line(file,"temperature-to-humidity map:")
        the_map = set()
        while True:
            line = file.readline().strip()
            if len(line) == 0:
                break
            the_map.add(tuple(map(int,line.split(" "))))
        humidities = from_source_to_destination(temperatures, the_map)
        print(f"humidities = {humidities}")
        print("="*20)
        read_expected_line(file,"humidity-to-location map:")
        the_map = set()
        while True:
            line = file.readline().strip()
            if len(line) == 0:
                break
            the_map.add(tuple(map(int,line.split(" "))))
        locations = from_source_to_destination(humidities, the_map)
        print(f"locations = {locations}")  
        print(f"result = {min(locations)}")

if __name__ == "__main__":
    main()
