def mars_exploration(s):
    
    count = 0
    correct = ["s", "o", "s"]
    for i in range(0, len(s) - 2, 3):
        current = s[i:i + 3].lower()
        if current != "sos":
            for j in range(0, 3):
                if current[j] != correct[j]: count += 1
    return count
