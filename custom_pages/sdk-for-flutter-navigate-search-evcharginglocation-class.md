---
title: "EVChargingLocation class abstract"
slug: "sdk-for-flutter-navigate-search-evcharginglocation-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EVChargingLocation-class.html -->


<div>
<h1>EVChargingLocation class abstract</h1></div>

<p>An electric vehicle (EV) charging location.</p>
<p>The semantics generally follow the OCPI 2.2.1 standard.</p>
<p>Known EV-specific acronyms:</p>
<ul>
<li>EV: Electric Vehicle</li>
<li>OCPI: Open Charge Point Interface (a standard with a rather wide adoption worldwide, <a href="https://evroaming.org/">https://evroaming.org/</a>)</li>
<li>CPO: Charge Point Operator (company that runs the EV charging location)</li>
<li>eMSP: e-Mobility Service Provider (customer-facing company)</li>
<li>EVSE: Electric Vehicle Supply Equipment (the actual charger that can charge one car at a time)</li>
</ul>
<p>A charging location includes a collection of one or more EV supply equipment (EVSE) instances.
Typically, the charging location is the exact location of the group of EVSEs,
simplified to a single point, but it can also be the entrance of a parking structure
which contains these EVSEs.
Each EVSE supports more precise position, where applicable.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-search-evcharginglocation-evcharginglocation">EVChargingLocation</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-search-evcharginglocation-connectorgroups">connectorGroups</a></li><li><a href="sdk-for-flutter-navigate-search-evcharginglocation-cpoid">cpoID</a></li><li><a href="sdk-for-flutter-navigate-search-evcharginglocation-emobilityserviceproviders">eMobilityServiceProviders</a></li><li><a href="sdk-for-flutter-navigate-search-evcharginglocation-energymix">energyMix</a></li><li><a href="sdk-for-flutter-navigate-search-evcharginglocation-evchargingoperator">evChargingOperator</a></li><li><a href="sdk-for-flutter-navigate-search-evcharginglocation-evchargingsuboperator">evChargingSubOperator</a></li><li><a href="sdk-for-flutter-navigate-search-evcharginglocation-evses">evses</a></li><li><a href="sdk-for-flutter-navigate-search-evcharginglocation-facilitytypes">facilityTypes</a></li><li><a href="sdk-for-flutter-navigate-search-evcharginglocation-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-search-evcharginglocation-id">id</a></li><li><a href="sdk-for-flutter-navigate-search-evcharginglocation-name">name</a></li><li><a href="sdk-for-flutter-navigate-search-evcharginglocation-openinghours">openingHours</a></li><li><a href="sdk-for-flutter-navigate-search-evcharginglocation-parkingtype">parkingType</a></li><li><a href="sdk-for-flutter-navigate-search-evcharginglocation-restrictions">restrictions</a></li><li><a href="sdk-for-flutter-navigate-search-evcharginglocation-runtimetype">runtimeType</a></li><li><a href="sdk-for-flutter-navigate-search-evcharginglocation-supportedvehicles">supportedVehicles</a></li><li><a href="sdk-for-flutter-navigate-search-evcharginglocation-supportphonenumber">supportPhoneNumber</a></li><li><a href="sdk-for-flutter-navigate-search-evcharginglocation-tariffs">tariffs</a></li><li><a href="sdk-for-flutter-navigate-search-evcharginglocation-timezone">timeZone</a></li><li><a href="sdk-for-flutter-navigate-search-evcharginglocation-truckrestrictions">truckRestrictions</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-search-evcharginglocation-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-search-evcharginglocation-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-search-evcharginglocation-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
