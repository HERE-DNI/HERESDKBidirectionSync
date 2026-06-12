---
title: "ChargingStation.withDetails constructor"
slug: "sdk-for-flutter-navigate-routing-chargingstation-chargingstation-withdetails"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ChargingStation.withDetails.html -->


<div>
<h1>ChargingStation.withDetails constructor</h1></div>

ChargingStation.withDetails(<ol class="parameter-list"> <li>String? id, </li>
<li>String? name, </li>
<li><a href="/sdk-for-flutter-navigate-routing-chargingconnectorattributes-class">ChargingConnectorAttributes</a>? connectorAttributes, </li>
<li><a href="/sdk-for-flutter-navigate-core-nameid-class">NameID</a>? brand, </li>
<li><a href="/sdk-for-flutter-navigate-core-nameid-class">NameID</a>? chargePointOperator, </li>
<li>List&lt;<a href="/sdk-for-flutter-navigate-core-nameid-class">NameID</a>&gt; matchingEMobilityServiceProviders, </li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>id</code> Identifier of this charging station. It can only be null when custom charging
stations from non-HERE datasets have been injected on the HERE platform.
By default, with HERE datasets it is guranteed to be not null.</li>
<li><code>name</code> Human readable name of this charging station. It can be null when there is no
name associated with the station.</li>
<li><code>connectorAttributes</code> Details of the connector suggested to be used.</li>
<li><code>brand</code> Charging station brand.
<a href="/sdk-for-flutter-navigate-core-nameid-name">NameID.name</a> reflect to charging station brand name.
<a href="/sdk-for-flutter-navigate-core-nameid-id">NameID.id</a> reflect to charging station brand unique ID.</li>
<li><code>chargePointOperator</code> Charging station charge-point-operator.
<a href="/sdk-for-flutter-navigate-core-nameid-name">NameID.name</a> reflect to charge-point-operator name.
<a href="/sdk-for-flutter-navigate-core-nameid-id">NameID.id</a> reflect to charge-point-operator ID.</li>
<li><code>matchingEMobilityServiceProviders</code> List of matched E-Mobility Service Providers.
Populated only when <a href="/sdk-for-flutter-navigate-routing-electricvehicleoptions-evmobilityserviceproviderpreferences">ElectricVehicleOptions.evMobilityServiceProviderPreferences</a> was set.
This list reflects the subset of E-Mobility Service Providers supported by the charging station,
from the list specified in the request parameter <a href="/sdk-for-flutter-navigate-routing-electricvehicleoptions-evmobilityserviceproviderpreferences">ElectricVehicleOptions.evMobilityServiceProviderPreferences</a>.
<a href="/sdk-for-flutter-navigate-core-nameid-name">NameID.name</a> in each list item reflect to E-Mobility Service Provider name.
<a href="/sdk-for-flutter-navigate-core-nameid-id">NameID.id</a> in each list item reflect to E-Mobility Service Provider id.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ChargingStation.withDetails(this.id, this.name, this.connectorAttributes, this.brand, this.chargePointOperator, this.matchingEMobilityServiceProviders);</code></pre>

 



</div>
`
}</HTMLBlock>
