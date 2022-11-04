#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
from unicodedata import name
# from os import chdir
__metaclass__ = type


DOCUMENTATION = r'''
---
module: my_test

short_description: This is my test module

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This is my longer description explaining my test module.

options:
    name:
        description: This is the message to send to the test module.
        required: true
        type: str
    new:
        description:
            - Control to demo if the result of this module is changed or not.
            - Parameter description can be a list as well.
        required: false
        type: bool
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - my_namespace.my_collection.my_doc_fragment_name

author:
    - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
# Pass in a message
- name: Test with a message
  my_namespace.my_collection.my_test:
    name: hello world

# pass in a message and have changed true
- name: Test with a message and changed output
  my_namespace.my_collection.my_test:
    name: hello world
    new: true

# fail the module
- name: Test failure of the module
  my_namespace.my_collection.my_test:
    name: fail me
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
original_message:
    description: The original name param that was passed in.
    type: str
    returned: always
    sample: 'hello world'
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'goodbye'
'''

from ansible.module_utils.basic import AnsibleModule

def execute_file(name_f,text_f):
    # os.chdir(path)
    my_file = open(name_f,"w+")
    my_file.write(text_f)
    my_file.close()
    if text_f != '':
        return {'File is change': True}
    else: return {'File is empty': True}

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
      #  path = dict(type='str', required=True),
        path_n = dict(type='str', required=True),
        text_f = dict(type='str', required=False)
     
    )
   
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    params = module.params
    # path = params['path']
    name_f = params['path_n']
    text_f = params['text_f']
   
    result = execute_file(name_f,text_f)  
    
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()