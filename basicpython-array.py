name_colls = ["Mary", "John", "Peter", "Jane", "William"]

# count number of items in the collection
item_count = len(name_colls)
print (item_count)

# get name from index 2. array collection starts from index 0 to n+1
# name_colls[1] meaning we get the second item from the collection 
# which falls under index 1
name_coll_2 = name_colls[1]
print (name_coll_2)

# get or iterate the item via loop
for name in name_colls:
  print (name)

# ading new name to the collection
name_colls.append('Christian')

print (name_colls)

# END: That's it for now
