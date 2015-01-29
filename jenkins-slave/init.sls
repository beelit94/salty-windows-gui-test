c:\jenkins:
  file.directory:
    - makedirs: True

c:\jenkins\slave.jar:
   file.managed:
     - source: http://10.140.28.218/jnlpJars/slave.jar