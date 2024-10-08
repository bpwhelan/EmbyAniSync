# coding: utf-8

"""
    Emby REST API
"""

import pprint
import re  # noqa: F401

import six

class LiveTVApiGetPrograms(object):
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
        'is_airing': 'bool',
        'tag_ids': 'str',
        'exclude_item_ids': 'str',
        'enable_total_record_count': 'bool',
        'series_timer_id': 'str',
        'library_series_id': 'str',
        'series_from_program_id': 'str',
        'showings_from_program_id': 'str',
        'group_programs_by_series': 'bool'
    }

    attribute_map = {
        'is_airing': 'IsAiring',
        'tag_ids': 'TagIds',
        'exclude_item_ids': 'ExcludeItemIds',
        'enable_total_record_count': 'EnableTotalRecordCount',
        'series_timer_id': 'SeriesTimerId',
        'library_series_id': 'LibrarySeriesId',
        'series_from_program_id': 'SeriesFromProgramId',
        'showings_from_program_id': 'ShowingsFromProgramId',
        'group_programs_by_series': 'GroupProgramsBySeries'
    }

    def __init__(self, is_airing=None, tag_ids=None, exclude_item_ids=None, enable_total_record_count=None, series_timer_id=None, library_series_id=None, series_from_program_id=None, showings_from_program_id=None, group_programs_by_series=None):  # noqa: E501
        """LiveTVApiGetPrograms - a model defined in Swagger"""  # noqa: E501
        self._is_airing = None
        self._tag_ids = None
        self._exclude_item_ids = None
        self._enable_total_record_count = None
        self._series_timer_id = None
        self._library_series_id = None
        self._series_from_program_id = None
        self._showings_from_program_id = None
        self._group_programs_by_series = None
        self.discriminator = None
        if is_airing is not None:
            self.is_airing = is_airing
        if tag_ids is not None:
            self.tag_ids = tag_ids
        if exclude_item_ids is not None:
            self.exclude_item_ids = exclude_item_ids
        if enable_total_record_count is not None:
            self.enable_total_record_count = enable_total_record_count
        if series_timer_id is not None:
            self.series_timer_id = series_timer_id
        if library_series_id is not None:
            self.library_series_id = library_series_id
        if series_from_program_id is not None:
            self.series_from_program_id = series_from_program_id
        if showings_from_program_id is not None:
            self.showings_from_program_id = showings_from_program_id
        if group_programs_by_series is not None:
            self.group_programs_by_series = group_programs_by_series

    @property
    def is_airing(self):
        """Gets the is_airing of this LiveTVApiGetPrograms.  # noqa: E501


        :return: The is_airing of this LiveTVApiGetPrograms.  # noqa: E501
        :rtype: bool
        """
        return self._is_airing

    @is_airing.setter
    def is_airing(self, is_airing):
        """Sets the is_airing of this LiveTVApiGetPrograms.


        :param is_airing: The is_airing of this LiveTVApiGetPrograms.  # noqa: E501
        :type: bool
        """

        self._is_airing = is_airing

    @property
    def tag_ids(self):
        """Gets the tag_ids of this LiveTVApiGetPrograms.  # noqa: E501


        :return: The tag_ids of this LiveTVApiGetPrograms.  # noqa: E501
        :rtype: str
        """
        return self._tag_ids

    @tag_ids.setter
    def tag_ids(self, tag_ids):
        """Sets the tag_ids of this LiveTVApiGetPrograms.


        :param tag_ids: The tag_ids of this LiveTVApiGetPrograms.  # noqa: E501
        :type: str
        """

        self._tag_ids = tag_ids

    @property
    def exclude_item_ids(self):
        """Gets the exclude_item_ids of this LiveTVApiGetPrograms.  # noqa: E501


        :return: The exclude_item_ids of this LiveTVApiGetPrograms.  # noqa: E501
        :rtype: str
        """
        return self._exclude_item_ids

    @exclude_item_ids.setter
    def exclude_item_ids(self, exclude_item_ids):
        """Sets the exclude_item_ids of this LiveTVApiGetPrograms.


        :param exclude_item_ids: The exclude_item_ids of this LiveTVApiGetPrograms.  # noqa: E501
        :type: str
        """

        self._exclude_item_ids = exclude_item_ids

    @property
    def enable_total_record_count(self):
        """Gets the enable_total_record_count of this LiveTVApiGetPrograms.  # noqa: E501


        :return: The enable_total_record_count of this LiveTVApiGetPrograms.  # noqa: E501
        :rtype: bool
        """
        return self._enable_total_record_count

    @enable_total_record_count.setter
    def enable_total_record_count(self, enable_total_record_count):
        """Sets the enable_total_record_count of this LiveTVApiGetPrograms.


        :param enable_total_record_count: The enable_total_record_count of this LiveTVApiGetPrograms.  # noqa: E501
        :type: bool
        """

        self._enable_total_record_count = enable_total_record_count

    @property
    def series_timer_id(self):
        """Gets the series_timer_id of this LiveTVApiGetPrograms.  # noqa: E501


        :return: The series_timer_id of this LiveTVApiGetPrograms.  # noqa: E501
        :rtype: str
        """
        return self._series_timer_id

    @series_timer_id.setter
    def series_timer_id(self, series_timer_id):
        """Sets the series_timer_id of this LiveTVApiGetPrograms.


        :param series_timer_id: The series_timer_id of this LiveTVApiGetPrograms.  # noqa: E501
        :type: str
        """

        self._series_timer_id = series_timer_id

    @property
    def library_series_id(self):
        """Gets the library_series_id of this LiveTVApiGetPrograms.  # noqa: E501


        :return: The library_series_id of this LiveTVApiGetPrograms.  # noqa: E501
        :rtype: str
        """
        return self._library_series_id

    @library_series_id.setter
    def library_series_id(self, library_series_id):
        """Sets the library_series_id of this LiveTVApiGetPrograms.


        :param library_series_id: The library_series_id of this LiveTVApiGetPrograms.  # noqa: E501
        :type: str
        """

        self._library_series_id = library_series_id

    @property
    def series_from_program_id(self):
        """Gets the series_from_program_id of this LiveTVApiGetPrograms.  # noqa: E501


        :return: The series_from_program_id of this LiveTVApiGetPrograms.  # noqa: E501
        :rtype: str
        """
        return self._series_from_program_id

    @series_from_program_id.setter
    def series_from_program_id(self, series_from_program_id):
        """Sets the series_from_program_id of this LiveTVApiGetPrograms.


        :param series_from_program_id: The series_from_program_id of this LiveTVApiGetPrograms.  # noqa: E501
        :type: str
        """

        self._series_from_program_id = series_from_program_id

    @property
    def showings_from_program_id(self):
        """Gets the showings_from_program_id of this LiveTVApiGetPrograms.  # noqa: E501


        :return: The showings_from_program_id of this LiveTVApiGetPrograms.  # noqa: E501
        :rtype: str
        """
        return self._showings_from_program_id

    @showings_from_program_id.setter
    def showings_from_program_id(self, showings_from_program_id):
        """Sets the showings_from_program_id of this LiveTVApiGetPrograms.


        :param showings_from_program_id: The showings_from_program_id of this LiveTVApiGetPrograms.  # noqa: E501
        :type: str
        """

        self._showings_from_program_id = showings_from_program_id

    @property
    def group_programs_by_series(self):
        """Gets the group_programs_by_series of this LiveTVApiGetPrograms.  # noqa: E501


        :return: The group_programs_by_series of this LiveTVApiGetPrograms.  # noqa: E501
        :rtype: bool
        """
        return self._group_programs_by_series

    @group_programs_by_series.setter
    def group_programs_by_series(self, group_programs_by_series):
        """Sets the group_programs_by_series of this LiveTVApiGetPrograms.


        :param group_programs_by_series: The group_programs_by_series of this LiveTVApiGetPrograms.  # noqa: E501
        :type: bool
        """

        self._group_programs_by_series = group_programs_by_series

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
        if issubclass(LiveTVApiGetPrograms, dict):
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
        if not isinstance(other, LiveTVApiGetPrograms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
