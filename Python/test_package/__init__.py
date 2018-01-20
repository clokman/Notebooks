import test_package.print_hello_function_container
import test_package.print_hello_class_container
import test_package.print_hello_direct # note that  the paths should include root (i.e., package name)
                                       # a path without the root package name does not always work (e.g., it works inPyCharm, but not in Jupyter)
#import package_within_package