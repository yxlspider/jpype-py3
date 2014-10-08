#!/usr/bin/python3
# *****************************************************************************
#   Copyright 2004-2008 Steve Menard
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# *****************************************************************************

from jpype import java, startJVM, getDefaultJVMPath

startJVM(getDefaultJVMPath())

arr = java.util.ArrayList()

# no matching overloads found for this line:
arr.addAll([str(x) for x in range(50)])

print(arr)

hmap = java.util.HashMap()

# no matching overloads found for this line:
hmap.putAll({5: 6, 7: 8, 'hello': 'there'})

print(hmap)

# for x in xrange(5):
# # this works:
#    hmap.put(str(x), str(x))
#    # but this doesn't:
#    hmap.put(str(x), x)
#
#
# # this throws:
# # AttributeError: 'java.util.HashMap' object has no attribute 'iterator'
# for x in hmap:
#    print x, hmap[x]