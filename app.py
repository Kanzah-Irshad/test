
#  GROUP # C (KAVITA & KANZAH)


list1 = input("Enter numbers: ")      
list1 = list1.split()                 
list1 = [int(x) for x in list1]        # Convert to integers

duplicates = []

for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] == list1[j] and list1[i] not in duplicates:
            duplicates.append(list1[i])

if duplicates:
    print("Duplicate numbers found:", duplicates)
else:
    print("No duplicates found.")




