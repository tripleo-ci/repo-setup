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
Install TripleO CI testing repos for UBI-8 by the distro specific path::

    repo-setup -d ubi8 repo-setup-ci-testing --output-path /etc/distro.repos.d

Install current master RDO Trunk repo and the deps repo::

    repo-setup current

Install current-tripleo RDO Trunk repo and the deps repo::

    repo-setup current-tripleo

Install the current-repo-setup-dev repo. This will also pull current and deps,
and will adjust the priorities of each repo appropriately::

    repo-setup current-repo-setup-dev

Install the mitaka RDO Trunk repo and deps::

    repo-setup -b mitaka current

Write repos to a different path::

    repo-setup -o ~/test-repos current

Install the current-tripleo, deps, and ceph repos. NOTE: The Ceph repo is
installed from a package and thus does not respect -o::

    repo-setup current-tripleo ceph

TripleO
```````

To use this for TripleO development, replace the tripleo.sh --repo-setup
step with the following::

    git clone https://github.com/cybertron/repo-setup
    cd repo-setup
    sudo ./setup.py install
    sudo repo-setup current-repo-setup-dev ceph

Now you're ready to install the undercloud::

    tripleo.sh --undercloud

And to build images::

    export OVERCLOUD_IMAGES_DIB_YUM_REPO_CONF="$(ls /etc/yum.repos.d/delorean* /etc/yum.repos.d/CentOS-Ceph-*)"
    tripleo.sh --overcloud-images

.. note:: This is a tool for bootstrapping the repo setup for TripleO,
    so it should not have any runtime OpenStack dependencies
    or we end up in a chicken-and-egg pickle, and let's be honest - no one wants a
    chicken and egg pickle.
