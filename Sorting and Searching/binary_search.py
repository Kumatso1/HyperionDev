# def search(list1,n):
#     l=0
#     u=len(list1)-1
#     while l <=u:
#         mid=(l+u)//2
#         if list1[mid]==n:
#             globals() ['pos'] = mid
#             return True
#         else:
#             if list1[mid] < n:
#                 l=mid
#             else:
#                 u=mid
albums2=["Dalison","James","Kelvin",5,10,"Alinafe","Emily"]
dark_side_index = albums2.index("Alinafe")
print(f"\nIndex of Dark Side of the Moon: {dark_side_index}")
# if search(list1,n):
#     print(f"The searched number {list1[pos]} is found at position {pos+1}")
# else:
#     print("Not found")
