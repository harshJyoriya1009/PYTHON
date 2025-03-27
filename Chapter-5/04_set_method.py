s={1,87,58,47,"Harsh"}

s.add(67)
print(s)

s.remove("Harsh")
print(s)

# • len(s): Returns 4, the length of the set  
# • s.remove(8): Updates the set s and removes 8 from s. 
# • s.pop(): Removes an arbitrary element from the set and return the element removed. 
# • s.clear():empties the set s.



# Union and Intersection

s1={1,7,58,69}
s2={1,78,89,69}

print(s1.union(s2))          #o/p- {1, 69, 7, 78, 89, 58}
print(s1.intersection(s2))   #o/p- {1,69}
