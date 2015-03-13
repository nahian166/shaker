# Copyright (c) 2015 Mirantis Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from shaker.engine.executors import base


class NetperfExecutor(base.BaseExecutor):
    def get_command(self):
        cmd = base.CommandLine('netperf')
        cmd.add('-H', self.agent['slave']['ip'])
        cmd.add('-l', self.test_definition.get('time') or 60)
        cmd.add('-t', self.test_definition.get('method') or 'TCP_STREAM')
        return cmd.make()


class NetperfWrapperExecutor(base.BaseExecutor):
    def get_command(self):
        target_ip = self.agent['slave']['ip']
        return ('netperf-wrapper -H %(ip)s -f stats %(method)s' %
                dict(ip=target_ip,
                     method=self.test_definition['method']))