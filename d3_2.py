txt = open("d3.txt").read()
data = txt.split("\n")

triangles = []
for item in data:
	triangles.append(item.split("  ")[1:])
triangles.pop()

for triangle in triangles:
	if '' in triangle:
		triangle.remove('')
	for id, line in enumerate(triangle):
		triangle[id] = int(triangle[id].strip())

triangles_v2 = []
for x in range(3):
	group_of_lines = []
	for triangle in triangles:
		group_of_lines.append(triangle[x])
	new_triangle = []
	i = 0
	while i <= len(group_of_lines)-3:
		new_triangle = [group_of_lines[i], group_of_lines[i+1], group_of_lines[i+2]]
		i += 3
		triangles_v2.append(new_triangle)

# print(len(triangles_v2))
count = 0
for triangle in triangles_v2:
	if triangle[0] + triangle[1] > triangle[2] and\
	   triangle[0] + triangle[2] > triangle[1] and\
	   triangle[1] + triangle[2] > triangle[0]:
	   count += 1
print(count)