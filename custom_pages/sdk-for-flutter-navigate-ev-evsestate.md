---
title: "EVSEState enum - ev library - Dart API"
slug: "sdk-for-flutter-navigate-ev-evsestate"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EVSEState.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="ev/ev-library-sidebar.html" data-below-sidebar="ev/EVSEState-enum-sidebar.html">

<div>

# <span class="kind-enum">EVSEState</span> enum

</div>

<div class="section desc markdown">

Indicates the current short-term status of the EVSE at the time given in the modified property.

There are no separate statuses available for individual connectors. A single EVSE can only be used by a single car, so same statuses apply to other connectors as well. So, if one connector is in use, the whole EVSE has status charging, and other connectors cannot be used at the same time, hence they should be considered in-use as well. If an EVSE can allow multiple connectors to be used at the same time, it is basically multiple EVSEs merged into a single physical box or device.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Values

<span class="name">unknown</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-ev-evsestate">EVSEState</a></span>  
No status information available or the EVSE/connector is offline.

<span class="name">available</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-ev-evsestate">EVSEState</a></span>  
The EVSE/connector is able to start a new charging session.

<span class="name">blocked</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-ev-evsestate">EVSEState</a></span>  
The EVSE/connector is not accessible because of a physical barrier, i.e. a car.

<span class="name">charging</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-ev-evsestate">EVSEState</a></span>  
The EVSE/connector is in use.

<span class="name">inoperative</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-ev-evsestate">EVSEState</a></span>  
The EVSE/connector is temporarily not available for use, but not broken or defect.

<span class="name">outOfOrder</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-ev-evsestate">EVSEState</a></span>  
The EVSE/connector is currently out of order.

<span class="name">reserved</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-ev-evsestate">EVSEState</a></span>  
The EVSE/connector is reserved for a particular EV driver and is unavailable for other drivers.

<span class="name">operational</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-ev-evsestate">EVSEState</a></span>  
The EVSE/connector was operational when checked the last time, but the actual latest status is not available at the moment.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-ev-evsestate-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-ev-evsestate-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-ev-evsestate-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-ev-evsestate-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-ev-evsestate-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-ev-evsestate-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-ev-evsestate-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-ev-evsestate">EVSEState</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
