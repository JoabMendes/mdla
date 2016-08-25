#a_selected_log

This file was very large (127M) and was splited in pieces of 10M with the command:

```
  split -b 10m a_selected_log.sql a_selected_log_
```

To join the file again run:

```
  cat a_selected_log* > a_selected_log.sql
```
