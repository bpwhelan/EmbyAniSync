# coding: utf-8

"""
    Emby REST API
"""

import pprint
import re  # noqa: F401

import six

class DlnaTranscodingProfile(object):
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
        'container': 'str',
        'type': 'DlnaDlnaProfileType',
        'video_codec': 'str',
        'audio_codec': 'str',
        'protocol': 'str',
        'estimate_content_length': 'bool',
        'enable_mpegts_m2_ts_mode': 'bool',
        'transcode_seek_info': 'DlnaTranscodeSeekInfo',
        'copy_timestamps': 'bool',
        'context': 'DlnaEncodingContext',
        'max_audio_channels': 'str',
        'min_segments': 'int',
        'segment_length': 'int',
        'break_on_non_key_frames': 'bool',
        'allow_interlaced_video_stream_copy': 'bool',
        'manifest_subtitles': 'str',
        'max_manifest_subtitles': 'int'
    }

    attribute_map = {
        'container': 'Container',
        'type': 'Type',
        'video_codec': 'VideoCodec',
        'audio_codec': 'AudioCodec',
        'protocol': 'Protocol',
        'estimate_content_length': 'EstimateContentLength',
        'enable_mpegts_m2_ts_mode': 'EnableMpegtsM2TsMode',
        'transcode_seek_info': 'TranscodeSeekInfo',
        'copy_timestamps': 'CopyTimestamps',
        'context': 'Context',
        'max_audio_channels': 'MaxAudioChannels',
        'min_segments': 'MinSegments',
        'segment_length': 'SegmentLength',
        'break_on_non_key_frames': 'BreakOnNonKeyFrames',
        'allow_interlaced_video_stream_copy': 'AllowInterlacedVideoStreamCopy',
        'manifest_subtitles': 'ManifestSubtitles',
        'max_manifest_subtitles': 'MaxManifestSubtitles'
    }

    def __init__(self, container=None, type=None, video_codec=None, audio_codec=None, protocol=None, estimate_content_length=None, enable_mpegts_m2_ts_mode=None, transcode_seek_info=None, copy_timestamps=None, context=None, max_audio_channels=None, min_segments=None, segment_length=None, break_on_non_key_frames=None, allow_interlaced_video_stream_copy=None, manifest_subtitles=None, max_manifest_subtitles=None):  # noqa: E501
        """DlnaTranscodingProfile - a model defined in Swagger"""  # noqa: E501
        self._container = None
        self._type = None
        self._video_codec = None
        self._audio_codec = None
        self._protocol = None
        self._estimate_content_length = None
        self._enable_mpegts_m2_ts_mode = None
        self._transcode_seek_info = None
        self._copy_timestamps = None
        self._context = None
        self._max_audio_channels = None
        self._min_segments = None
        self._segment_length = None
        self._break_on_non_key_frames = None
        self._allow_interlaced_video_stream_copy = None
        self._manifest_subtitles = None
        self._max_manifest_subtitles = None
        self.discriminator = None
        if container is not None:
            self.container = container
        if type is not None:
            self.type = type
        if video_codec is not None:
            self.video_codec = video_codec
        if audio_codec is not None:
            self.audio_codec = audio_codec
        if protocol is not None:
            self.protocol = protocol
        if estimate_content_length is not None:
            self.estimate_content_length = estimate_content_length
        if enable_mpegts_m2_ts_mode is not None:
            self.enable_mpegts_m2_ts_mode = enable_mpegts_m2_ts_mode
        if transcode_seek_info is not None:
            self.transcode_seek_info = transcode_seek_info
        if copy_timestamps is not None:
            self.copy_timestamps = copy_timestamps
        if context is not None:
            self.context = context
        if max_audio_channels is not None:
            self.max_audio_channels = max_audio_channels
        if min_segments is not None:
            self.min_segments = min_segments
        if segment_length is not None:
            self.segment_length = segment_length
        if break_on_non_key_frames is not None:
            self.break_on_non_key_frames = break_on_non_key_frames
        if allow_interlaced_video_stream_copy is not None:
            self.allow_interlaced_video_stream_copy = allow_interlaced_video_stream_copy
        if manifest_subtitles is not None:
            self.manifest_subtitles = manifest_subtitles
        if max_manifest_subtitles is not None:
            self.max_manifest_subtitles = max_manifest_subtitles

    @property
    def container(self):
        """Gets the container of this DlnaTranscodingProfile.  # noqa: E501


        :return: The container of this DlnaTranscodingProfile.  # noqa: E501
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this DlnaTranscodingProfile.


        :param container: The container of this DlnaTranscodingProfile.  # noqa: E501
        :type: str
        """

        self._container = container

    @property
    def type(self):
        """Gets the type of this DlnaTranscodingProfile.  # noqa: E501


        :return: The type of this DlnaTranscodingProfile.  # noqa: E501
        :rtype: DlnaDlnaProfileType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DlnaTranscodingProfile.


        :param type: The type of this DlnaTranscodingProfile.  # noqa: E501
        :type: DlnaDlnaProfileType
        """

        self._type = type

    @property
    def video_codec(self):
        """Gets the video_codec of this DlnaTranscodingProfile.  # noqa: E501


        :return: The video_codec of this DlnaTranscodingProfile.  # noqa: E501
        :rtype: str
        """
        return self._video_codec

    @video_codec.setter
    def video_codec(self, video_codec):
        """Sets the video_codec of this DlnaTranscodingProfile.


        :param video_codec: The video_codec of this DlnaTranscodingProfile.  # noqa: E501
        :type: str
        """

        self._video_codec = video_codec

    @property
    def audio_codec(self):
        """Gets the audio_codec of this DlnaTranscodingProfile.  # noqa: E501


        :return: The audio_codec of this DlnaTranscodingProfile.  # noqa: E501
        :rtype: str
        """
        return self._audio_codec

    @audio_codec.setter
    def audio_codec(self, audio_codec):
        """Sets the audio_codec of this DlnaTranscodingProfile.


        :param audio_codec: The audio_codec of this DlnaTranscodingProfile.  # noqa: E501
        :type: str
        """

        self._audio_codec = audio_codec

    @property
    def protocol(self):
        """Gets the protocol of this DlnaTranscodingProfile.  # noqa: E501


        :return: The protocol of this DlnaTranscodingProfile.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this DlnaTranscodingProfile.


        :param protocol: The protocol of this DlnaTranscodingProfile.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def estimate_content_length(self):
        """Gets the estimate_content_length of this DlnaTranscodingProfile.  # noqa: E501


        :return: The estimate_content_length of this DlnaTranscodingProfile.  # noqa: E501
        :rtype: bool
        """
        return self._estimate_content_length

    @estimate_content_length.setter
    def estimate_content_length(self, estimate_content_length):
        """Sets the estimate_content_length of this DlnaTranscodingProfile.


        :param estimate_content_length: The estimate_content_length of this DlnaTranscodingProfile.  # noqa: E501
        :type: bool
        """

        self._estimate_content_length = estimate_content_length

    @property
    def enable_mpegts_m2_ts_mode(self):
        """Gets the enable_mpegts_m2_ts_mode of this DlnaTranscodingProfile.  # noqa: E501


        :return: The enable_mpegts_m2_ts_mode of this DlnaTranscodingProfile.  # noqa: E501
        :rtype: bool
        """
        return self._enable_mpegts_m2_ts_mode

    @enable_mpegts_m2_ts_mode.setter
    def enable_mpegts_m2_ts_mode(self, enable_mpegts_m2_ts_mode):
        """Sets the enable_mpegts_m2_ts_mode of this DlnaTranscodingProfile.


        :param enable_mpegts_m2_ts_mode: The enable_mpegts_m2_ts_mode of this DlnaTranscodingProfile.  # noqa: E501
        :type: bool
        """

        self._enable_mpegts_m2_ts_mode = enable_mpegts_m2_ts_mode

    @property
    def transcode_seek_info(self):
        """Gets the transcode_seek_info of this DlnaTranscodingProfile.  # noqa: E501


        :return: The transcode_seek_info of this DlnaTranscodingProfile.  # noqa: E501
        :rtype: DlnaTranscodeSeekInfo
        """
        return self._transcode_seek_info

    @transcode_seek_info.setter
    def transcode_seek_info(self, transcode_seek_info):
        """Sets the transcode_seek_info of this DlnaTranscodingProfile.


        :param transcode_seek_info: The transcode_seek_info of this DlnaTranscodingProfile.  # noqa: E501
        :type: DlnaTranscodeSeekInfo
        """

        self._transcode_seek_info = transcode_seek_info

    @property
    def copy_timestamps(self):
        """Gets the copy_timestamps of this DlnaTranscodingProfile.  # noqa: E501


        :return: The copy_timestamps of this DlnaTranscodingProfile.  # noqa: E501
        :rtype: bool
        """
        return self._copy_timestamps

    @copy_timestamps.setter
    def copy_timestamps(self, copy_timestamps):
        """Sets the copy_timestamps of this DlnaTranscodingProfile.


        :param copy_timestamps: The copy_timestamps of this DlnaTranscodingProfile.  # noqa: E501
        :type: bool
        """

        self._copy_timestamps = copy_timestamps

    @property
    def context(self):
        """Gets the context of this DlnaTranscodingProfile.  # noqa: E501


        :return: The context of this DlnaTranscodingProfile.  # noqa: E501
        :rtype: DlnaEncodingContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this DlnaTranscodingProfile.


        :param context: The context of this DlnaTranscodingProfile.  # noqa: E501
        :type: DlnaEncodingContext
        """

        self._context = context

    @property
    def max_audio_channels(self):
        """Gets the max_audio_channels of this DlnaTranscodingProfile.  # noqa: E501


        :return: The max_audio_channels of this DlnaTranscodingProfile.  # noqa: E501
        :rtype: str
        """
        return self._max_audio_channels

    @max_audio_channels.setter
    def max_audio_channels(self, max_audio_channels):
        """Sets the max_audio_channels of this DlnaTranscodingProfile.


        :param max_audio_channels: The max_audio_channels of this DlnaTranscodingProfile.  # noqa: E501
        :type: str
        """

        self._max_audio_channels = max_audio_channels

    @property
    def min_segments(self):
        """Gets the min_segments of this DlnaTranscodingProfile.  # noqa: E501


        :return: The min_segments of this DlnaTranscodingProfile.  # noqa: E501
        :rtype: int
        """
        return self._min_segments

    @min_segments.setter
    def min_segments(self, min_segments):
        """Sets the min_segments of this DlnaTranscodingProfile.


        :param min_segments: The min_segments of this DlnaTranscodingProfile.  # noqa: E501
        :type: int
        """

        self._min_segments = min_segments

    @property
    def segment_length(self):
        """Gets the segment_length of this DlnaTranscodingProfile.  # noqa: E501


        :return: The segment_length of this DlnaTranscodingProfile.  # noqa: E501
        :rtype: int
        """
        return self._segment_length

    @segment_length.setter
    def segment_length(self, segment_length):
        """Sets the segment_length of this DlnaTranscodingProfile.


        :param segment_length: The segment_length of this DlnaTranscodingProfile.  # noqa: E501
        :type: int
        """

        self._segment_length = segment_length

    @property
    def break_on_non_key_frames(self):
        """Gets the break_on_non_key_frames of this DlnaTranscodingProfile.  # noqa: E501


        :return: The break_on_non_key_frames of this DlnaTranscodingProfile.  # noqa: E501
        :rtype: bool
        """
        return self._break_on_non_key_frames

    @break_on_non_key_frames.setter
    def break_on_non_key_frames(self, break_on_non_key_frames):
        """Sets the break_on_non_key_frames of this DlnaTranscodingProfile.


        :param break_on_non_key_frames: The break_on_non_key_frames of this DlnaTranscodingProfile.  # noqa: E501
        :type: bool
        """

        self._break_on_non_key_frames = break_on_non_key_frames

    @property
    def allow_interlaced_video_stream_copy(self):
        """Gets the allow_interlaced_video_stream_copy of this DlnaTranscodingProfile.  # noqa: E501


        :return: The allow_interlaced_video_stream_copy of this DlnaTranscodingProfile.  # noqa: E501
        :rtype: bool
        """
        return self._allow_interlaced_video_stream_copy

    @allow_interlaced_video_stream_copy.setter
    def allow_interlaced_video_stream_copy(self, allow_interlaced_video_stream_copy):
        """Sets the allow_interlaced_video_stream_copy of this DlnaTranscodingProfile.


        :param allow_interlaced_video_stream_copy: The allow_interlaced_video_stream_copy of this DlnaTranscodingProfile.  # noqa: E501
        :type: bool
        """

        self._allow_interlaced_video_stream_copy = allow_interlaced_video_stream_copy

    @property
    def manifest_subtitles(self):
        """Gets the manifest_subtitles of this DlnaTranscodingProfile.  # noqa: E501


        :return: The manifest_subtitles of this DlnaTranscodingProfile.  # noqa: E501
        :rtype: str
        """
        return self._manifest_subtitles

    @manifest_subtitles.setter
    def manifest_subtitles(self, manifest_subtitles):
        """Sets the manifest_subtitles of this DlnaTranscodingProfile.


        :param manifest_subtitles: The manifest_subtitles of this DlnaTranscodingProfile.  # noqa: E501
        :type: str
        """

        self._manifest_subtitles = manifest_subtitles

    @property
    def max_manifest_subtitles(self):
        """Gets the max_manifest_subtitles of this DlnaTranscodingProfile.  # noqa: E501


        :return: The max_manifest_subtitles of this DlnaTranscodingProfile.  # noqa: E501
        :rtype: int
        """
        return self._max_manifest_subtitles

    @max_manifest_subtitles.setter
    def max_manifest_subtitles(self, max_manifest_subtitles):
        """Sets the max_manifest_subtitles of this DlnaTranscodingProfile.


        :param max_manifest_subtitles: The max_manifest_subtitles of this DlnaTranscodingProfile.  # noqa: E501
        :type: int
        """

        self._max_manifest_subtitles = max_manifest_subtitles

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
        if issubclass(DlnaTranscodingProfile, dict):
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
        if not isinstance(other, DlnaTranscodingProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
