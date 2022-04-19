from ...zerotier.converters import ZeroTier as BaseZeroTier
from .base import OpenWrtConverter


class ZeroTier(OpenWrtConverter, BaseZeroTier):
    _uci_types = ['zerotier']

    def __intermediate_vpn(self, vpn):
        vpn = super().__intermediate_vpn(vpn, remove=[''])

        vpn.update(
            {
                '.name': self._get_uci_name(vpn.pop('name')).replace(' ', '_')
                + '_config',
                '.type': 'zerotier',
                'enabled': vpn.pop('enableBroadcast', '0'),
                'join': [vpn.pop('nwid')],
            }
        )
        for network_property in ['private', 'n']:
            if network_property in vpn:
                vpn.pop(network_property, None)
        return vpn

    def __netjson_vpn(self, vpn):
        # 'enabled' defaults to False in OpenWRT
        vpn['name'] = vpn.pop('.name')
        del vpn['.type']
        return super().__netjson_vpn(vpn)
