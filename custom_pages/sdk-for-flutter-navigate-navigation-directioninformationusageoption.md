---
title: "DirectionInformationUsageOption enum - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-directioninformationusageoption"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/DirectionInformationUsageOption-enum-sidebar.html">

<div>

# <span class="kind-enum">DirectionInformationUsageOption</span> enum

</div>

<div class="section desc markdown">

Indicates the option of direction information included in the notification.

</div>

## Values

<span class="name">none</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-navigation-directioninformationusageoption">DirectionInformationUsageOption</a></span>  
No direction information is included in the notification. **Example:** 'Now turn left to join the highway.'.

<span class="name">roadInformationOnly</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-navigation-directioninformationusageoption">DirectionInformationUsageOption</a></span>  
Road information (either street name or road number based on the maneuver action) is included in the notification, if available. Street name is included mainly for non-highway-related maneuver, whilst road number is included in case of highway-related maneuver. **Example:** 'Now turn left to join the I-83 South.'.

<span class="name">roadInformationAndSignpostDirection</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-navigation-directioninformationusageoption">DirectionInformationUsageOption</a></span>  
Both Road information (either street name or road number based on the maneuver action) and signpost direction are included in the notification, or either one, if available. Street name is included mainly for non-highway-related maneuver, whilst road number is included in case of highway-related maneuver. **Example:** 'Now turn left to join the I-83 South towards Baltimore.'.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-directioninformationusageoption-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-directioninformationusageoption-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-directioninformationusageoption-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-directioninformationusageoption-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-directioninformationusageoption-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-directioninformationusageoption-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-navigation-directioninformationusageoption-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-directioninformationusageoption">DirectionInformationUsageOption</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

