import salt.exceptions
import logging

log = logging.getLogger(__name__)


def enable_user(name, username, password):
    ret = {'name': name, 'changes': {}, 'result': False, 'comment': ''}

    # todo check user name is not in the list

    auto_admin_logon = __salt__['reg.read_key']('HKEY_LOCAL_MACHINE',
                                                'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon',
                                                'AutoAdminLogon')
    log.info('original AutoAdminLogon: %s' % auto_admin_logon)
    default_user = __salt__['reg.read_key']('HKEY_LOCAL_MACHINE',
                                            'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon',
                                            'DefaultUserName')
    log.info('original DefaultUserName: %s' % default_user)
    default_domain_name = __salt__['reg.read_key']('HKEY_LOCAL_MACHINE',
                                                   'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon',
                                                   'DefaultDomainName')
    log.info('original DefaultDomainName: %s' % default_domain_name)
    default_password = __salt__['reg.read_key']('HKEY_LOCAL_MACHINE',
                                                'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon',
                                                'DefaultPassword')
    log.info('original DefaultPassword: %s' % default_password)
    computer_name = __salt__['system.get_computer_name']()

    if auto_admin_logon == str(1) \
            and default_user == username \
            and default_domain_name == computer_name \
            and default_password is False:
        ret['result'] = True
        ret['comment'] = 'System already in the correct state'
        return ret

    if auto_admin_logon == str(1) \
            and default_user == username \
            and default_domain_name == computer_name \
            and default_password == password:
        ret['result'] = True
        ret['comment'] = 'auto logon for %s is set, need to reboot' % username
        return ret

    # auto admin logon key
    # not exist, the create key module will set key instead fo create key
    # if a key is already exist
    try:
        result = __salt__['reg.create_key']('HKEY_LOCAL_MACHINE',
                                            'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon',
                                            'AutoAdminLogon',
                                            '1')
        log.info('AutoAdminLogon created' + str(result))

        result = __salt__['reg.create_key']('HKEY_LOCAL_MACHINE',
                                   'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon',
                                   'DefaultUserName',
                                   username)
        log.info('DefaultUserName' + str(result))

        result = __salt__['reg.create_key']('HKEY_LOCAL_MACHINE',
                                   'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon',
                                   'DefaultDomainName',
                                   computer_name)
        log.info('DefaultDomainName' + str(result))

        result = __salt__['reg.create_key']('HKEY_LOCAL_MACHINE',
                                   'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon',
                                   'DefaultPassword',
                                   password)
        log.info('DefaultPassword' + str(result))

    except Exception as err:
        ret['result'] = False
        ret['comment'] = str(err)
        return ret

    ret['changes'] = {
        'old': 'auto logon for user:%s is not set' % username,
        'new': 'auto logon for user:%s is set, need to reboot system' % username,
    }

    ret['result'] = True
    ret['comment'] = 'auto logon for user:%s is set, need to reboot system' % username

    return ret