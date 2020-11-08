call_count = 0

def my_function():
    # Use a keyword that lets us update call_count
    global call_count
    call_count += 1

    print("You've called my_function() {} times!".format(call_count))

for i in range(20):
    my_function()

def read_files():
    file_contents = None

    def save_contents(filename):
        # Add a keyword that lets us modify file_contents
        nonlocal file_contents
        if file_contents is None:
            file_contents = []
    with open(filename) as fin:
        file_contents.append(fin.read())

    for filename in ['1984.txt', 'MobyDick.txt', 'CatsEye.txt']:
        save_contents(filename)

    return file_contents

print('\n'.join(read_files()))

def wait_until_done():
    def check_is_done():
    # Add a keyword so that wait_until_done()
    # doesn't run forever
        global done
        if random.random() < 0.1:
            done = True

    while not done:
        check_is_done()

done = False
wait_until_done()

print('Work done? {}'.format(done))
