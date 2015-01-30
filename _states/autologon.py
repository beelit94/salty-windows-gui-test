import salt.exceptions


def enable_user(name, username):
    ret = {'name': name, 'changes': {}, 'result': False, 'comment': ''}

    # todo check user name is not in the list

    key = __salt__['reg.read_key']('HKEY_LOCAL_MACHINE',
                                   'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon',
                                   'AutoAdminLogon')

    ret['key'] = key

    ret['changes'] = {
        'old': 'current_state',
        'new': 'new_state',
    }

    ret['result'] = True
    ret['comment'] = 'ke: ' + str(key)

    return ret