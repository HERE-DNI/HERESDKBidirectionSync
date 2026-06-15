---
title: "evChargingPool property"
slug: "sdk-for-flutter-navigate-search-details-evchargingpool"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- evChargingPool.html -->


<div>
<h1>evChargingPool property</h1></div>

<a href="sdk-for-flutter-navigate-search-evchargingpool-class">EVChargingPool</a>?
        evChargingPool
<div class="features">getter/setter pair</div>


<p>EV charging pool details. It is available only for a place that is a charging pool
for electric vehicles.
It is fully supported for offline search, provided that <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.ev</a>
is enabled in <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-layerconfiguration">SDKOptions.layerConfiguration</a>.</p>
<p>For online search, this feature is only available if it is explicitly enabled.
To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
name: "lookup.show" or "discover.show" or "browse.show"
value: "ev"
To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
"lookup.show", "discover.show" and "browse.show".
To enable fuel station details or truck amenities, the custom option value can be combined
as "ev,truck", "ev,truck,fuel" etc.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">EVChargingPool? evChargingPool;</code></pre>

 



</div>
`
}</HTMLBlock>
