#!/bin/bash

set -x

### Find the path to this script
# Absolute path to this script. /home/user/bin/foo.sh
SCRIPT="$(readlink -f $0)"
# Absolute path this script is in. /home/user/bin
SCRIPTPATH="$(dirname $SCRIPT)"

SPAMBAYES_DB_PATH="$SCRIPTPATH/spambayes.db"

function test() {
    sb_filter -d "$SPAMBAYES_DB_PATH" - | grep -q '^X-Spambayes-Classification: spam'
    exit $?
}

function train_ham() {
    sb_filter -d "$SPAMBAYES_DB_PATH" -g -
    exit $?
}

function train_spam() {
    sb_filter -d "$SPAMBAYES_DB_PATH" -s -
    exit $?
}


if [ "$1" == "test" ] ; then
    test
fi

if [ "$1" == "train_spam" ] ; then
    train_spam
fi

if [ "$1" == "train_ham" ] ; then
    train_ham
fi
