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


class V1alpha1InfoResponse(object):
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
        'links': 'list[V1alpha1Link]',
        'managed_namespace': 'str'
    }

    attribute_map = {
        'links': 'links',
        'managed_namespace': 'managedNamespace'
    }

    def __init__(self, links=None, managed_namespace=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1InfoResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._links = None
        self._managed_namespace = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if managed_namespace is not None:
            self.managed_namespace = managed_namespace

    @property
    def links(self):
        """Gets the links of this V1alpha1InfoResponse.  # noqa: E501


        :return: The links of this V1alpha1InfoResponse.  # noqa: E501
        :rtype: list[V1alpha1Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this V1alpha1InfoResponse.


        :param links: The links of this V1alpha1InfoResponse.  # noqa: E501
        :type links: list[V1alpha1Link]
        """

        self._links = links

    @property
    def managed_namespace(self):
        """Gets the managed_namespace of this V1alpha1InfoResponse.  # noqa: E501


        :return: The managed_namespace of this V1alpha1InfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._managed_namespace

    @managed_namespace.setter
    def managed_namespace(self, managed_namespace):
        """Sets the managed_namespace of this V1alpha1InfoResponse.


        :param managed_namespace: The managed_namespace of this V1alpha1InfoResponse.  # noqa: E501
        :type managed_namespace: str
        """

        self._managed_namespace = managed_namespace

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
        if not isinstance(other, V1alpha1InfoResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1InfoResponse):
            return True

        return self.to_dict() != other.to_dict()
