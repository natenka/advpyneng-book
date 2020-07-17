SSHWriter
class asyncssh.SSHWriter
SSH write stream handler

channel
    The SSH channel associated with this stream

 
logger
    The SSH logger associated with this stream

 
get_extra_info(name, default=None)
    Return additional information about this stream

    This method returns extra information about the channel associated with 
    this stream. See get_extra_info() on SSHClientChannel for additional information.

 
can_write_eof()
    Return whether the stream supports write_eof()

 
drain()
    Wait until the write buffer on the channel is flushed

    This method is a coroutine which blocks the caller if the stream is currently
    paused for writing, returning when enough data has been sent on the channel to 
    allow writing to resume. This can be used to avoid buffering an excessive 
    amount of data in the channel’s send buffer.

 
write(data)
    Write data to the stream

    This method writes bytes or characters to the stream.

    Note Unlike traditional asyncio stream writers, the data must be supplied as either 
    bytes or a str depending on whether an encoding was specified when the underlying 
    channel was opened.
 
writelines(list_of_data)
    Write a collection of data to the stream

 
write_eof()
    Write EOF on the channel

    This method sends an end-of-file indication on the channel, after which no 
    more data can be written.

    Note On an SSHServerChannel where multiple output streams are created, 
    writing EOF on one stream signals EOF for all of them, since it applies to 
    the channel as a whole.
     
close()
    Close the channel

    Note After this is called, no data can be read or written from any of the streams
    associated with this channel.
     
is_closing()
    Return if the stream is closing or is closed

 
wait_closed()
    Wait until the stream is closed

    This should be called after close() to wait until the underlying connection is closed.
