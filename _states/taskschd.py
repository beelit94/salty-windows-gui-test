import salt.exceptions
import platform
import sys
import os
from distutils.version import StrictVersion


windows_versions = {
    'Windows7': '6.1',
    'Windows8': '6.2',
    'Windows8.1': '6.3'
}

windows_server_versions = {
    'WindowsServer2003R2': '5.2',
    'WindowsServer2008': '6.0',
    'WindowsServer2008R2': '6.1',
    'WindowsServer2012': '6.2',
    'WindowsServer2012R2': '6.3'
}

def get_os_arch():
    if os.path.exists('C:\Program Files (x86)'):
        return 'x64'
    else:
        return 'x86'

def add_event(name, username, password, jenkins_master, jenkins_jar):
    ret = {'name': name, 'changes': {}, 'result': False, 'comment': ''}

    # jenkins slave label naming convention
    # windows + <version> + <minor version> + <arch> + <service pack>
    major = sys.getwindowsversion().major
    minor = sys.getwindowsversion().minor
    ver_str = str(major) + '.' + str(minor)
    ver = StrictVersion(ver_str)
    win_full_version = ''
    if 'Server' in platform.release():
        for win_key, win_value in windows_server_versions:
            if ver == StrictVersion(win_value):
                win_full_version = win_key
    else:
        for win_key, win_value in windows_versions:
            if ver == StrictVersion(win_value):
                win_full_version = win_key
    jenkins_labels = win_full_version + get_os_arch()

    task_name = 'jenkins'
    jenkins_folder = 'c:\\jenkins'
    task_run_cmd = '"java -jar %s -executors 1 -master %s -labels %s -mode exclusive -fsroot %s"' % \
                   (jenkins_jar, jenkins_master, jenkins_labels, jenkins_folder)
    cmd = 'SCHTASKS /Create /SC ONLOGON /RL HIGHEST /IT /F /TN %s /TR %s /RU %s /RP %s ' % \
          (task_name, task_run_cmd, username, password)

    cmd_result = __salt__['cmd.run_all'](cmd)

    if cmd_result['retcode'] != 0:
        ret['result'] = False
        ret['comment'] = cmd_result['stderr'] + cmd_result['stdout']
        return ret

    ret['result'] = True
    ret['comment'] = cmd_result['stdout']
    return ret
