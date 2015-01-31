c:\disconnectRDP.cmd:
  file.managed:
     - source: salt://gui-test/disconnectRDP.cmd

auto_logon:
  autologon:
    - enable_user
    - username: msiinstaller
    - password: msiinstaller

msinstaller:
  user.present:
    - password: msiinstaller
    - description: 'test account for msi installer'
    - groups:
      - Administrators

power_cfg:
  cmd.script:
    - source: salt://gui-test/powercfg_high.cmd
    - cwd: /