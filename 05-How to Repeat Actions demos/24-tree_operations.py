##--------------------------------------------------------------------
##
##  Demonstration - Recursive operations on trees
##
##  This demonstration presents three recursively-defined functions
##  that analyse a given tree structure, where trees are represented
##  as nested lists.
##
##  (This is an advanced example.  Don't worry if you don't
##  understand it.)
##


#---------------------------------------------------------------------
#
# Some test data
#
# Since Python allows lists to be constructed from other lists we
# can easily represent tree-like structures as nested lists.  Here
# we model a computer's directory structure using lists to represent
# folders (directories), and strings to represent files.
#
# An empty file system:

no_files = []

# A folder containing three files:

three_files = ['file1', 'file2', 'file3']

# A folder containing some files and another folder:

nested_folders = ['file1', ['file2.1', 'file2.2'], 'file3']

# A complex directory structure (the same one as depicted in the
# lecture slides):

several_folders = [['file1', 'file2', 'file3'],
                   [['file4']],
                   'file5']


#---------------------------------------------------------------------
#
# A recursive procedure to count the number of folders in a given
# tree-based directory structure
#
# The algorithm:
#
# To return the number of folders in a given tree:
# 1. If the given tree is a single file then it contains no folders,
#    so return zero
# 2. If the given tree is a folder we want to count it and all
#    the other folders it contains, so return one plus the sum of
#    the number of folders in each subtree within the given
#    folder
#
# The implementation:
#

# Return the number of "folders" (lists) in a tree of "files" (strings)
#
def num_folders(tree):
    if not isinstance(tree, list):
        # Base case - given item is a "file" (string) so don't count it
        return 0
    else:
        # Recursive case - given item is a "folder" (list) which
        # may contain other folders, so count it and the folders
        # it contains
        return 1 + sum(map(num_folders, tree))

# Some tests:

print(num_folders(no_files))
print(num_folders(three_files))
print(num_folders(nested_folders))
print(num_folders(several_folders))
print()


#---------------------------------------------------------------------
#
# A recursive procedure to count the number of files in a given
# tree-based directory structure
#
# The algorithm:
#
# To return the number of files in a given tree:
# 1. If the given tree is a single file then return one
# 2. If the given tree is a folder we want to count all
#    the files it contains, so return the sum of the number of
#    files in each subtree within the given folder
#
# The implementation:
#

# Return the number of "files" (strings) in a tree of "folders" (lists)
#
def num_files(tree):
    if not isinstance(tree, list):
        # Base case - given item is a "file" (string) so count it
        return 1
    else:
        # Recursive case - given item is a "folder" (list) so count
        # the number of files it contains
        return sum(map(num_files, tree))

# Some tests:

print(num_files(no_files))
print(num_files(three_files))
print(num_files(nested_folders))
print(num_files(several_folders))
print()


#---------------------------------------------------------------------
#
# A recursive procedure to return the maximum depth of a given
# tree-based directory structure
#
# The algorithm:
#
# To return the depth of a given tree:
# 1. If the given tree is a single file then return zero
#    because it doesn't increase the tree's depth
# 2. If the given tree is a folder it adds another level to the
#    tree, so return one plus the maximum depth of any subtree
#    within the given folder (which should evaluate to zero if
#    if the folder is empty)
#
# The implementation:
#

# Return the depth of a directory of "folders" (lists) and
# "files" (strings)
#
def dir_depth(tree):
    if not isinstance(tree, list):
        # Base case - item is a "file" (string) so don't count it
        # because it doesn't increase the tree's depth
        return 0
    else:
        # Recursive case - item is a "folder" (list), so it
        # increases the tree's depth by one plus the largest
        # depth of its subtrees (if any)
        return 1 + max(list(map(dir_depth, tree)) + [0])
    
# Some tests:

print(dir_depth(no_files))
print(dir_depth(three_files))
print(dir_depth(nested_folders))
print(dir_depth(several_folders))
