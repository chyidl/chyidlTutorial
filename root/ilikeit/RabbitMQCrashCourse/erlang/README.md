Erlang
======


How to Build and Install Erlang/OTP
-----------------------------------
```
# First Download the released source tar ball.
$ wget http://www.erlang.org/download/otp_src_21.2.tar.gz

# Unpacking the Erlang/OTP distribution file with your GUN compatible TAR program
$ tar -zxf otp_src_21.2.tar.gz  # Assuming bash/sh 

# Now Change directory into the base directory and set the $ERL_TOP variable
$ cd top_src_21.2
$ export ERL_TOP=`pwd`

# Configuring
$ ./configure --prefix=/opt/erlang/21.2 

# Building the Erlang/OTP release 
$ make 

# Before installation you should test whether your build is working properly by running our smoke test. The smoke test is a subset of the complete Erlang/OTP test suits. First your will need to build and release the test suites
$ make release_tests 

# This creates an additional folder in $ERL_TOP/release called tests. Now, it's time to start the smoke test.
$ cd release/tests/test_server 
$ $ERL_TOP/bin/erl -s ts install -s ts smoke batch -s init stop

# To verify that everything is ok you should open $ERL_TOP/release/tests/test_server/index.html in your web browser and make sure that there are zero failed test cases.

# Now ready to install the Erlang/OTP release! 
$ make install 

# Running
```
