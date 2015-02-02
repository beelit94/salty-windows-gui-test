{% set username = 'msinstaller' %}
{% set password = 'win9@fanbiejap' %}
{% set os_family = salt['grains.get']('os_family', '') %}
{% set osrelease = salt['grains.get']('osrelease', '') %}
{% set cpuarch = salt['grains.get']('cpuarch', '') %}

c:\disconnectRDP.cmd:
  file.managed:
     - source: salt://gui-test/disconnectRDP.cmd

c:\Users\{{ username }}\Desktop\disconnectRDP.cmd:
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

# since user prsent got bug for password, change password after set account
change_pwd_bug:
  module.run:
    - name: user.setpassword
    - m_name: {{ username }}
    - password: {{ password }}
    - watch:
      - user: {{ username }}

# another bug for user present
change_pwd_never_bug:
  cmd.run:
    - name: WMIC USERACCOUNT WHERE "Name='{{ username }}'" SET PasswordExpires=FALSE
    - m_name: {{ username }}

turn_off_uac:
  module.run:
    - name: reg.set_key
    - hkey: 'HKEY_LOCAL_MACHINE'
    - path: 'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System'
    - key: 'EnableLUA'
    - value: 0
    - vtype: 'REG_DWORD'

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
    - jenkins_jar: 'c:\jenkins\swarm-client-1.22-jar-with-dependencies.jar'
    - watch:
      - user: {{ username }}
      - module: change_pwd_bug