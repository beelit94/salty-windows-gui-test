c:\jenkins:
  file.directory:
    - makedirs: True

c:\jenkins\slave.jar:
   file.managed:
     - source: http://10.140.28.218/jnlpJars/slave.jar
     - source_hash: md5=8bcdb2b68aba5c448c35d0c8e46b2e96

c:\jenkins\swarm-client-1.22-jar-with-dependencies.jar:
  file.managed:
    - source: http://maven.jenkins-ci.org/content/repositories/releases/org/jenkins-ci/plugins/swarm-client/1.22/swarm-client-1.22-jar-with-dependencies.jar
    - source_hash: md5=41a24ed0a6c9998ab1d0864371f213e1

archive.extracted:
    - name: c:\splunk_boot
    - source: http://releases.splunk.com/released_builds/6.2.3/splunk/windows/splunk-6.2.3-264376-windows-64.zip
    - source_hash: md5=9d747a4f3b2dfc5572c8c4f7f56fbec7
    - archive_format: zip