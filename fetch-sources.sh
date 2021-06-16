#!/bin/bash

TARBALL_NAME=org.openjdk.jmc-8.1.0-SNAPSHOT-linux.gtk.x86_64.tar.gz
URL=https://github.com/AdoptOpenJDK/openjdk-jmc-overrides/releases/download/8.1.0-SNAPSHOT/$TARBALL_NAME

# if a jmc snapshot tarball already exists, remove it prior to downloading a new one
if [ -f $TARBALL_NAME ]; then
    rm $TARBALL_NAME
fi

wget $URL
