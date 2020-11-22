# coding: utf-8

"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    The version of the OpenAPI document: 2.11.8
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argo.workflows.client.configuration import Configuration


class V1alpha1Artifact(object):
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
        'archive': 'V1alpha1ArchiveStrategy',
        'archive_logs': 'bool',
        'artifactory': 'V1alpha1ArtifactoryArtifact',
        '_from': 'str',
        'gcs': 'V1alpha1GCSArtifact',
        'git': 'V1alpha1GitArtifact',
        'global_name': 'str',
        'hdfs': 'V1alpha1HDFSArtifact',
        'http': 'V1alpha1HTTPArtifact',
        'mode': 'int',
        'name': 'str',
        'optional': 'bool',
        'oss': 'V1alpha1OSSArtifact',
        'path': 'str',
        'raw': 'V1alpha1RawArtifact',
        's3': 'V1alpha1S3Artifact',
        'sub_path': 'str'
    }

    attribute_map = {
        'archive': 'archive',
        'archive_logs': 'archiveLogs',
        'artifactory': 'artifactory',
        '_from': 'from',
        'gcs': 'gcs',
        'git': 'git',
        'global_name': 'globalName',
        'hdfs': 'hdfs',
        'http': 'http',
        'mode': 'mode',
        'name': 'name',
        'optional': 'optional',
        'oss': 'oss',
        'path': 'path',
        'raw': 'raw',
        's3': 's3',
        'sub_path': 'subPath'
    }

    def __init__(self, archive=None, archive_logs=None, artifactory=None, _from=None, gcs=None, git=None, global_name=None, hdfs=None, http=None, mode=None, name=None, optional=None, oss=None, path=None, raw=None, s3=None, sub_path=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1Artifact - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._archive = None
        self._archive_logs = None
        self._artifactory = None
        self.__from = None
        self._gcs = None
        self._git = None
        self._global_name = None
        self._hdfs = None
        self._http = None
        self._mode = None
        self._name = None
        self._optional = None
        self._oss = None
        self._path = None
        self._raw = None
        self._s3 = None
        self._sub_path = None
        self.discriminator = None

        if archive is not None:
            self.archive = archive
        if archive_logs is not None:
            self.archive_logs = archive_logs
        if artifactory is not None:
            self.artifactory = artifactory
        if _from is not None:
            self._from = _from
        if gcs is not None:
            self.gcs = gcs
        if git is not None:
            self.git = git
        if global_name is not None:
            self.global_name = global_name
        if hdfs is not None:
            self.hdfs = hdfs
        if http is not None:
            self.http = http
        if mode is not None:
            self.mode = mode
        self.name = name
        if optional is not None:
            self.optional = optional
        if oss is not None:
            self.oss = oss
        if path is not None:
            self.path = path
        if raw is not None:
            self.raw = raw
        if s3 is not None:
            self.s3 = s3
        if sub_path is not None:
            self.sub_path = sub_path

    @property
    def archive(self):
        """Gets the archive of this V1alpha1Artifact.  # noqa: E501


        :return: The archive of this V1alpha1Artifact.  # noqa: E501
        :rtype: V1alpha1ArchiveStrategy
        """
        return self._archive

    @archive.setter
    def archive(self, archive):
        """Sets the archive of this V1alpha1Artifact.


        :param archive: The archive of this V1alpha1Artifact.  # noqa: E501
        :type: V1alpha1ArchiveStrategy
        """

        self._archive = archive

    @property
    def archive_logs(self):
        """Gets the archive_logs of this V1alpha1Artifact.  # noqa: E501

        ArchiveLogs indicates if the container logs should be archived  # noqa: E501

        :return: The archive_logs of this V1alpha1Artifact.  # noqa: E501
        :rtype: bool
        """
        return self._archive_logs

    @archive_logs.setter
    def archive_logs(self, archive_logs):
        """Sets the archive_logs of this V1alpha1Artifact.

        ArchiveLogs indicates if the container logs should be archived  # noqa: E501

        :param archive_logs: The archive_logs of this V1alpha1Artifact.  # noqa: E501
        :type: bool
        """

        self._archive_logs = archive_logs

    @property
    def artifactory(self):
        """Gets the artifactory of this V1alpha1Artifact.  # noqa: E501


        :return: The artifactory of this V1alpha1Artifact.  # noqa: E501
        :rtype: V1alpha1ArtifactoryArtifact
        """
        return self._artifactory

    @artifactory.setter
    def artifactory(self, artifactory):
        """Sets the artifactory of this V1alpha1Artifact.


        :param artifactory: The artifactory of this V1alpha1Artifact.  # noqa: E501
        :type: V1alpha1ArtifactoryArtifact
        """

        self._artifactory = artifactory

    @property
    def _from(self):
        """Gets the _from of this V1alpha1Artifact.  # noqa: E501

        From allows an artifact to reference an artifact from a previous step  # noqa: E501

        :return: The _from of this V1alpha1Artifact.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this V1alpha1Artifact.

        From allows an artifact to reference an artifact from a previous step  # noqa: E501

        :param _from: The _from of this V1alpha1Artifact.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def gcs(self):
        """Gets the gcs of this V1alpha1Artifact.  # noqa: E501


        :return: The gcs of this V1alpha1Artifact.  # noqa: E501
        :rtype: V1alpha1GCSArtifact
        """
        return self._gcs

    @gcs.setter
    def gcs(self, gcs):
        """Sets the gcs of this V1alpha1Artifact.


        :param gcs: The gcs of this V1alpha1Artifact.  # noqa: E501
        :type: V1alpha1GCSArtifact
        """

        self._gcs = gcs

    @property
    def git(self):
        """Gets the git of this V1alpha1Artifact.  # noqa: E501


        :return: The git of this V1alpha1Artifact.  # noqa: E501
        :rtype: V1alpha1GitArtifact
        """
        return self._git

    @git.setter
    def git(self, git):
        """Sets the git of this V1alpha1Artifact.


        :param git: The git of this V1alpha1Artifact.  # noqa: E501
        :type: V1alpha1GitArtifact
        """

        self._git = git

    @property
    def global_name(self):
        """Gets the global_name of this V1alpha1Artifact.  # noqa: E501

        GlobalName exports an output artifact to the global scope, making it available as '{{io.argoproj.workflow.v1alpha1.outputs.artifacts.XXXX}} and in workflow.status.outputs.artifacts  # noqa: E501

        :return: The global_name of this V1alpha1Artifact.  # noqa: E501
        :rtype: str
        """
        return self._global_name

    @global_name.setter
    def global_name(self, global_name):
        """Sets the global_name of this V1alpha1Artifact.

        GlobalName exports an output artifact to the global scope, making it available as '{{io.argoproj.workflow.v1alpha1.outputs.artifacts.XXXX}} and in workflow.status.outputs.artifacts  # noqa: E501

        :param global_name: The global_name of this V1alpha1Artifact.  # noqa: E501
        :type: str
        """

        self._global_name = global_name

    @property
    def hdfs(self):
        """Gets the hdfs of this V1alpha1Artifact.  # noqa: E501


        :return: The hdfs of this V1alpha1Artifact.  # noqa: E501
        :rtype: V1alpha1HDFSArtifact
        """
        return self._hdfs

    @hdfs.setter
    def hdfs(self, hdfs):
        """Sets the hdfs of this V1alpha1Artifact.


        :param hdfs: The hdfs of this V1alpha1Artifact.  # noqa: E501
        :type: V1alpha1HDFSArtifact
        """

        self._hdfs = hdfs

    @property
    def http(self):
        """Gets the http of this V1alpha1Artifact.  # noqa: E501


        :return: The http of this V1alpha1Artifact.  # noqa: E501
        :rtype: V1alpha1HTTPArtifact
        """
        return self._http

    @http.setter
    def http(self, http):
        """Sets the http of this V1alpha1Artifact.


        :param http: The http of this V1alpha1Artifact.  # noqa: E501
        :type: V1alpha1HTTPArtifact
        """

        self._http = http

    @property
    def mode(self):
        """Gets the mode of this V1alpha1Artifact.  # noqa: E501

        mode bits to use on this file, must be a value between 0 and 0777 set when loading input artifacts.  # noqa: E501

        :return: The mode of this V1alpha1Artifact.  # noqa: E501
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this V1alpha1Artifact.

        mode bits to use on this file, must be a value between 0 and 0777 set when loading input artifacts.  # noqa: E501

        :param mode: The mode of this V1alpha1Artifact.  # noqa: E501
        :type: int
        """

        self._mode = mode

    @property
    def name(self):
        """Gets the name of this V1alpha1Artifact.  # noqa: E501

        name of the artifact. must be unique within a template's inputs/outputs.  # noqa: E501

        :return: The name of this V1alpha1Artifact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha1Artifact.

        name of the artifact. must be unique within a template's inputs/outputs.  # noqa: E501

        :param name: The name of this V1alpha1Artifact.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def optional(self):
        """Gets the optional of this V1alpha1Artifact.  # noqa: E501

        Make Artifacts optional, if Artifacts doesn't generate or exist  # noqa: E501

        :return: The optional of this V1alpha1Artifact.  # noqa: E501
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """Sets the optional of this V1alpha1Artifact.

        Make Artifacts optional, if Artifacts doesn't generate or exist  # noqa: E501

        :param optional: The optional of this V1alpha1Artifact.  # noqa: E501
        :type: bool
        """

        self._optional = optional

    @property
    def oss(self):
        """Gets the oss of this V1alpha1Artifact.  # noqa: E501


        :return: The oss of this V1alpha1Artifact.  # noqa: E501
        :rtype: V1alpha1OSSArtifact
        """
        return self._oss

    @oss.setter
    def oss(self, oss):
        """Sets the oss of this V1alpha1Artifact.


        :param oss: The oss of this V1alpha1Artifact.  # noqa: E501
        :type: V1alpha1OSSArtifact
        """

        self._oss = oss

    @property
    def path(self):
        """Gets the path of this V1alpha1Artifact.  # noqa: E501

        Path is the container path to the artifact  # noqa: E501

        :return: The path of this V1alpha1Artifact.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this V1alpha1Artifact.

        Path is the container path to the artifact  # noqa: E501

        :param path: The path of this V1alpha1Artifact.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def raw(self):
        """Gets the raw of this V1alpha1Artifact.  # noqa: E501


        :return: The raw of this V1alpha1Artifact.  # noqa: E501
        :rtype: V1alpha1RawArtifact
        """
        return self._raw

    @raw.setter
    def raw(self, raw):
        """Sets the raw of this V1alpha1Artifact.


        :param raw: The raw of this V1alpha1Artifact.  # noqa: E501
        :type: V1alpha1RawArtifact
        """

        self._raw = raw

    @property
    def s3(self):
        """Gets the s3 of this V1alpha1Artifact.  # noqa: E501


        :return: The s3 of this V1alpha1Artifact.  # noqa: E501
        :rtype: V1alpha1S3Artifact
        """
        return self._s3

    @s3.setter
    def s3(self, s3):
        """Sets the s3 of this V1alpha1Artifact.


        :param s3: The s3 of this V1alpha1Artifact.  # noqa: E501
        :type: V1alpha1S3Artifact
        """

        self._s3 = s3

    @property
    def sub_path(self):
        """Gets the sub_path of this V1alpha1Artifact.  # noqa: E501

        SubPath allows an artifact to be sourced from a subpath within the specified source  # noqa: E501

        :return: The sub_path of this V1alpha1Artifact.  # noqa: E501
        :rtype: str
        """
        return self._sub_path

    @sub_path.setter
    def sub_path(self, sub_path):
        """Sets the sub_path of this V1alpha1Artifact.

        SubPath allows an artifact to be sourced from a subpath within the specified source  # noqa: E501

        :param sub_path: The sub_path of this V1alpha1Artifact.  # noqa: E501
        :type: str
        """

        self._sub_path = sub_path

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
        if not isinstance(other, V1alpha1Artifact):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1Artifact):
            return True

        return self.to_dict() != other.to_dict()
