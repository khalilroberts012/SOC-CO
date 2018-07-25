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
import userProfileModel
from userProfileModel import UserProfile


#remember, you can get this by searching for jinja2 google app engine
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


##BASIC MAIN HANDLER, WILL CHANGE TO HOMEPAGE
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("This is the homepage.")


##CREATE A NEW ACCOUNT
class CreateAccountLoginHandler(webapp2.RequestHandler):
    def get(self):
        createAnAccountTemplate = jinja_env.get_template("templates/welcome.html")
        self.response.write(createAnAccountTemplate.render())

        #collecting HTML input in the account creation process to input in Data Store
    def post(self):
        userProfile = userProfileModel.UserProfile()

        userAccountCheckQuery = UserProfile.query().filter(UserProfile.email == self.request.get('userLogin-email'))
        userProfile = userAccountCheckQuery.get()

    class SignInHandler(webapp2.RequestHandler):
        def get (self):
            signinTemplates = jinja_env.get_template("templates/signIn.html")
            html = self.response.write(signInTemplates.render())



        #if str(userProfile)=="None":
        #     self.response.write("Sorry. An account with this email on file does not exist.")
        # else:
        #     if UserProfile.password == self.request.get('userLogin-password')):
        #
        #
        #
        # query = UserProfile.query().filter(UserProfile.email == self.request.get('userLogin-email')
        # if()
        #     if(UserProfile.query().filter(UserProfile.password == self.request.get('userLogin-password')))
        #
        # userProfile.firstName = self.request.get('user-firstname')
        # userProfile.lastName = self.request.get('user-lastname')
        # userProfile.userName = self.request.get('user-username')
        # userProfile.email = self.request.get('user-email')
        # userProfile.password = self.request.get('user-password')
        # userProfile.phone = self.request.get('user-phone')
        # userProfile.gender = self.request.get('user-gender')
        # userProfile.twitterHandle = "https://twitter.com/" + str(self.request.get('user-twitterHandle'))
        # userProfile.facebookHandle = "https://facebook.com/" + str(self.request.get('user-facebookHandle'))
        # userProfile.linkedinHandle = "https://www.linkedin.com/in/" + str(self.request.get('user-linkedinHandle'))
        #
        # displayUserProfileTemplate = jinja_env.get_template("templates/results.html")
        #
        # html = displayUserProfileTemplate.render({
        #     'firstName': userProfile.firstName,
        #     'lastName': userProfile.lastName,
        #     'userName': userProfile.userName,
        #     'email': userProfile.email,
        #     'password': userProfile.password,
        #     'phone': userProfile.phone,
        #     'gender': userProfile.gender,
        #     'twitterHandle': userProfile.twitterHandle,
        #     'facebookHandle': userProfile.facebookHandle,
        #     'linkedinHandle': userProfile.linkedinHandle
        # })

        self.response.write(html)
        #userProfile.put()


##FIND AND DISPLAY A USER ACCOUNT
class ShowUserHandler(webapp2.RequestHandler):
    def get(self, userName):

         userProfile = userProfileModel.UserProfile()
         userNameQuery = UserProfile.query().filter(UserProfile.userName == userName)
         userProfile = userNameQuery.get()

         #if the userName is not found in the query
         if str(userProfile)=="None":
             self.response.write("Sorry we couldn't find a profile with the username " + userName + ". Please try again.")

         #if the userName is found in the query
         else:
            displayUserProfileTemplate = jinja_env.get_template("templates/results.html")
            html = displayUserProfileTemplate.render({
                'firstName': userProfile.firstName,
                'lastName': userProfile.lastName,
                'userName': userProfile.userName,
                'email': userProfile.email,
                'password': userProfile.password,
                'phone': userProfile.phone,
                'twitterHandle': userProfile.twitterHandle,
                'facebookHandle': userProfile.facebookHandle,
                'linkedinHandle': userProfile.linkedinHandle})
            self.response.write(html)

app = webapp2.WSGIApplication([
    (r'/', MainHandler),
    (r'/createaccount', CreateAccount&LoginHandler),
    (r'/user/(\w+)', ShowUserHandler),
    (r'/signin', SignInHandler),
], debug=True)
