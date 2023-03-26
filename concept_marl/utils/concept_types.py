# coding=utf-8
# Copyright 2022 The Google Research Authors.
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

"""Concept types supported by Concept PPO."""

import enum


class ConceptType(enum.IntEnum):
  """Agents which have default initializers supported below."""
  BINARY = 0
  SCALAR = 1
  CATEGORICAL = 2
  POSITION = 3


class ObjectType(enum.IntEnum):
  """Agents which have default initializers supported below."""
  AGENT = 0
  ENVIRONMENT_OBJECT = 1
