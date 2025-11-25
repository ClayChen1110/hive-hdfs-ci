#!/bin/bash

# Script to check if out-dated.txt exists on HDFS at /tmp/share

HDFS_PATH="/tmp/share/out-dated.txt"

echo "Checking if $HDFS_PATH exists on HDFS..."

if hdfs dfs -test -e "$HDFS_PATH"; then
    echo "✓ File exists: $HDFS_PATH"
    exit 0
else
    echo "✗ File does not exist: $HDFS_PATH"
    exit 1
fi
