# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

rm $HOME/memcached.sock
rm $HOME/memcached.pid
memcached -d -m 64 -s $HOME/memcached.sock -P $HOME/memcached.pid 
