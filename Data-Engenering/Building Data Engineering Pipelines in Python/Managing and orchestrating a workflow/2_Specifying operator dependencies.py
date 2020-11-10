# Specify direction using verbose method
prepare_crust.set_downstream(apply_tomato_sauce)

tasks_with_tomato_sauce_parent = [add_cheese, add_ham, add_olives, add_mushroom]
for task in tasks_with_tomato_sauce_parent:
    # Specify direction using verbose method on relevant task
    apply_tomato_sauce.set_downstream(task)

# Specify direction using bitshift operator
tasks_with_tomato_sauce_parent >> bake_pizza

# Specify direction using verbose method
bake_pizza.set_upstream(prepare_oven)