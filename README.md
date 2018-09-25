# CDNNodes
DNS Resolve方法
====
>根据已有的CDN厂商的客户网站的域名（网上搜索或手动查到一些CNAME符合的域名），利用CNAMEs’ Feature可以确定所属的CDN厂商。从多个DNS节点(5000个)访问同一网站域名，进行网站的域名解析，得到不同的CDN节点的IP地址；通过外部API接口（我目前使用了ip-api.com接口，因为区域比较详细），根据IP地址找到CDN节点的地理位置等信息。

Censys数据扫描方法
====
>根据ipv4、80端口的Censys扫描数据，凑成一个HTTP Get包，IP地址访问域名，分析返回结果，如果结果中带有域名网站的内容，则用了它的CDN。
>利用HTTP Response的特征值进行筛选，过滤得到符合CDN厂商的IP。
