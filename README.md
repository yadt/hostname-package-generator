hostname-package-generator
==========================

Create an RPM which provides the hostname. This helps other packages to be pinned to this host.

We use it to make sure that the config RPM created by http://github.com/yadt/yadt-config-rpm-maker will be installed only on the intended host and not somewhere else.

```
Manage an RPM that provides the hostname in the RPM database.

Usage:

./hostname-package [Options ...]

Options:
    --help          Show help
    --generate      Generate and install new hostname package
    --out DIR       Write resulting RPM to DIR instead of installing it
    --fqdn FQDN     Use FQDN instead of 'hostname -f'
    --prefix PREFIX Use PREFIX instead of yadt for the generic
                    yadt-hostname-package provide
    --provides PROV Additional RPM Provides

Called without options will display the current status of the hostname package.

Set the KEEPWORKDIR environment variable to keep the build area for debugging.

Licensed under the GNU General Public License, see 
http://www.gnu.org/licenses/gpl.txt for full text.
```

Typical Usage:
--------------

Install a hostname package with `hostname-package --generate` and depend in other packages on one of the names provided by it. Run `hostname-package` to view the installed hostname RPM.

Installation
------------

Clone this git repo and run `make` to run the tests and create an RPM. For production use it is recommended to use `make srpm` and build the resulting src.rpm into the noarch.rpm in your RPM build environment.
