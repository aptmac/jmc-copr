#!/bin/bash
VERSION=9.0.0-SNAPSHOT
TARBALL_NAME=org.openjdk.jmc-$VERSION-linux.gtk.x86_64.tar.gz
URL=https://github.com/adoptium/jmc-build/releases/download/$VERSION/$TARBALL_NAME

# if a jmc snapshot tarball already exists, remove it prior to downloading a new one
if [ -f $TARBALL_NAME ]; then
    rm $TARBALL_NAME
fi

wget $URL
