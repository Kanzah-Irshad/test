
#  GROUP # C (KAVITA & KANZAH)

list1 = input("Enter strings words by seperates space: ").split()


duplicates = []

for strr in list1:
    if list1.count(strr) > 1 and strr not in duplicates:
        duplicates.append(strr)


if duplicates:
    print("Duplicate words found:", duplicates)
else:
    print("No duplicates found.")

