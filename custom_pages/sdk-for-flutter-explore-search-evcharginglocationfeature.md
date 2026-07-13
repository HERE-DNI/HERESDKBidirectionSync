---
title: "EVChargingLocationFeature enum - search library - Dart API"
slug: "sdk-for-flutter-explore-search-evcharginglocationfeature"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVChargingLocationFeature-enum-sidebar.html">

<div>

# <span class="kind-enum">EVChargingLocationFeature</span> enum

</div>

<div class="section desc markdown">

Optional features that can be requested for EV charging locations.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Values

<span class="name">evses</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-search-evcharginglocationfeature">EVChargingLocationFeature</a></span>  
<a href="sdk-for-flutter-explore-search-evcharginglocation-evses">EVChargingLocation.evses</a> will be returned. If <a href="sdk-for-flutter-explore-search-evcharginglocationfeature">EVChargingLocationFeature.connectorGroups</a> is also included, then <a href="sdk-for-flutter-explore-search-evchargingconnectorgroup-connectors">EVChargingConnectorGroup.connectors</a> will also be returned.

<span class="name">truckRestrictions</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-search-evcharginglocationfeature">EVChargingLocationFeature</a></span>  
<a href="sdk-for-flutter-explore-search-evcharginglocation-truckrestrictions">EVChargingLocation.truckRestrictions</a> will be returned.

<span class="name">locationInfo</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-search-evcharginglocationfeature">EVChargingLocationFeature</a></span>  
<a href="sdk-for-flutter-explore-search-evcharginglocation-cpoid">EVChargingLocation.cpoID</a>, <a href="sdk-for-flutter-explore-search-evcharginglocation-facilitytypes">EVChargingLocation.facilityTypes</a>, <a href="sdk-for-flutter-explore-search-evcharginglocation-parkingtype">EVChargingLocation.parkingType</a>, <a href="sdk-for-flutter-explore-search-evcharginglocation-energymix">EVChargingLocation.energyMix</a>, and <a href="sdk-for-flutter-explore-search-evcharginglocation-openinghours">EVChargingLocation.openingHours</a> will be returned.

<span class="name">emsps</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-search-evcharginglocationfeature">EVChargingLocationFeature</a></span>  
<a href="sdk-for-flutter-explore-search-evcharginglocation-emobilityserviceproviders">EVChargingLocation.eMobilityServiceProviders</a> will be returned.

<span class="name">connectorGroups</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-search-evcharginglocationfeature">EVChargingLocationFeature</a></span>  
<a href="sdk-for-flutter-explore-search-evcharginglocation-connectorgroups">EVChargingLocation.connectorGroups</a> will be returned. To ensure <a href="sdk-for-flutter-explore-search-evchargingconnectorgroup-connectors">EVChargingConnectorGroup.connectors</a> is available, also include <a href="sdk-for-flutter-explore-search-evcharginglocationfeature">EVChargingLocationFeature.evses</a>. To ensure <a href="sdk-for-flutter-explore-search-evchargingconnectorgroup-tariffindexes">EVChargingConnectorGroup.tariffIndexes</a> is available, also include <a href="sdk-for-flutter-explore-search-evcharginglocationfeature">EVChargingLocationFeature.tariffs</a>.

<span class="name">tariffs</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-search-evcharginglocationfeature">EVChargingLocationFeature</a></span>  
<a href="sdk-for-flutter-explore-search-evchargingconnectorgroup-tariffindexes">EVChargingConnectorGroup.tariffIndexes</a> will be returned. Ignored if neither <a href="sdk-for-flutter-explore-search-evcharginglocationfeature">EVChargingLocationFeature.evses</a> nor <a href="sdk-for-flutter-explore-search-evcharginglocationfeature">EVChargingLocationFeature.connectorGroups</a> are included.

<span class="name">nearby</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-search-evcharginglocationfeature">EVChargingLocationFeature</a></span>  
<a href="sdk-for-flutter-explore-search-evcharginglocation-facilitytypes">EVChargingLocation.facilityTypes</a> will be returned.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-search-evcharginglocationfeature-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evcharginglocationfeature-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evcharginglocationfeature-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-search-evcharginglocationfeature-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evcharginglocationfeature-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-search-evcharginglocationfeature-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-explore-search-evcharginglocationfeature-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-evcharginglocationfeature">EVChargingLocationFeature</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

