# frogsay

Based on https://pypi.org/project/frogsay/
Also: https://github.com/chrlie/frogsay

Unfortunately, the installation of frogsay that is delivered by pip3 isn't 
working on my current Debian 10.2 installation. 

It has to do with `frogsay` and `python-RIBBITS` have not been adapted to the
API on `https://frog.tips/api/1/tips` is serving a JSON file in stead of a DER
file it used to do.

These changes are now reflected in this version of frogsay.
