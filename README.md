# gears-exercise

A small demonstration setup demonstrating a Vagrant environment which brings up a loadbalancer and a specified number of web server nodes.
It then provides a small python script demonstrating an even balancing between the nodes from a specified number of requests.

=== Instructions ===

Change the number of webserver nodes to deploy by editing the NO_OF_NODES variable in the Vagrant file in the project root.

Execute the testlb.py script as such:

./testlb.py --host localhost --num num_reqs



