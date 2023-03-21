repo-setup
=============

A tool for managing repo_setup.repos from places like RDO Trunk and Ceph.

See: https://blogs.rdoproject.org/2016/04/newbie-in-rdo-2-rdo-trunk-from-a-bird-s-eye-view/

Also ensures yum-plugin-priorities is installed since the RDO Trunk repos
require that to work sanely.

.. note:: The tool will remove any delorean* repos at the target location
          to avoid conflicts with older repos. This means you must specify
          all of the repos you want to enable in one repo-setup call.

Examples
--------
Install Podified CI testing repos for UBI-8 by the distro specific path::

    repo-setup -d ubi8 podified-ci-testing --output-path /etc/distro.repos.d

Install current master RDO Trunk repo and the deps repo::

    repo-setup current

Install current-podified RDO Trunk repo and the deps repo::

    repo-setup current-podified

Install the current-podified-dev repo. This will also pull current and deps,
and will adjust the priorities of each repo appropriately::

    repo-setup current-podified-dev

Install the mitaka RDO Trunk repo and deps::

    repo-setup -b mitaka current

Write repos to a different path::

    repo-setup -o ~/test-repos current

Install the current-podified, deps, and ceph repos. NOTE: The Ceph repo is
installed from a package and thus does not respect -o::

    repo-setup current-podified ceph
