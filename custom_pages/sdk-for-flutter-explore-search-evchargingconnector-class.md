---
title: "EVChargingConnector class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-evchargingconnector-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVChargingConnector-class-sidebar.html">

<div>

# <span class="kind-class">EVChargingConnector</span> class

</div>

<div class="section desc markdown">

Represents a connector at the charging point.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnector-evchargingconnector">EVChargingConnector</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnector-connectortype">connectorType</a></span> <span class="signature">↔ String</span>  
Standardized type of the connector. Should be one of the constants defined in <a href="sdk-for-flutter-explore-ev-evchargingconnectortype-class">EVChargingConnectorType</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnector-format">format</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-ev-evchargingconnectorformat">EVChargingConnectorFormat</a></span>  
Format of the connector, whether it is a socket or a cable.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnector-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnector-id">id</a></span> <span class="signature">↔ String</span>  
Identifier of the connector within the EVSE.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnector-maxcurrentinamperes">maxCurrentInAmperes</a></span> <span class="signature">↔ int</span>  
Max current (in amperes) of the connector.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnector-maxpowerinwatts">maxPowerInWatts</a></span> <span class="signature">↔ int?</span>  
Max power (in watts) of the connector, if available. This should be set when the maximum electric power is lower than the calculated value from voltage and amperage.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnector-maxvoltageinvolts">maxVoltageInVolts</a></span> <span class="signature">↔ int</span>  
Max voltage (in volts) of the connector.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnector-powertype">powerType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-core-powertype">PowerType</a></span>  
Type of electrical power used by the connector.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnector-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnector-tariffindexes">tariffIndexes</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span>  
Tariffs for the connector, presented by indexes to the charging station's tariffs-list. Available only if `EVChargingLocationFeature.TARIFFS` is included in `EVSearchOptions.additional_features`, otherwise empty.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnector-termsandconditionsurl">termsAndConditionsUrl</a></span> <span class="signature">↔ String?</span>  
URL to the operator’s terms and conditions, if available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnector-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnector-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingconnector-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

