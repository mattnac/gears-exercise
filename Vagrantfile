# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/trusty64"
  config.vm.define "lb" do |lb|
    lb.vm.network :private_network, ip: "192.168.99.100"
    lb.vm.network "forwarded_port", guest: 80, host: 8080
  end
  N = 5
  (1..N).each do |id|
    config.vm.define "web#{id}" do |server|
      server.vm.network :private_network, ip: "192.168.99.#{10+id}"
      server.vm.hostname = "web#{id}"
      if id == N
        server.vm.provision "ansible" do |ansible|
          ansible.playbook = "site.yml"
          ansible.limit = 'all'
        end
      end
    end
  end
end

# Change N to change number of nodes deployed
#    config.vm.define "web02" do |web02|
#      web02.vm.network :private_network, ip: "192.168.99.102"
#    end
#    config.vm.define "web03" do |web03|
#      web03.vm.network :private_network, ip: "192.168.99.103"
#    end
