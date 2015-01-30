import salt.exceptions

def enable_user(username):
	ret = {'username': username, 'changes': {}, 'result': False, 'comment': '', 'key': ''}

	# todo, check user name is not in the list

    # Check the current state of the system. Does anything need to change?
    key = __salt__['reg.read_key']('HKEY_LOCAL_MACHINE', 'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon', 'AutoAdminLogon')

    ret['key'] = key

    ret['changes'] = {
        'old': 'current_state',
        'new': 'new_state',
    }

    ret['result'] = True

    return ret