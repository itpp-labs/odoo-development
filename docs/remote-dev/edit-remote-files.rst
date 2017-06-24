=============================
 Edit files on remote server
=============================


sshfs
=====

.. code-block:: sh

    sudo apt-get install sshfs
    mkdir /mnt/remote-files/

    # use your HOST and PORT
    # Warnings. It's not secure to use such mounting for production server.
    sshfs -o allow_other,IdentityFile=~/.ssh/id_rsa root@HOST:/root/odoo /mnt/remote-files -p PORT
    # update /etc/fuse.conf if needed

    # to unmount use
    sudo umount /mnt/remote-files


win-sshfs (Windows)
===================

After launching the win-sshfs program, you will be presented with a graphical interface to make the process of mounting a remote file share simple.

Step 1: Click the Add button in the lower left corner of the window.

Step 2: Enter a name for the file share in the Drive Name field.

Step 3. Enter the IP of your droplet in the Host field.

Step 4. Enter your SSH port. (Leave as port 22 unless you have changed the SSH port manually).

Step 5. Enter your username in the Username field. (Unless you have set up user accounts manually you will enter root in this field).

Step 6. Enter your SSH password in the password field. (Note on Windows you will need to have your droplet configured for password logins rather than ssh-key-authentication).

Step 7. Enter your desired mount point in the Directory field. (Enter / to mount the file system from root. Likewise you can enter /var/www or ~/ for your home directory).

Step 8. Select the drive letter you would like Windows to use for your droplets file system.

Step 9. Click the Mount button to connect to the droplet and mount the file system.

Now your virtual server's file system will be available through My Computer as the drive letter you chose in step 8.

References
==========

* https://www.digitalocean.com/community/tutorials/how-to-use-sshfs-to-mount-remote-file-systems-over-ssh
* https://askubuntu.com/questions/780705/fuse-unknown-option-defer-permissions
