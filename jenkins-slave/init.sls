c:\jenkins:
  file.directory:
    - makedirs: True

c:\jenkins\slave.jar:
   file.managed:
     - source: http://10.140.28.218/jnlpJars/slave.jar
     - source_hash: md5=8bcdb2b68aba5c448c35d0c8e46b2e96