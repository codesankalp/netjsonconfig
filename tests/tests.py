from netjsonconfig.backends.openwrt.openwrt import OpenWrt
from netjsonconfig.backends.zerotier.zerotier import ZeroTier

config = {
    "zerotier": [
        {
            "name": "network1",
            "enableBroadcast": True,
            "id": "6ab565387ae448c5",
            "private": False,
        },
        {
            "name": "network2 sample",
            "enableBroadcast": False,
            "id": "8056c2e21c000009",
            "private": True,
        },
    ]
}

print(ZeroTier(config).render())
# output partially matches with conf in /var/lib/zerotier-one/{id}.conf:
"""
# zerotier config: 6ab565387ae448c5

enableBroadcast=True
n=network1
nwid=6ab565387ae448c5
private=False

# zerotier config: 8056c2e21c000009

enableBroadcast=False
n=network2
nwid=8056c2e21c000009
private=True
"""

print(OpenWrt(config).render())
# output will be:
"""
package zerotier

config zerotier 'network1_config'
        option enabled '1'
        list join '6ab565387ae448c5'

config zerotier 'network2_sample_config'
        option enabled '0'
        list join '8056c2e21c000009'
"""
