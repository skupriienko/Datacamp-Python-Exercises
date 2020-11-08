# Define send_message()
def send_message(pending, message):
    print("USER : {}".format(message))
    action, pending_action = policy(interpret(message))
    if action == 'do_pending' and pending is not None:
        print("BOT : {}".format(pending))
    else:
        print("BOT : {}".format(action))
    return pending_action


# Define send_messages()
def send_messages(messages):
    pending = None
    for msg in messages:
        pending = send_message(pending, msg)


# Send the messages
send_messages([
    "I'd like to order some coffee",
    "ok yes please"
])