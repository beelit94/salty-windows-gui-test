{% set username = 'msinstaller' %}
{% set password = 'win9@fanbiejap' %}
{% set os_family = salt['grains.get']('os_family', '') %}
{% set osrelease = salt['grains.get']('osrelease', '') %}
{% set cpuarch = salt['grains.get']('cpuarch', '') %}

c:\disconnectRDP.cmd:
  file.managed:
     - source: salt://gui-test/disconnectRDP.cmd

auto_logon:
  autologon:
    - enable_user
    - username: {{ username }}
    - password: {{ password }}

{{ username }}:
  user.present:
    - password: {{ password }}
    - groups:
      - Administrators

power_cfg:
  cmd.script:
    - source: salt://gui-test/powercfg_high.cmd
    - cwd: /

jenkins_plugin:
  taskschd:
    - add_event
    - username: {{ username }}
    - password: {{ password }}
    - jenkins_master: 'http://10.140.28.218:8080/'
    - jenkins_jar: 'c:\\jenkins\\swarm-client-1.22-jar-with-dependencies.jar'
    - jenkins_slave_labels: {{ os_family }}{{ osrelease }}{{ cpuarch }}
    - watch:
      - user: {{ username }}