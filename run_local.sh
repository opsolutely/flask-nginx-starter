#!/bin/bash

source ./local_files/keys.sh
supervisord -c ./local_files/supervisor_local.conf
