import array
# 같은 주소에 저장됨
arr = array.array("f",[99,0,-7,0,16])
for i in range(len(arr)):
    print(f"{arr[i]:3},{id(arr[i])}")
