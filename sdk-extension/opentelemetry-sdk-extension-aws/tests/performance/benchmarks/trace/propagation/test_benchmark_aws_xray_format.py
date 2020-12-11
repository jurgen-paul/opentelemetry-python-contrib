# Copyright The OpenTelemetry Authors
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

from requests.structures import CaseInsensitiveDict

from opentelemetry.sdk.extension.aws.trace.propagation.aws_xray_format import (
    TRACE_HEADER_KEY,
    AwsXRayFormat,
)
from opentelemetry.trace.propagation.textmap import DictGetter

XRAY_PROPAGATOR = AwsXRayFormat()


def test_extract_single_header(benchmark):
    benchmark(
        XRAY_PROPAGATOR.extract,
        DictGetter(),
        {
            TRACE_HEADER_KEY: "bdb5b63237ed38aea578af665aa5aa60-00000000000000000c32d953d73ad225"
        },
    )


def test_inject_empty_context(benchmark):
    benchmark(XRAY_PROPAGATOR.inject, CaseInsensitiveDict.__setitem__, {})
