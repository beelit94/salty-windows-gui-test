import salt.exceptions


def add_event(name, username, password, jenkins_master, jenkins_jar, jenkins_slave_labels):
    ret = {'name': name, 'changes': {}, 'result': False, 'comment': ''}

    task_name = 'jenkins'
    jenkins_folder = 'c:\\jenkins'
    task_run_cmd = '"java -jar %s -executors 1 -master %s -labels %s -mode exclusive -fsroot %s"' % \
                   (jenkins_jar, jenkins_master, jenkins_slave_labels, jenkins_folder)
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
