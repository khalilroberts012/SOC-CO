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
from google.appengine.api import users
from google.appengine.api import images
from google.appengine.ext import ndb


#remember, you can get this by searching for jinja2 google app engine
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

##BASIC MAIN HANDLER, WILL CHANGE TO HOMEPAGE
class HomepageLoginHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        # If the user is logged in...
        if user:
            email_address = user.nickname()
            existingUser = UserProfile.get_by_id(user.user_id())

            #If the user has previously been to our site, we greet them
            if existingUser:
                editUserProfileTemplate = jinja_env.get_template("templates/results.html")
                html = editUserProfileTemplate.render({
                    'firstName': userProfile.firstName,
                    'lastName': userProfile.lastName,
                    'userName': userProfile.userName,
                    'email': userProfile.email,
                    'password': userProfile.password,
                    'phone': userProfile.phone,
                    'gender': userProfile.gender,
                    'twitterHandle': userProfile.twitterHandle,
                    'facebookHandle': userProfile.facebookHandle,
                    'linkedinHandle': userProfile.linkedinHandle,
                    'profilePicture': userProfile.profilePicture,
                    'signOut': users.create_logout_url('/')
                })
                self.response.write(html)

            #If the user hasn't been to our site, we ask them to sign up
            else:
                ###NEED CREATE ACCOUNT TEMPLATE AND NAME
                createAccountTemplate = jinja_env.get_template("/templates/welcome.html")
                self.response.write(createAccountTemplate.render({
                'signOut': str(users.create_logout_url('/'))
                }))

        #Otherwise, the user isn't logged in
        else:
            homepageLoginTemplate = jinja_env.get_template("/templates/signIn.html")
            self.response.write(homepageLoginTemplate.render({
            'signIn': users.create_login_url('/')
            }))

    def post(self):
        user = users.get_current_user()
        userProfile = userProfileModel.UserProfile()

        if not user:
            self.error(500)
            return

        userProfile.user_id = user.user_id()
        userProfile.firstName = self.request.get('user-firstname')
        userProfile.lastName = self.request.get('user-lastname')
        userProfile.userName = self.request.get('user-username')
        userProfile.email = self.request.get('user-email')
        userProfile.password = self.request.get('user-password')
        userProfile.phone = self.request.get('user-phone')
        userProfile.gender = self.request.get('user-gender')
        userProfile.profilePicture = (str(self.request.get('image')))
        userProfile.twitterHandle = "https://twitter.com/" + str(self.request.get('twitterInput'))
        userProfile.facebookHandle = "https://facebook.com/" + str(self.request.get('facebookInput'))
        userProfile.linkedinHandle = "https://www.linkedin.com/in/" + str(self.request.get('linkedinInput'))
        userProfile.put()


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
            'linkedinHandle': userProfile.linkedinHandle,
            'profilePicture': str("/img?id=" + str(userProfile.key.urlsafe()))
        })

        self.response.write(html)

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
            displayUserProfileTemplate = jinja_env.get_template("templates/profile.html")
            html = displayUserProfileTemplate.render({
                'firstName': userProfile.firstName,
                'lastName': userProfile.lastName,
                'userName': userProfile.userName,
                'email': userProfile.email,
                'password': userProfile.password,
                'phone': userProfile.phone,
                'twitterHandle': userProfile.twitterHandle,
                'facebookHandle': userProfile.facebookHandle,
                'linkedinHandle': userProfile.linkedinHandle
                'profilePicture': "/img?id=" + str(userProfile.key.urlsafe()),
                })
            self.response.write(html)

##UPLOADING AN IMAGE
class Image(webapp2.RequestHandler):
    def get(self):
        key = ndb.Key(urlsafe=self.request.get('id'))
        data = key.get()

        if data.profilePicture:
            self.response.headers['Content-Type'] = 'image/jpg'
            self.response.out.write(data.profilePicture)
        else:
            self.response.out.write('No image')


app = webapp2.WSGIApplication([
    (r'/', HomepageLoginHandler),
    (r'/img', Image),
    (r'/(\w+)', ShowUserHandler),
], debug=True)
