---
title: "EVChargingConnectorGroup class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-evchargingconnectorgroup-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVChargingConnectorGroup-class-sidebar.html">

<div>

# <span class="kind-class">EVChargingConnectorGroup</span> class

</div>

<div class="section desc markdown">

Represents the connector group at the charging location.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnectorgroup-evchargingconnectorgroup">EVChargingConnectorGroup</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnectorgroup-availableconnectorcount">availableConnectorCount</a></span> <span class="signature">↔ int?</span>  
Number of connectors available for use at the time of query. The field is not present if the availability is not known.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnectorgroup-connectorcount">connectorCount</a></span> <span class="signature">↔ int</span>  
Number of connectors in the group. If an EVSE has multiple identical connectors they are counted as one as only one is accessible at a time.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnectorgroup-connectors">connectors</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-evchargingconnectorreference-class">EVChargingConnectorReference</a></span>\></span></span>  
Array of EVSE + connector(s) pairs that belong to the group. Provides access to EVSE statuses and more detailed connector characteristics. Available only if `EVChargingLocationFeature.EVSES` is included in `EVSearchOptions.additional_features`, otherwise empty.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnectorgroup-connectortype">connectorType</a></span> <span class="signature">↔ String</span>  
The standard (type) of the connectors belonging to this group. Should be one of the constants defined in <a href="sdk-for-flutter-explore-ev-evchargingconnectortype-class">EVChargingConnectorType</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnectorgroup-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnectorgroup-maxpowerinwatts">maxPowerInWatts</a></span> <span class="signature">↔ int</span>  
Maximum power that can be delivered by the connectors, in watts (W). Connectors without max power are not grouped.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnectorgroup-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnectorgroup-tariffindexes">tariffIndexes</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span>  
Tariffs for the connector group, represented by indexes to the charging station's tariffs-list. Available only if `EVChargingLocationFeature.TARIFFS` is included in `EVSearchOptions.additional_features`, otherwise empty.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnectorgroup-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnectorgroup-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnectorgroup-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

