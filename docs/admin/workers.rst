===============
 ``--workers``
===============

*Based on this comment from Odony:* https://github.com/odoo/odoo/issues/39825#issuecomment-555256475

So the documentation states that a single worker can handle 6 users. What it means to say is that a worker can handle on average ~ 6 heavy read transactions / second (150ms each) = 6 web requests/s. If a user triggers about 60 heavy requests / minute during active use, that's 1 req/s on average, so 6 users could max out a worker during peaks, when all of them are active.
But in reality humans don't create sustained load, and the real usage will average out over time to a much lower number, maybe 20% of that, so a single worker may be able to handle dozens of normal users.
Unless you're facing pathological cases, like a class where all students click at the same time, or heavy automated RPC scripts (non-human heavy users), you could start with 1 worker for 30 users, maybe even 40 in a multi-tenant case where the users are distributed on different time zones, and not all databases are active at the same time.

If you don't know how many workers you will need, start with 10, but try to have the flexibility (in RAM and CPU) to deploy more easily as needed. Monitor your system to see how you're doing in terms of resources and transaction rates.

Other things to consider:

* Always configure more than 6 workers, as browsers will need to open many parallel connections and you don't want them to be queued, as users will feel the delays. 6 or 8 is a minimum, even if you don't have enough CPUs.
* The real limit to the number of workers is the RAM, not the CPUs. If workers x limit_memory_hard is much more than the available RAM, you could cause swapping or crashing. These days get at least 32GB or 64GB RAM, it's not much, and if you don't allocate everything to Odoo, the rest will be useful for OS cache and buffers.
* You can go for 2 x num_cpus + 1 workers to make sure you will be using all the cores available. Having less workers than that is a waste of resources. But you can have more workers if you want, as long as you have enough RAM.
* CPU speed matters, so try to get the best CPU clock speed you can. Better split the workers on several servers with less CPU cores but higher clocks speeds.


Longpolling
===========

Hidden feature of Multiprocessing is automatic run gevent process for longpolling support.

Longpolling is an extra proccess, i.e. if you have ``--workers=2`` then you will get 2 worker processes and 1 gevent process
