# Copyright 2024 Google LLC
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

from setuptools import setup, find_packages
import os

# Get the path to the prompts directory (inside src)
PROMPTS_DIR = os.path.join(os.path.dirname(__file__), 'prompts')

setup(
    name='devai-cli',
    version='0.0.0',
    packages=find_packages(),
    py_modules=['devai'],
    package_data={
        'devai': ['prompts/**/*.yaml'],  # Include all YAML files from prompts directory
    },
    data_files=[
        ('prompts', [os.path.join(PROMPTS_DIR, f) for f in os.listdir(PROMPTS_DIR) if f.endswith('.yaml')]),
    ],
    install_requires=[
        'click==8.1.7',
        'google-cloud-aiplatform'
    ],
    entry_points={
        'console_scripts': [
            'devai = devai.cli:devai',
        ],
    },
)