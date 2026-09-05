#!/bin/bash

if curl -fs http://127.0.0.1:5000/health > /dev/null; then
    echo "$(date): MyApp is healthy"
else
    echo "$(date): MyApp is DOWN"
    systemctl restart myapp
fi
