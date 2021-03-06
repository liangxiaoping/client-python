# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.0-beta.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class V1Event(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, count=None, first_timestamp=None, involved_object=None, last_timestamp=None, message=None, metadata=None, reason=None, source=None, type=None):
        """
        V1Event - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'count': 'int',
            'first_timestamp': 'UnversionedTime',
            'involved_object': 'V1ObjectReference',
            'last_timestamp': 'UnversionedTime',
            'message': 'str',
            'metadata': 'V1ObjectMeta',
            'reason': 'str',
            'source': 'V1EventSource',
            'type': 'str'
        }

        self.attribute_map = {
            'count': 'count',
            'first_timestamp': 'firstTimestamp',
            'involved_object': 'involvedObject',
            'last_timestamp': 'lastTimestamp',
            'message': 'message',
            'metadata': 'metadata',
            'reason': 'reason',
            'source': 'source',
            'type': 'type'
        }

        self._count = count
        self._first_timestamp = first_timestamp
        self._involved_object = involved_object
        self._last_timestamp = last_timestamp
        self._message = message
        self._metadata = metadata
        self._reason = reason
        self._source = source
        self._type = type


    @property
    def count(self):
        """
        Gets the count of this V1Event.
        The number of times this event has occurred.

        :return: The count of this V1Event.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this V1Event.
        The number of times this event has occurred.

        :param count: The count of this V1Event.
        :type: int
        """

        self._count = count

    @property
    def first_timestamp(self):
        """
        Gets the first_timestamp of this V1Event.
        The time at which the event was first recorded. (Time of server receipt is in TypeMeta.)

        :return: The first_timestamp of this V1Event.
        :rtype: UnversionedTime
        """
        return self._first_timestamp

    @first_timestamp.setter
    def first_timestamp(self, first_timestamp):
        """
        Sets the first_timestamp of this V1Event.
        The time at which the event was first recorded. (Time of server receipt is in TypeMeta.)

        :param first_timestamp: The first_timestamp of this V1Event.
        :type: UnversionedTime
        """

        self._first_timestamp = first_timestamp

    @property
    def involved_object(self):
        """
        Gets the involved_object of this V1Event.
        The object that this event is about.

        :return: The involved_object of this V1Event.
        :rtype: V1ObjectReference
        """
        return self._involved_object

    @involved_object.setter
    def involved_object(self, involved_object):
        """
        Sets the involved_object of this V1Event.
        The object that this event is about.

        :param involved_object: The involved_object of this V1Event.
        :type: V1ObjectReference
        """
        if involved_object is None:
            raise ValueError("Invalid value for `involved_object`, must not be `None`")

        self._involved_object = involved_object

    @property
    def last_timestamp(self):
        """
        Gets the last_timestamp of this V1Event.
        The time at which the most recent occurrence of this event was recorded.

        :return: The last_timestamp of this V1Event.
        :rtype: UnversionedTime
        """
        return self._last_timestamp

    @last_timestamp.setter
    def last_timestamp(self, last_timestamp):
        """
        Sets the last_timestamp of this V1Event.
        The time at which the most recent occurrence of this event was recorded.

        :param last_timestamp: The last_timestamp of this V1Event.
        :type: UnversionedTime
        """

        self._last_timestamp = last_timestamp

    @property
    def message(self):
        """
        Gets the message of this V1Event.
        A human-readable description of the status of this operation.

        :return: The message of this V1Event.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this V1Event.
        A human-readable description of the status of this operation.

        :param message: The message of this V1Event.
        :type: str
        """

        self._message = message

    @property
    def metadata(self):
        """
        Gets the metadata of this V1Event.
        Standard object's metadata. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata

        :return: The metadata of this V1Event.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1Event.
        Standard object's metadata. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata

        :param metadata: The metadata of this V1Event.
        :type: V1ObjectMeta
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")

        self._metadata = metadata

    @property
    def reason(self):
        """
        Gets the reason of this V1Event.
        This should be a short, machine understandable string that gives the reason for the transition into the object's current status.

        :return: The reason of this V1Event.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this V1Event.
        This should be a short, machine understandable string that gives the reason for the transition into the object's current status.

        :param reason: The reason of this V1Event.
        :type: str
        """

        self._reason = reason

    @property
    def source(self):
        """
        Gets the source of this V1Event.
        The component reporting this event. Should be a short machine understandable string.

        :return: The source of this V1Event.
        :rtype: V1EventSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this V1Event.
        The component reporting this event. Should be a short machine understandable string.

        :param source: The source of this V1Event.
        :type: V1EventSource
        """

        self._source = source

    @property
    def type(self):
        """
        Gets the type of this V1Event.
        Type of this event (Normal, Warning), new types could be added in the future

        :return: The type of this V1Event.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1Event.
        Type of this event (Normal, Warning), new types could be added in the future

        :param type: The type of this V1Event.
        :type: str
        """

        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
