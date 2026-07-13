---
title: "EVChargingPool class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-evchargingpool-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EVChargingPool-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVChargingPool-class-sidebar.html">

<div>

# <span class="kind-class">EVChargingPool</span> class

</div>

<div class="section desc markdown">

A charging pool for electric vehicles is an area equipped with one or more charging stations.

Use <a href="sdk-for-flutter-navigate-search-placecategory-businessandservicesevchargingstation">PlaceCategory.businessAndServicesEvChargingStation</a> to find stations. In the `Details` of a `Place` result you can find the list of found pools containing stations, if any.

For offline EV rich attributes, also enable <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.ev</a> in <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-layerconfiguration">SDKOptions.layerConfiguration</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingpool-evchargingpool">EVChargingPool</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-chargingStations" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-evchargingstation-class">EVChargingStation</a></span>\></span></span> <span class="parameter-name">chargingStations</span>, </span><span id="sdk-for-flutter-navigate-param-eMobilityServiceProviders" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-emobilityserviceprovider-class">EMobilityServiceProvider</a></span>\></span></span> <span class="parameter-name">eMobilityServiceProviders</span>, </span><span id="sdk-for-flutter-navigate-param-accessRestrictionReasons" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-evaccessrestrictionreason">EVAccessRestrictionReason</a></span>\></span></span> <span class="parameter-name">accessRestrictionReasons</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingpool-access">access</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-search-evaccesstype">EVAccessType</a>?</span>  
The accessibility level of the charging pool, or `null` if unknown.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingpool-accessrestrictionreasons">accessRestrictionReasons</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-evaccessrestrictionreason">EVAccessRestrictionReason</a></span>\></span></span>  
Contains the list of reasons for restriction. Populated only for offline search and when access is <a href="sdk-for-flutter-navigate-search-evaccesstype">EVAccessType.restrictedAccess</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingpool-chargingstations">chargingStations</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-evchargingstation-class">EVChargingStation</a></span>\></span></span>  
List of charging stations.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingpool-cpoid">cpoId</a></span> <span class="signature">↔ String?</span>  
CPO (Charge Point Operator) id for charging pool. Only online search fills this field.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingpool-details">details</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-search-evchargingpooldetails-class">EVChargingPoolDetails</a>?</span>  
EV charging station attributes details. It is available only for a place that has charging station for electric vehicles. Only offline search fills this field.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingpool-emobilityserviceproviders">eMobilityServiceProviders</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-emobilityserviceprovider-class">EMobilityServiceProvider</a></span>\></span></span>  
List of e-Mobility Service Providers. Only online search fills this field.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingpool-evseinfo">evseInfo</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-evse-class">Evse</a></span>\></span></span>  
Charge Point Operator (CPO) ID uses the Electric Vehicle Supply Equipment ID (EVSE ID) for an exact identification of the charging infrastructure and charging point. Only online search fills this field.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingpool-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingpool-id">id</a></span> <span class="signature">↔ String?</span>  
HERE ID of the charging pool. Only online search fills this field.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingpool-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingpool-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingpool-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingpool-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
