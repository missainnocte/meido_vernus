def event_handler(msg):
    msg_chain = msg.get('messageChain')
    if not msg_chain:
        return
    if not is_at_me(msg_chain):
        return
    if not is_req_setu(msg_chain):
        return
    return send_setu(get_group(msg))