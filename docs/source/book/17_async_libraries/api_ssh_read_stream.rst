class asyncssh.SSHReader[source]
SSH read stream handler

channel
    The SSH channel associated with this stream

 
logger
    The SSH logger associated with this stream

 
at_eof()[source]
    Return whether the stream is at EOF

    This method returns True when EOF has been received and all data in 
    the stream has been read.

 
read(n=-1)[source]
    Read data from the stream

    This method is a coroutine which reads up to n bytes or characters from the stream.
    If n is not provided or set to -1, it reads until EOF or a signal is received.

    If EOF is received and the receive buffer is empty, an empty bytes or str object 
    is returned.

    If the next data in the stream is a signal, 
    the signal is delivered as a raised exception.

    Note Unlike traditional asyncio stream readers, the data will be delivered as 
    either bytes or a str depending on whether an encoding was specified when 
    the underlying channel was opened.
 
readline()[source]
    Read one line from the stream

    This method is a coroutine which reads one line, ending in 'n'.

    If EOF is received before 'n' is found, the partial line is returned. 
    If EOF is received and the receive buffer is empty, an empty bytes or 
    str object is returned.

    If the next data in the stream is a signal, the signal is delivered 
    as a raised exception.

    Note In Python 3.5 and later, SSHReader objects can also be used as 
    async iterators, returning input data one line at a time.
     
readuntil(separator)
    Read data from the stream until separator is seen

    This method is a coroutine which reads from the stream until the requested 
    separator is seen. If a match is found, the returned data will include the 
    separator at the end.

    The separator argument can be either a single bytes or str value or a 
    sequence of multiple values to match against, returning data as soon as any 
    of the separators are found in the stream.

    If EOF or a signal is received before a match occurs, an IncompleteReadError 
    is raised and its partial attribute will contain the data in the stream prior 
    to the EOF or signal.

    If the next data in the stream is a signal, the signal is delivered as a 
    raised exception.
