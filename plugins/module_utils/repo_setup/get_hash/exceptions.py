#   Copyright 2021 Red Hat, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#
#
from __future__ import absolute_import, division, print_function


__metaclass__ = type


class Base(Exception):
    """Base Exception"""


class HashMissingConfig(Base):
    """Missing configuration file for HashInfo. This is thrown
    when there is no config.yaml in constants.CONFIG_PATH or the local
    directory assuming execution from a source checkout.
    """

    def __init__(self, error_msg):
        super(HashMissingConfig, self).__init__(error_msg)


class HashInvalidConfig(Base):
    """Invalid configuration file for HashInfo. This is used when
    any of they keys in constants.CONFIG_KEYS is not found in config.yaml.
    """

    def __init__(self, error_msg):
        super(HashInvalidConfig, self).__init__(error_msg)


class HashInvalidParameter(Base):
    """Invalid parameters passed for HashInfo. This is thrown when
    the user passed invalid combination ofparameters parameters to the cli
    entrypoint, for example specifying --component with centos7.
    """

    def __init__(self, error_msg):
        super(HashInvalidParameter, self).__init__(error_msg)


class HashInvalidDLRNResponse(Base):
    """Invalid response received from the DLRN server.  This is seen if
    the delorean server replies with a status code other than 200 OK for
    a query to commit.yaml or delorean.repo.md5.
    """

    def __init__(self, error_msg):
        super(HashInvalidDLRNResponse, self).__init__(error_msg)
