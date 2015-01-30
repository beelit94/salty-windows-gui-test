import salt.exceptions


def enable_user(name, username):
    ret = {'name': name, 'changes': {}, 'result': False, 'comment': ''}

    # todo check user name is not in the list

    auto_admin_logon = __salt__['reg.read_key']('HKEY_LOCAL_MACHINE',
                                                'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon',
                                                'AutoAdminLogon')
    default_user = __salt__['reg.read_key']('HKEY_LOCAL_MACHINE',
                                            'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon',
                                            'DefaultUserName')
    default_domain_name = __salt__['reg.read_key']('HKEY_LOCAL_MACHINE',
                                                   'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon',
                                                   'DefaultDomainName')

    computer_name = __salt__['win_system.get_computer_name']()

    if auto_admin_logon == str(1) \
            and default_user == username \
            and default_domain_name == computer_name:
        ret['result'] = True
        ret['comment'] = 'System already in the correct state'
        return ret

    # default_password = __salt__['reg.read_key']('HKEY_LOCAL_MACHINE',
    #                                             'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon',
    #                                             'DefaultPassword')


    # ret['changes'] = {
    #     'old': 'current_state',
    #     'new': 'new_state',
    # }

    ret['result'] = False
    ret['comment'] = 'Not in right state'

    return ret