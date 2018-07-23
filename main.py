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

import webapp2
import os
import jinja2
from models import UserProfile

#remember, you can get this by searching for jinja2 google app engine
jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_dir.get_template("templates/welcome.html")
        self.response.write(start_template.render())

    def post(self):
        firstNameInput = self.request.get('user-firstname')
        lastNameInput = self.request.get('user-lastname')
        userNameInput = self.request.get('user-username')
        emailInput = self.request.get('user-email')
        passwordInput = self.request.get('user-password')
        phoneInput = self.request.get('user-phone')
        genderInput = self.request.get('user-gender')
        twitterHandleInput = self.request.get('user-twitterHandle')
        facebookHandleInput = self.request.get('user-facebookHandle')
        linkedinHandleInput = self.request.get('user-linkedinHandle')


        #put into database (optional)
        userProfileUpdate = UserProfile(
        firstName = firstNameInput,
        lastName = lastNameInput,
        userName = userNameInput,
        email = emailInput,
        password = passwordInput,
        phone = phoneInput,
        gender = genderInput,
        twitterHandle = twitterHandleInput,
        facebookHandle = facebookHandleInput,
        linkedinHandle = linkedinHandleInput
        )
        userProfileUpdate.put()

        #pass to the template via a dictionary
        variable_dict = {
        firstName: 'fistName',
        lastName: 'lastName',
        userName: 'username',
        email: 'email',
        password: 'password',
        phone: 'phone',
        gender: 'gender',
        twitterHandle: 'twitterHandle',
        facebookHandle: 'facebookHandle',
        linkedinHandle: 'linkedinHandle'}
        end_template = jinja_current_dir.get_template("templates/results.html")
        self.response.write(end_template.render(variable_dict))

class ShowUserHandler(webapp2.RequestHandler):
    def get(self):
        results_template = jinja_current_dir.get_template("templates/results.html")
        userShow = UserProfile.query().order(-UserProfile.userName).fetch()
        dict_for_template = {'variable_dict': userName}
        self.response.write(results_template.render(dict_for_template))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/showfavs', ShowUserHandler)
], debug=True)
