# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""Session scoped fixtures for TIM-VX tests."""

from tvm import rpc
import pytest
import os


@pytest.fixture(scope="session", name="remote")
def get_remote() -> rpc.RPCSession:
    """Get a remote RPC session for testing.

    Returns:
        rpc.RPCSession: 
        A connected rpc session if remote RPC host is given;
        A local session if not.
    """
    # Read remote RPC server address from environment variables.
    rpc_host = os.environ.get("RPC_HOST")
    rpc_port = int(os.environ.get("RPC_PORT") or 0)
    return rpc.connect(rpc_host, rpc_port) if rpc_host else rpc.LocalSession()
