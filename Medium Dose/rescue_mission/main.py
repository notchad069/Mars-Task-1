def muchikofilter(data,size = 3):
    noiseless1_data = []
    for i in range(len(data) - size + 1):
        a = data[i :i+size] #extractin 3 elements
        noiseless1_data.append(sum(a)/size)
    return noiseless1_data
def sanchikofilter(data,size = 3):
    noiseless2_data = []
    for i in range(len(data) - size +1):
        b = data[i:i+size]
        b_sorted = sorted(b)
        noiseless2_data.append(b_sorted[size//2])
    return noiseless2_data
with open("log.txt","r") as file: #opens log.txt in read mode
    sensor_data = [int(x) for x in file.read().strip().split()]

muchikofiltered_data = muchikofilter(sensor_data)
sanchikofiltered_data = sanchikofilter(sensor_data)

print("here's the unfiltered data for ya: ",sensor_data)
print("Muchiko filtered data: ",muchikofiltered_data)
print("Sanchiko filtered data: ", sanchikofiltered_data)
