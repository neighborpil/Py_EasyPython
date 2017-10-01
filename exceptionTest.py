def __call__(self, string):
    #the special argument "-" means sys.std(in, out)
    if string == '-':
        if 'r' in self._mode:
            return _sys.stdin
        elif 'w' in self._mode:
            return _sys.sysout
        else:
            msg = _('argument "=" with mode %r') % self._mode
            raise ValueError(msg)

    #all other arguments are used as file names
        try:
            return open(string, self._mode._bufsize, self._encoding, self._errors)
        except OSError as e:
            message = _("can't open '%s': %s")
            raise ArgumentTypeError(message % (string, e))
