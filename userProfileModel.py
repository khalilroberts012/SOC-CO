#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.appengine.ext import ndb

class UserProfile(ndb.Model):
    firstName = ndb.StringProperty(required=True)
    lastName = ndb.StringProperty(required=True)
    userName = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    image = ndb.BlobProperty(required=False)
    # phone = ndb.StringProperty(required=True)
    # twitterHandle = ndb.StringProperty(required=True)
    # facebookHandle = ndb.StringProperty(required=True)
    # linkedinHandle = ndb.StringProperty(required=True)
