---
title: "matchingEMobilityServiceProviders property"
slug: "sdk-for-flutter-navigate-routing-chargingstation-matchingemobilityserviceproviders"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- matchingEMobilityServiceProviders.html -->


<div>
<h1>matchingEMobilityServiceProviders property</h1></div>

        
        List&lt;<a href="sdk-for-flutter-navigate-core-nameid-class">NameID</a>&gt;
matchingEMobilityServiceProviders
<div class="features">getter/setter pair</div>


<p>List of matched E-Mobility Service Providers.
Populated only when <a href="sdk-for-flutter-navigate-routing-electricvehicleoptions-evmobilityserviceproviderpreferences">ElectricVehicleOptions.evMobilityServiceProviderPreferences</a> was set.
This list reflects the subset of E-Mobility Service Providers supported by the charging station,
from the list specified in the request parameter <a href="sdk-for-flutter-navigate-routing-electricvehicleoptions-evmobilityserviceproviderpreferences">ElectricVehicleOptions.evMobilityServiceProviderPreferences</a>.
<a href="sdk-for-flutter-navigate-core-nameid-name">NameID.name</a> in each list item reflect to E-Mobility Service Provider name.
<a href="sdk-for-flutter-navigate-core-nameid-id">NameID.id</a> in each list item reflect to E-Mobility Service Provider id.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;NameID&gt; matchingEMobilityServiceProviders;</code></pre>

 



</div>
`
}</HTMLBlock>
