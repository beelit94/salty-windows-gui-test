{% set username = 'msinstaller' %}
{% set password = 'win9@fanbiejap' %}

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

jenkins_swarm_plugin:
  cmd.run:
    - name: 'SCHTASKS /Create /SC ONLOGON /TN jenkins /TR "java -jar c:\jenkins\swarm-client-1.22-jar-with-dependencies.jar -executors 1 -master http://10.140.28.218:8080 -" /RU {{ username }} /RP {{ password }} /RL HIGHEST /IT /F'
    - watch:
      - user.present: {{ username }}