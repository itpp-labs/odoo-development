================
 LXD Containers
================

.. code-block:: sh

    # For understanding LXC see https://wiki.debian.org/LXC

    # Based on:
    # lxd + docker: https://stgraber.org/2016/04/13/lxd-2-0-docker-in-lxd-712/
    # lxd network (static ip): https://stgraber.org/2016/10/27/network-management-with-lxd-2-3/
    LXD_NETWORK="dev-network2"

    # install lxd 2.3+
    apt-get install software-properties-common iptables-persistent

    add-apt-repository ppa:ubuntu-lxc/lxd-stable
    apt-get update
    apt-get dist-upgrade
    apt-get install lxd

    # init lxd
    lxd init

    # init network
    lxc network create ${LXD_NETWORK}
    lxc network show ${LXD_NETWORK}  # check ipv4.address field


    ############################
    # Per each Developer
    GITHUB_USERNAME="yelizariev"
    CONTAINER="${GITHUB_USERNAME}"
    SERVER_DOMAIN="${GITHUB_USERNAME}.dev.it-projects.info"
    NGINX_CONF="dev-${GITHUB_USERNAME}.conf"
    LOCAL_IP="10.37.82.100"  # use one from network subnet
    PORT="10100"  # unique per each developer

    lxc init ubuntu-daily:16.04 ${CONTAINER} -p default
    lxc network attach ${LXD_NETWORK} ${CONTAINER} eth0
    lxc config device set ${CONTAINER} eth0 ipv4.address ${LOCAL_IP}
    lxc config device add ${CONTAINER} sharedcache disk path=/root/.cache source=/var/lxc/share/cache
    lxc config set ${CONTAINER} security.privileged true
    lxc config set ${CONTAINER} raw.lxc "lxc.apparmor.profile=unconfined"

    # forward ssh port
    iptables -t nat -A PREROUTING -p tcp --dport ${PORT} -j DNAT \
      --to-destination ${LOCAL_IP}:22
      
    # save iptables record. Otherwise it's disappeared after rebooting
    sudo netfilter-persistent save
    sudo netfilter-persistent reload

    lxc start ${CONTAINER}
    lxc exec ${CONTAINER} -- mkdir -p /root/.ssh
    lxc exec ${CONTAINER} -- bash -c "curl --silent https://github.com/${GITHUB_USERNAME}.keys >> /root/.ssh/authorized_keys"
    # colorize prompt:
    lxc exec ${CONTAINER} -- sed -i "s/#force_color_prompt=yes/force_color_prompt=yes/" /root/.bashrc
    lxc exec ${CONTAINER} -- sed -i "s/01;32m/01;36m/" /root/.bashrc

    # install some packages
    lxc exec  ${CONTAINER} -- apt update
    lxc exec  ${CONTAINER} -- apt dist-upgrade -y
    lxc exec  ${CONTAINER} -- apt install docker.io htop python3-pip -y
    lxc exec  ${CONTAINER} -- pip3 install odooup -y
    # https://docs.docker.com/v17.09/compose/install/#install-compose
    lxc exec  ${CONTAINER} -- curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
    lxc exec  ${CONTAINER} -- chmod +x /usr/local/bin/docker-compose

    ## nginx on host machine
    cd /tmp/
    curl -s https://raw.githubusercontent.com/it-projects-llc/odoo-development/master/docs/remote-dev/lxd/nginx.conf > nginx.conf
    sed -i "s/NGINX_SERVER_DOMAIN/.${SERVER_DOMAIN}/g" nginx.conf
    sed -i "s/SERVER_HOST/${LOCAL_IP}/g" nginx.conf
    cp nginx.conf /etc/nginx/sites-available/${NGINX_CONF}
    ln -s /etc/nginx/sites-available/${NGINX_CONF} /etc/nginx/sites-enabled/${NGINX_CONF}
    # then restart nginx in a usual way

    ###################
    # Control commands

    # delete container
    lxc delete CONTAINER-NAME

    # see iptables rules
    iptables -L -t nat

    # delete nat rule
    iptables -t nat -D PREROUTING POSITION_NUMBER
