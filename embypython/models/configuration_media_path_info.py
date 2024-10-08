# coding: utf-8

"""
    Emby REST API
"""

import pprint
import re  # noqa: F401

import six

class ConfigurationMediaPathInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'path': 'str',
        'network_path': 'str'
    }

    attribute_map = {
        'path': 'Path',
        'network_path': 'NetworkPath'
    }

    def __init__(self, path=None, network_path=None):  # noqa: E501
        """ConfigurationMediaPathInfo - a model defined in Swagger"""  # noqa: E501
        self._path = None
        self._network_path = None
        self.discriminator = None
        if path is not None:
            self.path = path
        if network_path is not None:
            self.network_path = network_path

    @property
    def path(self):
        """Gets the path of this ConfigurationMediaPathInfo.  # noqa: E501


        :return: The path of this ConfigurationMediaPathInfo.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ConfigurationMediaPathInfo.


        :param path: The path of this ConfigurationMediaPathInfo.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def network_path(self):
        """Gets the network_path of this ConfigurationMediaPathInfo.  # noqa: E501


        :return: The network_path of this ConfigurationMediaPathInfo.  # noqa: E501
        :rtype: str
        """
        return self._network_path

    @network_path.setter
    def network_path(self, network_path):
        """Sets the network_path of this ConfigurationMediaPathInfo.


        :param network_path: The network_path of this ConfigurationMediaPathInfo.  # noqa: E501
        :type: str
        """

        self._network_path = network_path

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ConfigurationMediaPathInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConfigurationMediaPathInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
