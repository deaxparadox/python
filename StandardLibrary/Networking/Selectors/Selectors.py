'''
- The selectors modules provides a platform-independent abstraction layer on top
of the platform-specific I/O monitoring functions in select.
'''

'''Operating Model
- APIs in selectors are even based, similar to poll() form select.
- A selector object provides methods for specifying which evens to look for on 
a socket, and then lets the caller wait for events in a platform-independent way.
- Registering interest in an even creats a SelectorKey, which holds the socket, 
information about the events of interest, and optional application data.
- The owner of the selector calls it select() method to learn about events
- The return value is a sequence of key objects and a bitmask indicating which
events have occured.
- A program using a selector should repeatedly call select(), and then handle 
the events appropriately.
'''