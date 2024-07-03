#!/bin/bash

if [[ "${BASH_SOURCE[0]}" != "${0}" ]]; then
    echo "This script must not be sourced"
    exit 1
fi

pyresttest http://proxy ./tests/api.yml