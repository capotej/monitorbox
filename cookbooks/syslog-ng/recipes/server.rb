require_recipe "syslog-ng"

directory "/mnt/log" do
  mode 0755
  recursive true
end

template "/etc/syslog-ng/syslog-ng.conf" do
  source "syslog-ng-server.conf.erb"
  owner "root"
  group "root"
  mode 0644
  notifies :restart, resources(:service => "syslog-ng")
end

directory node[:syslog_ng][:root] do
  owner "root"
  group "root"
end

directory node[:syslog_ng][:root] + "/syslog" do
  owner "root"
  group "root"
  mode 0750
  recursive true
end
