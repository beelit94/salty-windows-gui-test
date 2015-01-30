import salt.exceptions

def enable_user(username):
	ret = {'username': username, 'changes': {}, 'result': False, 'comment': '', key: ''}

	# todo, check user name is not in the list

    # Check the current state of the system. Does anything need to change?
    key = __salt__['reg.read_key.read_key']('HKEY_LOCAL_MACHINE', 'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon', 'AutoAdminLogon')
    ret['key'] = key
    # if current_state == foo:
    #     ret['result'] = True
    #     ret['comment'] = 'System already in the correct state'
    #     return ret

    # # The state of the system does need to be changed. Check if we're running
    # # in ``test=true`` mode.
    # if __opts__['test'] == True:
    #     ret['comment'] = 'The state of "{0}" will be changed.'.format(name)
    #     ret['changes'] = {
    #         'old': current_state,
    #         'new': 'Description, diff, whatever of the new state',
    #     }

    #     # Return ``None`` when running with ``test=true``.
    #     ret['result'] = None

    #     return ret

    # # Finally, make the actual change and return the result.
    # new_state = __salt__['my_custom_module.change_state'](name, foo)

    # ret['comment'] = 'The state of "{0}" was changed!'.format(name)

    ret['changes'] = {
        'old': 'current_state',
        'new': 'new_state',
    }

    ret['result'] = True

    return ret