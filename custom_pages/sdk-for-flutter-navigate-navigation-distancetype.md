---
title: "DistanceType enum - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-distancetype"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- DistanceType.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/DistanceType-enum-sidebar.html">

<div>

# <span class="kind-enum">DistanceType</span> enum

</div>

<div class="section desc markdown">

**Note:** The distance types are being given for warnings at distances which can be configured via options specific for each warner.

These distances are defined based on the `sdk.navigation.TimingProfile` calculated based on the speed limit present at the driver's current location. Indicates the distance type for a warning.

</div>

## Values

<span class="name">ahead</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span>  
The warning is given for the first time for a new warner data ahead. In case the distance to the warner data is 0, then a warning with distance type <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.reached</a> will also be given at the same moment.

<span class="name">passed</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span>  
The warning is given when a warner data was passed.

<span class="name">reached</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span>  
The warning is given when a warner data was reached. In case the distance to the warner data is 0 when the warning with distance type <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.ahead</a> is given, then a warning with distance type <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.reached</a> will be given at the same moment.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-distancetype-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-distancetype-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-distancetype-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-distancetype-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-distancetype-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-distancetype-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-navigation-distancetype-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
