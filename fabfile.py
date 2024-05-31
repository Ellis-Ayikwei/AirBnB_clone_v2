# Fabfile to:
#    - update the remote system(s) 
#    - download and install an application

# Import Fabric's API module
from fabric.api import *


env.hosts = [
    'localhost'
    #'server.domain.tld',
  # 'ip.add.rr.ess
  # 'server2.domain.tld',
]
# Set the username

# Set the password [NOT RECOMMENDED]
#env.password = "passwd"

def update_upgrade():
    """
        Update the default OS installation's
        basic default tools.
                                            """
    sudo("apt update")
    sudo("apt -y upgrade")

def install_memcached():
    """ Download and install memcached. """
    sudo("apt install -y memcached")

def update_install():

    # Update
    update_upgrade()
    
    # Install
    install_memcached()
