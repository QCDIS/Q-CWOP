# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CWLGit(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, url: str=None, branch: str=None, path: str=None):  # noqa: E501
        """CWLGit - a model defined in Swagger

        :param id: The id of this CWLGit.  # noqa: E501
        :type id: str
        :param url: The url of this CWLGit.  # noqa: E501
        :type url: str
        :param branch: The branch of this CWLGit.  # noqa: E501
        :type branch: str
        :param path: The path of this CWLGit.  # noqa: E501
        :type path: str
        """
        self.swagger_types = {
            'id': str,
            'url': str,
            'branch': str,
            'path': str
        }

        self.attribute_map = {
            'id': 'id',
            'url': 'url',
            'branch': 'branch',
            'path': 'path'
        }
        self._id = id
        self._url = url
        self._branch = branch
        self._path = path

    @classmethod
    def from_dict(cls, dikt) -> 'CWLGit':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CWLGit of this CWLGit.  # noqa: E501
        :rtype: CWLGit
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this CWLGit.


        :return: The id of this CWLGit.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this CWLGit.


        :param id: The id of this CWLGit.
        :type id: str
        """

        self._id = id

    @property
    def url(self) -> str:
        """Gets the url of this CWLGit.


        :return: The url of this CWLGit.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this CWLGit.


        :param url: The url of this CWLGit.
        :type url: str
        """

        self._url = url

    @property
    def branch(self) -> str:
        """Gets the branch of this CWLGit.


        :return: The branch of this CWLGit.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch: str):
        """Sets the branch of this CWLGit.


        :param branch: The branch of this CWLGit.
        :type branch: str
        """

        self._branch = branch

    @property
    def path(self) -> str:
        """Gets the path of this CWLGit.


        :return: The path of this CWLGit.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path: str):
        """Sets the path of this CWLGit.


        :param path: The path of this CWLGit.
        :type path: str
        """

        self._path = path