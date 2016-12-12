txt = open("d3.txt").read()
data = txt.split("\n")
triangles = []
for item in data:
	triangles.append(item.split("  ")[1:])
triangles.pop()
count = 0
for triangle in triangles:
	if '' in triangle:
		triangle.remove('')
	for id, line in enumerate(triangle):
		triangle[id] = int(triangle[id].strip())

	
	if triangle[0] + triangle[1] > triangle[2] and\
	   triangle[0] + triangle[2] > triangle[1] and\
	   triangle[1] + triangle[2] > triangle[0]:
	   count += 1

print(count)
