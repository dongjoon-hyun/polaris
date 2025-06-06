#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

# coding: utf-8

"""
    Polaris Management Service

    Defines the management APIs for using Polaris to create and manage Iceberg catalogs and their principals

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from polaris.management.models.grant_principal_role_request import GrantPrincipalRoleRequest

class TestGrantPrincipalRoleRequest(unittest.TestCase):
    """GrantPrincipalRoleRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GrantPrincipalRoleRequest:
        """Test GrantPrincipalRoleRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GrantPrincipalRoleRequest`
        """
        model = GrantPrincipalRoleRequest()
        if include_optional:
            return GrantPrincipalRoleRequest(
                principal_role = polaris.management.models.principal_role.PrincipalRole(
                    name = 'k&*h<4<U/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:Ts\";mGL,i&z5[P@M\"lzfB+Y,Twzfu~N^z\"mfqecVU0', 
                    federated = True, 
                    properties = {
                        'key' : ''
                        }, 
                    create_timestamp = 56, 
                    last_update_timestamp = 56, 
                    entity_version = 56, )
            )
        else:
            return GrantPrincipalRoleRequest(
        )
        """

    def testGrantPrincipalRoleRequest(self):
        """Test GrantPrincipalRoleRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
