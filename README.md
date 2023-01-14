# Network-Emulator

## Table of Contents:
* [Introduction](#introduction)
* [Libraries used](#libraries-used)
* [Run the project](#run-the-project)
* [Analysis](#analysis)
* [Source](#source)

## Introduction:
In this project, we perform network emulation using Mininet. We create our own network topology, as shown [here](LINK). We also implement routing protocols, to build routes from the source to the destination.

Lastly, we use the IPerf test to gain insights about the TCP bandwith in our emulated network.

## Libraries used
* [mininet](http://mininet.org/api/annotated.html)


## Run the project

To run the project, we first need to setup Mininet in a VM. 

### Mininet Setup

#### For Windows:
1. Install a Virtual Machine Software (recommended: [Oracle VM](https://www.virtualbox.org/wiki/Downloads))


2. Download the mininet VM image [here](https://github.com/mininet/mininet/releases/download/2.3.0/mininet-2.3.0-210211-ubuntu-18.04.5-server-amd64-ovf.zip)

3. Import the VM image into virtual box  (You can double-click to open in virtual box)

4. Default setup will be good and you can increase the RAM to 4GB if you want

5. Open the mininet VM.

6. username and password are both mininet

#### For Linux Ubuntu:

1. You can get source code 

`git clone git://github.com/mininet/mininet`

2. Then you can run the command: 

`mininet/util/install.sh -a`

3. You can run the following command to test:

`sudo mn --switch ovsbr --test pingall`

All this above you can find in [here](http://mininet.org/download/)

#### For Mac M1:

1. If you are an M1 user, you cannot install virtualbox. There are two
workarounds: the cloud or using VMWare Fusion

2. If you are using the cloud, you can get free versions (e.g., AWS EC2 gives
you free tiers for Linux VMs, Alibaba cloud platform also gives you free tiers), or
you can get paid versions from Linode, EC2, Alibaba and many others.

3. Another possible workaround is to use VMWare Fusion and UTM as a
replacement for VirtualBox. 

### Uploading files:

1. Get the files using the following command:

```bash
# Clone this repository
$ git clone https://github.com/parthskansara/Network-Emulator.git
```

2. For VirtualBox Shared Folders, install guest utilities with this command: 

`sudo apt-get install virtualbox-guest-utils`

a. Add the folder using Devices → Shared Folders and make the
drive <ins>*auto-mount*</ins> and <ins>*permanent*</ins>. Restart the VM, and your folder will be under `/media`

b. To access the folder, you will need to add the mininet user to the
group **vboxsf** using the following command:

`sudo adduser mininet vboxsf`

c. Reboot

### Run the Network Emulator
This emulator configures a network with static routes. For dynamic routing, check [this](#run-the-dynamic-routing-emulator).

1. Move into the project directory using the following command:

`cd path to media/Network-Emulator`

2. Install dependencies using the following command:

`pip install -r requirements.txt`

* #### Basic Emulator with static routes
This emulator configures a network with static routes. For dynamic routing, check [this](#run-the-dynamic-routing-emulator).

a. Run the emulator using the following command. It creates a custom topology as shown [here](LINK).
 
`python emulator.py`


* #### Dynamic Routing Emulator
This emulator configures a network with dynamic routing. We use BIRD for running the RIP protocol, which can assign alternative routes in case a link is down. 

a. Install BIRD. You can use the instructions given [here]( https://gitlab.labs.nic.cz/labs/bird/).

b. Run the emulator using the following command:

 `python RIP-emulator.py`
 
 
 ### Run the IPerf test

We will perform an IPerf test of H1 as a host and H2 is the server to perform a TCP bandwidth test. We have 3 files with different configurations for the routers:
* iperf-test-10kb.py: Buffer size is 10KB
* iperf-test-5mb.py: Buffer size is 5MB
* iperf-test-25mb.py: Buffer size is 25MB

The bandwidth in each case is set to 100Mbps and the delay at each router is set to 30 ms.

Run the IPerf tests using the following commands:

```bash
# Buffer size = 10KB
$ python iperf-test-10kb.py

# Buffer size = 5MB
$ python iperf-test-5mb.py

# Buffer size = 25MB
$ python iperf-test-25mb.py

```


## Analysis
1. This [document](LINK) explains the working of the Basic Emulator.

2. This [document](LINK) explains the working of the RIP Emulator.

3. This [document](LINK) explains the IPerf Test.

## Source
This project was completed as a part of the course CSE 534: Fundamentals of Computer Vision (Fall 2022) under [Prof. Aruna Balasubramanian](https://www.cs.stonybrook.edu/people/faculty/ArunaBalasubramanian) at Stony Brook University.


The original assignment can be found [here](https://drive.google.com/file/d/1PN7ALmftR3wQLpY1RtAhNpfL3hOTNUHW/view?usp=sharing).
