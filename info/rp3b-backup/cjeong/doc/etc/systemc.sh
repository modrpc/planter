#!/bin/bash

# activemq
export SYSTEMC_HOME=/opt/systemc-2.3.1

# Header files  : <SYSTEMC_HOME>/include
# Libraries     : <SYSTEMC_HOME>/lib-linux
# Documentation : <SYSTEMC_HOME>/docs
# Examples      : <SYSTEMC_HOME>/examples

export SYSTEMC_INCDIR=$SYSTEMC_HOME/include
export SYSTEMC_LIBDIR=$SYSTEMC_HOME/lib-linux

export LD_LIBRARY_PATH=$SYSTEMC_LIBDIR:$LD_LIBRARY_PATH
