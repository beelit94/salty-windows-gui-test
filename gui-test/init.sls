c:\disconnectRDP.cmd:
  file.managed:
     - source: salt://gui-test/disconnectRDP.cmd

auto_logon:
  autologon:
    - enable_user
    - username: eserv

msinstaller:
  user.present:
    - password: msiinstaller
    - group:
      - Administrators