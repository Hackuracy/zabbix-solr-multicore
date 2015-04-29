# zabbix-solr-multicore
Primitive solution for SolR monitoring on Zabbix

## Presentation

My problem was that my solr contains numerous core.
For many reason i need to monitor some cache / document values.
I found some template to monitor the default core named 'collection1'.
I decide to create a discovery rule for corenames and monitor some item.

This solution is a combination of built-in jvm template and https://github.com/flaviotorres/zabbix using JMX connector

## Discovery Rule

It use this URI /admin/cores?action=STATUS which returns xml list of cores.

## UserParameter 
Just one for discovery UserParameter=solr.core.discovery.
All of item are retreived throught jmx connector

##Items



