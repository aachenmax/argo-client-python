# coding: utf-8

"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    The version of the OpenAPI document: 2.10.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argo.workflows.client.configuration import Configuration


class V1alpha1Gauge(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'realtime': 'bool',
        'value': 'str'
    }

    attribute_map = {
        'realtime': 'realtime',
        'value': 'value'
    }

    def __init__(self, realtime=None, value=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1Gauge - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._realtime = None
        self._value = None
        self.discriminator = None

        self.realtime = realtime
        self.value = value

    @property
    def realtime(self):
        """Gets the realtime of this V1alpha1Gauge.  # noqa: E501

        Realtime emits this metric in real time if applicable  # noqa: E501

        :return: The realtime of this V1alpha1Gauge.  # noqa: E501
        :rtype: bool
        """
        return self._realtime

    @realtime.setter
    def realtime(self, realtime):
        """Sets the realtime of this V1alpha1Gauge.

        Realtime emits this metric in real time if applicable  # noqa: E501

        :param realtime: The realtime of this V1alpha1Gauge.  # noqa: E501
        :type realtime: bool
        """
        if self.local_vars_configuration.client_side_validation and realtime is None:  # noqa: E501
            raise ValueError("Invalid value for `realtime`, must not be `None`")  # noqa: E501

        self._realtime = realtime

    @property
    def value(self):
        """Gets the value of this V1alpha1Gauge.  # noqa: E501

        Value is the value of the metric  # noqa: E501

        :return: The value of this V1alpha1Gauge.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this V1alpha1Gauge.

        Value is the value of the metric  # noqa: E501

        :param value: The value of this V1alpha1Gauge.  # noqa: E501
        :type value: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha1Gauge):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1Gauge):
            return True

        return self.to_dict() != other.to_dict()
