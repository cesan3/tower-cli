# Copyright 2013, AnsibleWorks Inc.
# Michael DeHaan <michael@ansibleworks.com>
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

import BaseCommand
import awx_cli
import awx_cli.common as common

class VersionCommand(BaseCommand.BaseCommand):

    """ shows AWX version information """

    def __init__(self, toplevel):
        super(VersionCommand, self).__init__(toplevel)
        self.name = "version"

    def run(self, args):
 
        parser = common.get_parser()
        # parser.add_option('-f', '--foo', dest='foo', default=None, type='str')

        (options, args) = parser.parse_args()
        handle = common.connect(options)
 
        data = handle.get('/api/v1/config/')

        output = dict(
           cli_version = awx_cli.__version__,
           server_version = data['version']
        )
        print common.dump(output)

        return 0



