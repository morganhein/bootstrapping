#!/usr/bin/env bash

# Installs the 1password CLI
# https://support.1password.com/command-line-getting-started/

if [[ "$OSTYPE" == "darwin"* ]]; then
    curl https://cache.agilebits.com/dist/1P/op/pkg/v1.8.0/op_darwin_amd64_v1.8.0.pkg -O
    chmod +x op_darwin_amd64_v1.8.0.pkg
    ./op_darwin_amd64_v1.8.0.pkg
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    gpg --keyserver hkps://keyserver.ubuntu.com --receive-keys 3FEF9748469ADBE15DA7CA80AC2D62742012EA22
    curl -o /tmp/op.zip https://cache.agilebits.com/dist/1P/op/pkg/v1.8.0/op_linux_amd64_v1.8.0.zip
    unzip -d /tmp/op/ /tmp/op.zip
    gpg --verify /tmp/op/op.sig /tmp/op/op
    sudo mv /tmp/op/op /usr/local/bin
else
    echo "UNABLE TO DETERMINE OPERATING SYSTEM"
    return
fi

echo "1Password CLI installed.

Type op 'signin example.1password.com wendy_appleseed@example.com' to log in."

# TODO: set 'eval $(op signin example)' to a login script