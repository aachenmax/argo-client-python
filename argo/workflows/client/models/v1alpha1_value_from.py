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


class V1alpha1ValueFrom(object):
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
        'default': 'str',
        'jq_filter': 'str',
        'json_path': 'str',
        'parameter': 'str',
        'path': 'str'
    }

    attribute_map = {
        'default': 'default',
        'jq_filter': 'jqFilter',
        'json_path': 'jsonPath',
        'parameter': 'parameter',
        'path': 'path'
    }

    def __init__(self, default=None, jq_filter=None, json_path=None, parameter=None, path=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1ValueFrom - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._default = None
        self._jq_filter = None
        self._json_path = None
        self._parameter = None
        self._path = None
        self.discriminator = None

        if default is not None:
            self.default = default
        if jq_filter is not None:
            self.jq_filter = jq_filter
        if json_path is not None:
            self.json_path = json_path
        if parameter is not None:
            self.parameter = parameter
        if path is not None:
            self.path = path

    @property
    def default(self):
        """Gets the default of this V1alpha1ValueFrom.  # noqa: E501

        Default specifies a value to be used if retrieving the value from the specified source fails  # noqa: E501

        :return: The default of this V1alpha1ValueFrom.  # noqa: E501
        :rtype: str
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this V1alpha1ValueFrom.

        Default specifies a value to be used if retrieving the value from the specified source fails  # noqa: E501

        :param default: The default of this V1alpha1ValueFrom.  # noqa: E501
        :type default: str
        """

        self._default = default

    @property
    def jq_filter(self):
        """Gets the jq_filter of this V1alpha1ValueFrom.  # noqa: E501

        JQFilter expression against the resource object in resource templates  # noqa: E501

        :return: The jq_filter of this V1alpha1ValueFrom.  # noqa: E501
        :rtype: str
        """
        return self._jq_filter

    @jq_filter.setter
    def jq_filter(self, jq_filter):
        """Sets the jq_filter of this V1alpha1ValueFrom.

        JQFilter expression against the resource object in resource templates  # noqa: E501

        :param jq_filter: The jq_filter of this V1alpha1ValueFrom.  # noqa: E501
        :type jq_filter: str
        """

        self._jq_filter = jq_filter

    @property
    def json_path(self):
        """Gets the json_path of this V1alpha1ValueFrom.  # noqa: E501

        JSONPath of a resource to retrieve an output parameter value from in resource templates  # noqa: E501

        :return: The json_path of this V1alpha1ValueFrom.  # noqa: E501
        :rtype: str
        """
        return self._json_path

    @json_path.setter
    def json_path(self, json_path):
        """Sets the json_path of this V1alpha1ValueFrom.

        JSONPath of a resource to retrieve an output parameter value from in resource templates  # noqa: E501

        :param json_path: The json_path of this V1alpha1ValueFrom.  # noqa: E501
        :type json_path: str
        """

        self._json_path = json_path

    @property
    def parameter(self):
        """Gets the parameter of this V1alpha1ValueFrom.  # noqa: E501

        Parameter reference to a step or dag task in which to retrieve an output parameter value from (e.g. '{{steps.mystep.outputs.myparam}}')  # noqa: E501

        :return: The parameter of this V1alpha1ValueFrom.  # noqa: E501
        :rtype: str
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        """Sets the parameter of this V1alpha1ValueFrom.

        Parameter reference to a step or dag task in which to retrieve an output parameter value from (e.g. '{{steps.mystep.outputs.myparam}}')  # noqa: E501

        :param parameter: The parameter of this V1alpha1ValueFrom.  # noqa: E501
        :type parameter: str
        """

        self._parameter = parameter

    @property
    def path(self):
        """Gets the path of this V1alpha1ValueFrom.  # noqa: E501

        Path in the container to retrieve an output parameter value from in container templates  # noqa: E501

        :return: The path of this V1alpha1ValueFrom.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this V1alpha1ValueFrom.

        Path in the container to retrieve an output parameter value from in container templates  # noqa: E501

        :param path: The path of this V1alpha1ValueFrom.  # noqa: E501
        :type path: str
        """

        self._path = path

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
        if not isinstance(other, V1alpha1ValueFrom):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ValueFrom):
            return True

        return self.to_dict() != other.to_dict()
