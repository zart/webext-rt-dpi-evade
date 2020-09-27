webextension-antidpi
====================


This is source code of Chrome Extension that evade Rostelecom's attempts
to inject advertisments into random javascript code over insecure connections.
It does so by appending "?" to the *.js urls if they don't use query params.
This causes RT's DPI engine to skip such an url.


Legal
-----

Licensed under MIT license.
