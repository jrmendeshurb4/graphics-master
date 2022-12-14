# Copyright 2020 The TensorFlow Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for rasterize than splat functionality with opengl rasterization."""

from tensorflow_graphics.rendering import rasterization_backend
from tensorflow_graphics.rendering.tests import splat_test
from tensorflow_graphics.util import test_case


class SplatWithOpenGLTest(splat_test.SplatTest):

  def setUp(self):
    super().setUp()
    # This pattern was chosen instead of a parametrized test to faclitate
    # running the test cases in pure CPU mode on machines that do not have a
    # GPU. In this case the opengl rasterizer cannot be added as dependency to
    # the binary as CPU only machines do not have the required libEGL.so
    # available. This pattern provides a separate build target for the opengl
    # rasterizer version.
    self._backend = rasterization_backend.RasterizationBackends.OPENGL


if __name__ == '__main__':
  test_case.main()
