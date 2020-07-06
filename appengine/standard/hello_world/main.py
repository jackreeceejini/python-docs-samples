# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
from validation import valid_day, valid_month, valid_year

form = """<form method="post" action="/testform">
<label> <h3> What is your birthday</h3> </label>
<br>
    <label> Day
        <input type="text" name="day">
    </label>
    <label> Month
        <input type="text" name="month">
    </label>
    <label> Year
        <input type="text" name="year">
    </label>
    <div  style="color: red">%(error)s</div>
    <br>
    <br>
    <input type="submit">
</form>
"""
class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(form)

class TestHandler(webapp2.RequestHandler):
    def post(self):
        user_month = valid_month(self.request.get('month'))
        user_day = valid_day(self.request.get('day'))
        user_year = valid_year(self.request.get('year'))

        if not (user_month and user_day and user_year):
            self.response.out.write(form)
        else:
            self.response.out.write("Thanks! That's a totally valid day!")


app = webapp2.WSGIApplication([
    ('/', MainPage), 
    ('/testform', TestHandler)
], debug=True)
