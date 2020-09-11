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


class V1ListMeta(object):
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
        '_continue': 'str',
        'remaining_item_count': 'int',
        'resource_version': 'str',
        'self_link': 'str'
    }

    attribute_map = {
        '_continue': 'continue',
        'remaining_item_count': 'remainingItemCount',
        'resource_version': 'resourceVersion',
        'self_link': 'selfLink'
    }

    def __init__(self, _continue=None, remaining_item_count=None, resource_version=None, self_link=None, local_vars_configuration=None):  # noqa: E501
        """V1ListMeta - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self.__continue = None
        self._remaining_item_count = None
        self._resource_version = None
        self._self_link = None
        self.discriminator = None

        if _continue is not None:
            self._continue = _continue
        if remaining_item_count is not None:
            self.remaining_item_count = remaining_item_count
        if resource_version is not None:
            self.resource_version = resource_version
        if self_link is not None:
            self.self_link = self_link

    @property
    def _continue(self):
        """Gets the _continue of this V1ListMeta.  # noqa: E501

        continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message.  # noqa: E501

        :return: The _continue of this V1ListMeta.  # noqa: E501
        :rtype: str
        """
        return self.__continue

    @_continue.setter
    def _continue(self, _continue):
        """Sets the _continue of this V1ListMeta.

        continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message.  # noqa: E501

        :param _continue: The _continue of this V1ListMeta.  # noqa: E501
        :type _continue: str
        """

        self.__continue = _continue

    @property
    def remaining_item_count(self):
        """Gets the remaining_item_count of this V1ListMeta.  # noqa: E501

        remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is *estimating* the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact.  This field is alpha and can be changed or removed without notice.  # noqa: E501

        :return: The remaining_item_count of this V1ListMeta.  # noqa: E501
        :rtype: int
        """
        return self._remaining_item_count

    @remaining_item_count.setter
    def remaining_item_count(self, remaining_item_count):
        """Sets the remaining_item_count of this V1ListMeta.

        remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is *estimating* the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact.  This field is alpha and can be changed or removed without notice.  # noqa: E501

        :param remaining_item_count: The remaining_item_count of this V1ListMeta.  # noqa: E501
        :type remaining_item_count: int
        """

        self._remaining_item_count = remaining_item_count

    @property
    def resource_version(self):
        """Gets the resource_version of this V1ListMeta.  # noqa: E501

        String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency  # noqa: E501

        :return: The resource_version of this V1ListMeta.  # noqa: E501
        :rtype: str
        """
        return self._resource_version

    @resource_version.setter
    def resource_version(self, resource_version):
        """Sets the resource_version of this V1ListMeta.

        String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#concurrency-control-and-consistency  # noqa: E501

        :param resource_version: The resource_version of this V1ListMeta.  # noqa: E501
        :type resource_version: str
        """

        self._resource_version = resource_version

    @property
    def self_link(self):
        """Gets the self_link of this V1ListMeta.  # noqa: E501

        selfLink is a URL representing this object. Populated by the system. Read-only.  # noqa: E501

        :return: The self_link of this V1ListMeta.  # noqa: E501
        :rtype: str
        """
        return self._self_link

    @self_link.setter
    def self_link(self, self_link):
        """Sets the self_link of this V1ListMeta.

        selfLink is a URL representing this object. Populated by the system. Read-only.  # noqa: E501

        :param self_link: The self_link of this V1ListMeta.  # noqa: E501
        :type self_link: str
        """

        self._self_link = self_link

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
        if not isinstance(other, V1ListMeta):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ListMeta):
            return True

        return self.to_dict() != other.to_dict()
