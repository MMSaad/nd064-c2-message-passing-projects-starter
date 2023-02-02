Vagrant.configure("2") do |config|

  config.vm.define "master" do |master|
    master.vm.box = "opensuse/Leap-15.4.x86_64"
    master.vm.box_version = "15.4.13.7"
    master.vm.hostname = "master"
    master.vm.network 'private_network', ip: "192.168.0.200",  virtualbox__intnet: true
    master.vm.network "forwarded_port", guest: 22, host: 2222, id: "ssh", disabled: true
    master.vm.network "forwarded_port", guest: 22, host: 2000 # Master Node SSH
    master.vm.network "forwarded_port", guest: 6443, host: 6443 # API Access
    master.vm.network "forwarded_port", guest: 5432, host: 5432 # PG
    for p in 30000..30100 # expose NodePort IP's
      master.vm.network "forwarded_port", guest: p, host: p, protocol: "tcp"
      end
    master.vm.provider "virtualbox" do |v|
      v.memory = "8192"
      v.cpus = 2
      v.name = "master"
      end
    master.vm.provision "shell", inline: <<-SHELL
      sudo zypper refresh
      sudo zypper --non-interactive install bzip2
      sudo zypper --non-interactive install etcd
      sudo zypper --non-interactive install apparmor-parser
      curl -sfL https://get.k3s.io | sh -
    SHELL
  end
end