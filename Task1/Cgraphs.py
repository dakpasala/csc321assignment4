import matplotlib.pyplot as plt

# Data from the results
digest_sizes = list(range(8, 51, 2))
collision_times = [
    0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.01, 0.01, 0.01, 0.04, 0.08,
    0.10, 0.16, 0.35, 1.13, 2.82, 4.11, 12.81, 14.10, 19.40, 28.67
]
inputs_tried = [
    256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216,
    67108864, 268435456, 1073741824, 4294967296, 17179869184, 68719476736,
    274877906944, 1099511627776, 4398046511104, 17592186044416,
    70368744177664, 281474976710656, 1125899906842624
]  # Estimated based on birthday bound

# Create the first graph: Digest size vs Collision time
plt.figure(figsize=(10, 6))
plt.plot(digest_sizes, collision_times, marker='o', label='Collision Time (s)')
plt.title('Digest Size vs Collision Time')
plt.xlabel('Digest Size (Bits)')
plt.ylabel('Collision Time (Seconds)')
plt.grid(True)
plt.legend()
plt.show()

# Create the second graph: Digest size vs Number of inputs tried
plt.figure(figsize=(10, 6))
plt.plot(digest_sizes, inputs_tried, marker='o', color='orange', label='Inputs Tried')
plt.yscale('log')  # Use a logarithmic scale for better visibility
plt.title('Digest Size vs Number of Inputs Tried')
plt.xlabel('Digest Size (Bits)')
plt.ylabel('Number of Inputs Tried (Log Scale)')
plt.grid(True)
plt.legend()
plt.show()
