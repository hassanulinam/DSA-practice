# Given a char array, find count "AG" pairs (i, j) such that i < j and arr[i]='A' and arr[j]='G'
# EX: arr = [B, A, C, G, G, S, A, E, G, D] --> 4 pairs

arr = input("Enter character arr: ").split()
A, G = input("Enter A G values to find: ").split()
N = len(arr)

# # ------- Approach with prefix-sum --------
# # Time Complexity = O(N), Space Complexity = O(N)
# a_counts = [0]
# if arr[0] == A:
#     a_counts[0] = 1
# for i in range(1, N):
#     previous_count = a_counts[i - 1]
#     if arr[i] == A:
#         a_counts.append(previous_count + 1)
#     else:
#         a_counts.append(previous_count)

# print("A Counts: ", a_counts)
# pairs_count = 0
# for i in range(N):
#     if arr[i] == G:
#         pairs_count += a_counts[i]
# print(pairs_count)

# ---- Carry Forward technique ----
# :: we can simply remember the no.of occurences of 'A' at each index, and simply increase the resultant_count if found 'G'
a_count = 1 if arr[0] == A else 0
resultant_count = 0
for i in range(1, N):
    if arr[i] == G:
        resultant_count += a_count
    elif arr[i] == A:
        a_count += 1

print(resultant_count)
# Thus, Time Complexity = O(N), Space Complexity = O(1)
