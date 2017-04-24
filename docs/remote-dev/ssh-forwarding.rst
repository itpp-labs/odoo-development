======================
 SSH agent forwarding
======================


To send commit or get access to private repositories you can use either login-password authentication or ssh keys. In later case you can face a problem to do it on remote server, because your private ssh key is not installed there. The good news is that you don't need to do it. You can "forward ssh keys". Simply add following lines to ``~/.ssh/config`` file on your (local) computer::

  Host your.dev.server.example.com
    ForwardAgent yes

Then connect to your server and type to test::

    ssh -T git@github.com

For more information see: https://developer.github.com/guides/using-ssh-agent-forwarding/
