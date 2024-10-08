# coding: utf-8

"""
    Emby REST API
"""

import pprint
import re  # noqa: F401

import six

class SyncModelSyncDialogOptions(object):
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
        'targets': 'list[SyncSyncTarget]',
        'options': 'list[SyncModelSyncJobOption]',
        'quality_options': 'list[SyncModelSyncQualityOption]',
        'profile_options': 'list[SyncModelSyncProfileOption]'
    }

    attribute_map = {
        'targets': 'Targets',
        'options': 'Options',
        'quality_options': 'QualityOptions',
        'profile_options': 'ProfileOptions'
    }

    def __init__(self, targets=None, options=None, quality_options=None, profile_options=None):  # noqa: E501
        """SyncModelSyncDialogOptions - a model defined in Swagger"""  # noqa: E501
        self._targets = None
        self._options = None
        self._quality_options = None
        self._profile_options = None
        self.discriminator = None
        if targets is not None:
            self.targets = targets
        if options is not None:
            self.options = options
        if quality_options is not None:
            self.quality_options = quality_options
        if profile_options is not None:
            self.profile_options = profile_options

    @property
    def targets(self):
        """Gets the targets of this SyncModelSyncDialogOptions.  # noqa: E501


        :return: The targets of this SyncModelSyncDialogOptions.  # noqa: E501
        :rtype: list[SyncSyncTarget]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this SyncModelSyncDialogOptions.


        :param targets: The targets of this SyncModelSyncDialogOptions.  # noqa: E501
        :type: list[SyncSyncTarget]
        """

        self._targets = targets

    @property
    def options(self):
        """Gets the options of this SyncModelSyncDialogOptions.  # noqa: E501


        :return: The options of this SyncModelSyncDialogOptions.  # noqa: E501
        :rtype: list[SyncModelSyncJobOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this SyncModelSyncDialogOptions.


        :param options: The options of this SyncModelSyncDialogOptions.  # noqa: E501
        :type: list[SyncModelSyncJobOption]
        """

        self._options = options

    @property
    def quality_options(self):
        """Gets the quality_options of this SyncModelSyncDialogOptions.  # noqa: E501


        :return: The quality_options of this SyncModelSyncDialogOptions.  # noqa: E501
        :rtype: list[SyncModelSyncQualityOption]
        """
        return self._quality_options

    @quality_options.setter
    def quality_options(self, quality_options):
        """Sets the quality_options of this SyncModelSyncDialogOptions.


        :param quality_options: The quality_options of this SyncModelSyncDialogOptions.  # noqa: E501
        :type: list[SyncModelSyncQualityOption]
        """

        self._quality_options = quality_options

    @property
    def profile_options(self):
        """Gets the profile_options of this SyncModelSyncDialogOptions.  # noqa: E501


        :return: The profile_options of this SyncModelSyncDialogOptions.  # noqa: E501
        :rtype: list[SyncModelSyncProfileOption]
        """
        return self._profile_options

    @profile_options.setter
    def profile_options(self, profile_options):
        """Sets the profile_options of this SyncModelSyncDialogOptions.


        :param profile_options: The profile_options of this SyncModelSyncDialogOptions.  # noqa: E501
        :type: list[SyncModelSyncProfileOption]
        """

        self._profile_options = profile_options

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
        if issubclass(SyncModelSyncDialogOptions, dict):
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
        if not isinstance(other, SyncModelSyncDialogOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
