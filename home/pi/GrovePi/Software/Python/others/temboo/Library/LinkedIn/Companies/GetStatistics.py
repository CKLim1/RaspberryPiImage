# -*- coding: utf-8 -*-

###############################################################################
#
# GetStatistics
# Returns general statistics for a company.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetStatistics(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetStatistics Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetStatistics, self).__init__(temboo_session, '/Library/LinkedIn/Companies/GetStatistics')


    def new_input_set(self):
        return GetStatisticsInputSet()

    def _make_result_set(self, result, path):
        return GetStatisticsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetStatisticsChoreographyExecution(session, exec_id, path)

class GetStatisticsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetStatistics
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by LinkedIn (AKA the Client ID).)
        """
        super(GetStatisticsInputSet, self)._set_input('APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process (AKA the OAuth User Secret).)
        """
        super(GetStatisticsInputSet, self)._set_input('AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process (AKA the OAuth User Token).)
        """
        super(GetStatisticsInputSet, self)._set_input('AccessToken', value)
    def set_CompanyID(self, value):
        """
        Set the value of the CompanyID input for this Choreo. ((required, integer) A LinkedIn assigned ID associated with the company.)
        """
        super(GetStatisticsInputSet, self)._set_input('CompanyID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml (the default) and json.)
        """
        super(GetStatisticsInputSet, self)._set_input('ResponseFormat', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by LinkedIn (AKA the Client Secret).)
        """
        super(GetStatisticsInputSet, self)._set_input('SecretKey', value)

class GetStatisticsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetStatistics Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LinkedIn.)
        """
        return self._output.get('Response', None)

class GetStatisticsChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetStatisticsResultSet(response, path)
