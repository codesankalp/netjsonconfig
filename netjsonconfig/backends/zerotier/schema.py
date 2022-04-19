"""
ZeroTier specific JSON-Schema definition
"""

from copy import deepcopy

from ...schema import schema as default_schema

# missing properties from this schema are:
# authTokens, capabilities, lastModified, mtu, multicastLimit,
# remoteTraceLevel, remoteTraceTarget, routes, rules, v4AssignMode,
# v6AssignMode, dns, ssoConfig, tags
base_zerotier_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "additionalProperties": True,
    "properties": {
        "zerotier": {
            "type": "array",
            "title": "ZeroTier",
            "uniqueItems": True,
            "additionalItems": True,
            "propertyOrder": 12,
            "items": {
                "type": "object",
                "title": "ZerotTier tunnel",
                "additionalProperties": True,
                "required": ["name", "id", "enableBroadcast"],
                "properties": {
                    "name": {
                        "title": "network name",
                        "description": "Zerotier Network name",
                        "type": "string",
                    },
                    "id": {
                        "title": "network id",
                        "description": "Zerotier Network ID",
                        "type": "string",
                        "minLength": 16,
                        "maxLength": 16,
                    },
                    "enableBroadcast": {
                        "title": "enable broadcast",
                        "type": "boolean",
                        "description": "Enable broadcast packets on the network",
                    },
                    "creationTime": {
                        "title": "creation time",
                        "type": "integer",
                        "description": "Creation time of the network.",
                    },
                    "private": {
                        "title": "private",
                        "type": "boolean",
                        "description": "Whether or not the network is private.  If false, members will *NOT* need to be authorized to join.",
                    },
                },
            },
        }
    },
}

schema = deepcopy(base_zerotier_schema)
schema['properties']['files'] = default_schema['properties']['files']
