c:\disconnectRDP.cmd:
  file.managed:
     - source: salt://gui-test/disconnectRDP.cmd

auto_logon:
  autologon:
    - enable_user
    - username: eserv

'cn=msinstaller,cn=Administrator':
  user.present:
    - password: msiinstaller
    