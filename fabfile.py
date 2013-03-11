from fabric.api import *
from fabric.contrib.files import exists
from fabric.contrib.project import upload_project

env['user'] = "ubuntu"

env.warn_only = True

def bootstrap():
  base_packages = [
    "libshadow-ruby1.8",
    "debhelper",
    "curl",
    "git-core",
    "bzip2",
    "zlib1g-dev",
    "libssl-dev",
    "libopenssl-ruby",
    "libreadline-dev",
    "ruby",
    "ruby-dev",
    "build-essential",
    "rubygems"
  ]
  run('sudo apt-get update')
  run('sudo apt-get upgrade -y')
  run('sudo apt-get install -y %s' % ' '.join(base_packages))
  run('sudo gem install --no-rdoc --no-ri chef ohai')

def chef():
  local("berks install --path=vendor/cookbooks")
  chef_binary = "/var/lib/gems/1.8/bin/chef-solo"
  if not exists(chef_binary): bootstrap()
  if not exists('/tmp/chef'): run('mkdir /tmp/chef')
  if not exists('/tmp/roles'): run('mkdir /tmp/roles')
  run('rm -rf /tmp/chef/*')
  run('rm -rf /tmp/roles/*')
  upload_project(local_dir="vendor/cookbooks", remote_dir="/tmp/chef")
  put('roles/monitor.json', '/tmp/roles/')
  put('monitor.json', '/tmp/chef/cookbooks')
  put('solo.rb', '/tmp/chef/cookbooks')
  run('cd /tmp/chef/cookbooks && sudo /var/lib/gems/1.8/bin/chef-solo -c solo.rb -j monitor.json')

