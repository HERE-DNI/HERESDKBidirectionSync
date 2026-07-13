---
title: "PlaceFilterEv class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-placefilterev-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/PlaceFilterEv-class-sidebar.html">

<div>

# <span class="kind-class">PlaceFilterEv</span> class

</div>

<div class="section desc markdown">

Constraints that are applicable on the places of category EV station.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-search-placefilterev-placefilterev">PlaceFilterEv</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-search-placefilterev-connectortypeids">connectorTypeIDs</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span>  
Filter to retrieve EV charging stations with at least one of the connector type IDs. For more information on the current connector types, see <https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-placefilterev-currenttype">currentType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-currenttype">CurrentType</a>?</span>  
Filter to retrieve EV charging stations with the given current type provided at one of the station EVSE. Accepted is either AC or DC. Not supported for `suggestByText` in `OfflineSearchEngine` (only available for the Navigate license).

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-placefilterev-emobilityserviceproviderpartnerids">eMobilityServiceProviderPartnerIDs</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span>  
Filter to retrieve EV charging stations with at least one matching e-Mobility Service Provider Partner ID.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-placefilterev-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-placefilterev-minpowerinkilowatts">minPowerInKilowatts</a></span> <span class="signature">↔ double?</span>  
Filter to retrieve EV charging stations with the given minimum charging power in KW delivered by at least one of the station EVSE. Not supported for `suggestByText` in `OfflineSearchEngine` (only available for the Navigate license).

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-placefilterev-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-placefilterev-suppliernames">supplierNames</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span>  
Sets a constraint on the charge point operator name of the EV station.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-search-placefilterev-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-placefilterev-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-search-placefilterev-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

