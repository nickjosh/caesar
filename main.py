#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
from caesar import encrypt
import webapp2
import cgi

form= """
<form action = "/" method = "post">
    <label>
        Rotate by:<input type = "number" name= "rot" ></input>
    </label>
        <br>
    <label>
        Text:<textarea row = "10" cols="50" name="text" type = "text">%(value)sb</textarea>
    </label>
    <input type="submit" value="submit">
</form>
"""

class Caesar(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

    def post(self):
       rot = self.request.get("rot")
       text = self.request.get("text")
       rot = int(rot)
       answer = encrypt(text,rot)
       close = cgi.escape(answer)
       self.response.write(form % {"value":answer})


    #def post(self):
        #self.response.write(form)

app = webapp2.WSGIApplication([
('/', Caesar)
], debug=True)
