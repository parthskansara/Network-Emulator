from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI


class LinuxRouter( Node ):

    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()


class NetworkTopo( Topo ):
    def build( self, **_opts ):
        r1 = self.addNode('r1', cls=LinuxRouter, ip='191.7.7.1/24')
        r2 = self.addNode('r2', cls=LinuxRouter, ip='191.7.1.3/24')
        r3 = self.addNode('r3', cls=LinuxRouter, ip='191.7.2.3/24')
        r4 = self.addNode('r4', cls=LinuxRouter, ip='191.7.5.1/24')

        h1 = self.addHost('h1', ip='191.7.7.2/24', defaultRoute='via 191.7.7.1')
        h2 = self.addHost('h2', ip='191.7.5.2/24', defaultRoute='via 191.7.5.1')

        self.addLink(h1, r1, intfName2='r1-eth0',params2={'ip' :'191.7.7.2/24'})
        self.addLink(h2, r4, intfName2='r4-eth0',params2={'ip' :'191.7.5.2/24'})

        self.addLink(r1, r2, intfName1='r1-eth1', intfName2='r2-eth0', params1={'ip':'191.7.1.2/24'}, params2={'ip':'191.7.1.3/24'})
        self.addLink(r1, r3, intfName1='r1-eth2', intfName2='r3-eth0', params1={'ip':'191.7.2.2/24'}, params2={'ip':'191.7.2.3/24'})
        self.addLink(r2, r4, intfName1='r2-eth1', intfName2='r4-eth1', params1={'ip':'191.7.3.4/24'}, params2={'ip':'191.7.3.5/24'})
        self.addLink(r3, r4, intfName1='r3-eth1', intfName2='r4-eth2', params1={'ip':'191.7.4.4/24'}, params2={'ip':'191.7.4.5/24'})

def run():
    topo = NetworkTopo()
    net = Mininet(topo=topo)
    net.start()
                                # add edge         via route    at destination interface
    info( net['r1'].cmd("ip route add 191.7.3.0/24 via 191.7.1.3 dev r1-eth1"))
    info( net['r1'].cmd("ip route add 191.7.4.0/24 via 191.7.2.3 dev r1-eth2"))
    info( net['r1'].cmd("ip route add 191.7.5.0/24 via 191.7.1.3 dev r1-eth1"))
    info( net['r1'].cmd("ip route add 191.7.5.0/24 via 191.7.2.3 dev r1-eth2"))

    info( net['r2'].cmd("ip route add 191.7.5.0/24 via 191.7.3.5 dev r2-eth1"))
    info( net['r2'].cmd("ip route add 191.7.7.0/24 via 191.7.1.2 dev r2-eth0"))
    info( net['r2'].cmd("ip route add 191.7.4.0/24 via 191.7.3.5 dev r2-eth1"))
    info( net['r2'].cmd("ip route add 191.7.2.0/24 via 191.7.1.2 dev r2-eth0"))

    info( net['r3'].cmd("ip route add 191.7.5.0/24 via 191.7.4.5 dev r3-eth1"))
    info( net['r3'].cmd("ip route add 191.7.7.0/24 via 191.7.2.2 dev r3-eth0"))
    info( net['r3'].cmd("ip route add 191.7.3.0/24 via 191.7.4.5 dev r3-eth1"))
    info( net['r3'].cmd("ip route add 191.7.1.0/24 via 191.7.2.2 dev r3-eth0"))

    info( net['r4'].cmd("ip route add 191.7.7.0/24 via 191.7.3.4 dev r4-eth1"))
    info( net['r4'].cmd("ip route add 191.7.1.0/24 via 191.7.3.4 dev r4-eth1"))
    info( net['r4'].cmd("ip route add 191.7.2.0/24 via 191.7.4.4 dev r4-eth2"))
    info( net['r4'].cmd("ip route add 191.7.7.0/24 via 191.7.4.4 dev r4-eth2"))
    

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    run()
