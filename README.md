# Monitor-in-a-Box

This will setup a graphite/statsd/syslog-server instance in AWS.

### Dependencies
* an aws account with a .pem key file
* gem install berksfile (ruby 1.9 only)
* pip install fabric

### Installation / Deployment

1. Setup a security group with at least ports 12311, 8125, and 22 open to 0.0.0.0/0 for both TCP and UDP (you can harden this up once you know which hosts will be talking to it, if you wish)
2. Start an instance (m1.small is fine) with this ami: **ami-fd4aa494** using the security group setup above
3. Once it's green on the dashboard, get its public hostname, like: **ec2-24-134-125-167.compute-1.amazonaws.com**
4. Start the chef run with: ```fab chef:hosts=ec2-24-134-125-167.compute-1.amazonaws.com -i path/to/awskey.pem```
5. This **will** take a long time due to compiling node.js, just wait it out

### Usage

Once your server is up, you should be able to go http://ec2-24-134-125-167.compute-1.amazonaws.com and see the graphite dashboard.

Username: **admin**

Password: **adminpassword123**

Statsd will be listening to metrics on port **8125**

This also sets up a logging server, listening for messages on **12311**

Externally received messages can be seen at: ```/mnt/log/external.log```
