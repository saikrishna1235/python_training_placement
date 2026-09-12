s = "ABAB"
k = 2  # Max operations allowed

for i in range(len(s)):
    if s[i] != "B" and k > 0:
        s_list = list(s)  # Convert to list to allow modification
        s_list[i] = "B"  # Change 'A' to 'B'
        s = "".join(s_list)  # Convert back to string
        k -= 1  # Reduce the count of available operations

print(s)  # Output: BBBB            
