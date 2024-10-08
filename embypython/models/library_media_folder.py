# coding: utf-8

"""
    Emby REST API
"""

import pprint
import re  # noqa: F401

import six

class LibraryMediaFolder(object):
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
        'name': 'str',
        'id': 'str',
        'sub_folders': 'list[LibrarySubFolder]'
    }

    attribute_map = {
        'name': 'Name',
        'id': 'Id',
        'sub_folders': 'SubFolders'
    }

    def __init__(self, name=None, id=None, sub_folders=None):  # noqa: E501
        """LibraryMediaFolder - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._id = None
        self._sub_folders = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if sub_folders is not None:
            self.sub_folders = sub_folders

    @property
    def name(self):
        """Gets the name of this LibraryMediaFolder.  # noqa: E501


        :return: The name of this LibraryMediaFolder.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LibraryMediaFolder.


        :param name: The name of this LibraryMediaFolder.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this LibraryMediaFolder.  # noqa: E501


        :return: The id of this LibraryMediaFolder.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LibraryMediaFolder.


        :param id: The id of this LibraryMediaFolder.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def sub_folders(self):
        """Gets the sub_folders of this LibraryMediaFolder.  # noqa: E501


        :return: The sub_folders of this LibraryMediaFolder.  # noqa: E501
        :rtype: list[LibrarySubFolder]
        """
        return self._sub_folders

    @sub_folders.setter
    def sub_folders(self, sub_folders):
        """Sets the sub_folders of this LibraryMediaFolder.


        :param sub_folders: The sub_folders of this LibraryMediaFolder.  # noqa: E501
        :type: list[LibrarySubFolder]
        """

        self._sub_folders = sub_folders

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
        if issubclass(LibraryMediaFolder, dict):
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
        if not isinstance(other, LibraryMediaFolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
