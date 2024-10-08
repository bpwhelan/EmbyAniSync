# coding: utf-8

"""
    Emby REST API
"""

import pprint
import re  # noqa: F401

import six

class SyncModelSyncedItemProgress(object):
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
        'progress': 'float',
        'status': 'SyncModelSyncJobItemStatus'
    }

    attribute_map = {
        'progress': 'Progress',
        'status': 'Status'
    }

    def __init__(self, progress=None, status=None):  # noqa: E501
        """SyncModelSyncedItemProgress - a model defined in Swagger"""  # noqa: E501
        self._progress = None
        self._status = None
        self.discriminator = None
        if progress is not None:
            self.progress = progress
        if status is not None:
            self.status = status

    @property
    def progress(self):
        """Gets the progress of this SyncModelSyncedItemProgress.  # noqa: E501


        :return: The progress of this SyncModelSyncedItemProgress.  # noqa: E501
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this SyncModelSyncedItemProgress.


        :param progress: The progress of this SyncModelSyncedItemProgress.  # noqa: E501
        :type: float
        """

        self._progress = progress

    @property
    def status(self):
        """Gets the status of this SyncModelSyncedItemProgress.  # noqa: E501


        :return: The status of this SyncModelSyncedItemProgress.  # noqa: E501
        :rtype: SyncModelSyncJobItemStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SyncModelSyncedItemProgress.


        :param status: The status of this SyncModelSyncedItemProgress.  # noqa: E501
        :type: SyncModelSyncJobItemStatus
        """

        self._status = status

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
        if issubclass(SyncModelSyncedItemProgress, dict):
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
        if not isinstance(other, SyncModelSyncedItemProgress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
