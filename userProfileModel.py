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
    email = ndb.StringProperty(required=False)
    password = ndb.StringProperty(required=False)
    phone = ndb.StringProperty(required=False)
    twitterHandle = ndb.StringProperty(required=False)
    facebookHandle = ndb.StringProperty(required=False)
    linkedinHandle = ndb.StringProperty(required=False)
    snapchatHandle = ndb.StringProperty(required=False)
    instagramHandle = ndb.StringProperty(required=False)
    profilePicture = ndb.BlobProperty(required=False)
