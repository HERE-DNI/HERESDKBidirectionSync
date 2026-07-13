---
title: "EVSEInfo class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-evseinfo-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EVSEInfo-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVSEInfo-class-sidebar.html">

<div>

# <span class="kind-class">EVSEInfo</span> class

</div>

<div class="section desc markdown">

Represents an EVSE at the charging point.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-search-evseinfo-evseinfo">EVSEInfo</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-search-evseinfo-capabilities">capabilities</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-ev-evsecapability">EVSECapability</a></span>\></span></span>  
Capabilities of the EVSE.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evseinfo-connectors">connectors</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-evchargingconnector-class">EVChargingConnector</a></span>\></span></span>  
List of available connectors on the EVSE. An operational EVSE should have at least one connector.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evseinfo-coordinates">coordinates</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>?</span>  
The geographic coordinates of the EVSE.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evseinfo-evseid">evseID</a></span> <span class="signature">↔ String?</span>  
Identifier compliant with the EVSE ID from eMI3 standard version V1.0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evseinfo-floorlevel">floorLevel</a></span> <span class="signature">↔ String?</span>  
Floor level on which the EVSE is located.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evseinfo-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evseinfo-id">id</a></span> <span class="signature">↔ String?</span>  
Human-readable globally unique identifier for the EVSE.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evseinfo-lastupdated">lastUpdated</a></span> <span class="signature">↔ DateTime</span>  
Timestamp when the status of this EVSE was last updated.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evseinfo-paymentsupports">paymentSupports</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-ev-evsepaymentsupport">EVSEPaymentSupport</a></span>\></span></span>  
List of payment support functionalities on EVSE for ad-hoc customers (without pre-registration).

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evseinfo-physicalreference">physicalReference</a></span> <span class="signature">↔ String?</span>  
A number or string printed on the outside of the EVSE for visual identification.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evseinfo-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evseinfo-status">status</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-ev-evsestate">EVSEState</a></span>  
Status of the EVSE.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evseinfo-uid">uid</a></span> <span class="signature">↔ String</span>  
Uniquely identifies the EVSE within the CPOs platform (and suboperator platforms). For example a database ID or the actual "EVSE ID". This field can never be changed, modified or renamed. This is the 'technical' identification of the EVSE, not to be used as 'human readable' identification, use the field <a href="sdk-for-flutter-navigate-search-evseinfo-id">EVSEInfo.id</a> for that.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-search-evseinfo-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evseinfo-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-search-evseinfo-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
