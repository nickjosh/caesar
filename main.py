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

class Caesar(webapp2.RequestHandler):
    def get(self):
        


form="""
<form action="/" method="post">
<label>Rotate by:input type="text">

</label>
<textarea rows="8" cols="60">
<input type="submit" value="Submit">

</form>
"""
self.response.write(form)
    def post(self):

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
