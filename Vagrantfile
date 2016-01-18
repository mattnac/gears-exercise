# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  # Bring up a loadbalancer node
  config.vm.box = "ubuntu/trusty64"
  config.vm.define "lb" do |lb|
    lb.vm.network :private_network, ip: "192.168.99.100"
    lb.vm.network "forwarded_port", guest: 80, host: 8080
  end

  # Change NO_OF_NODES to specify number of webserver nodes to bring up
  NO_OF_NODES = 3
  (1..NO_OF_NODES).each do |id|
    config.vm.define "web#{id}" do |server|
      server.vm.network :private_network, ip: "192.168.99.#{100+id}"
      server.vm.hostname = "web#{id}"
      if id == NO_OF_NODES
        server.vm.provision "ansible" do |ansible|
          ansible.playbook = "site.yml"
          ansible.limit = 'all'
        end
      end
    end
  end
end
