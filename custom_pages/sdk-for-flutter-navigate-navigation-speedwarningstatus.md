---
title: "SpeedWarningStatus enum - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-speedwarningstatus"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SpeedWarningStatus.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/SpeedWarningStatus-enum-sidebar.html">

<div>

# <span class="kind-enum">SpeedWarningStatus</span> enum

</div>

<div class="section desc markdown">

This enum represents the status of the speed warning feature.

</div>

## Values

<span class="name">speedLimitExceeded</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-navigation-speedwarningstatus">SpeedWarningStatus</a></span>  
Status when the current speed exceeded the speed limit (plus offset) for the current road segment. This status is followed by <a href="sdk-for-flutter-navigate-navigation-speedwarningstatus">SpeedWarningStatus.speedLimitRestored</a> once the driving speed is again below the speed limit (plus offset) for the current road segment.

**Note:** The speed limit used to check this condition does not take into account any temporary special speed limit. See `SpeedLimitListener`.

<span class="name">speedLimitRestored</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-navigation-speedwarningstatus">SpeedWarningStatus</a></span>  
Status where the current speed is again below the speed limit (plus offset) for the current road segment. This status is only possible after previously exceeding a speed limit.

**Note:** The speed limit used to check this condition does not take into account any temporary special speed limit. See \`SpeedLimitListener.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedwarningstatus-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedwarningstatus-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedwarningstatus-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedwarningstatus-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedwarningstatus-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedwarningstatus-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedwarningstatus-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-speedwarningstatus">SpeedWarningStatus</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
