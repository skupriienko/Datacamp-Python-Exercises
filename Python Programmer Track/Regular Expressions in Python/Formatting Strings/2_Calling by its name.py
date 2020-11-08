# Create a dictionary
plan = {
  		"field": courses[0],
        "tool": courses[1]
        }

# Complete the placeholders accessing elements of field and tool keys
my_message = "If you are interested in {0}, you can take the course related to {1}"

# Use dictionary to replace placeholders
print(my_message.format(plan["field"], plan["tool"]))
