=============================
 Remote Procedure Call (RPC)
=============================

Call method
===========

.. code-block:: js

    /**
     * Call a method (over RPC) on the bound OpenERP model.
     *
     * @param {String} method name of the method to call
     * @param {Array} [args] positional arguments
     * @param {Object} [kwargs] keyword arguments
     * @param {Object} [options] additional options for the rpc() method
     * @returns {jQuery.Deferred<>} call result
     */
    call: function (method, args, kwargs, options) {
        args = args || [];
        kwargs = kwargs || {};
        if (!_.isArray(args)) {
            // call(method, kwargs)
            kwargs = args;
            args = [];
        }
        var call_kw = '/web/dataset/call_kw/' + this.name + '/' + method;
        return session.rpc(call_kw, {
            model: this.name,
            method: method,
            args: args,
            kwargs: kwargs
        }, options);
    },

How to call wizard method from js
=================================

.. code-block:: js

    var compose_model = new Model('mail.compose.message');
    return compose_model.call('create', [msg, {default_parent_id: options.parent_id}])
        .then(function(id){
            return compose_model.call('send_mail_action', [id, {}]);
        });
