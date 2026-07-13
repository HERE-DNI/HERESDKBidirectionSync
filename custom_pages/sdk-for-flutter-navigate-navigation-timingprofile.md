---
title: "TimingProfile enum - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-timingprofile"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TimingProfile.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/TimingProfile-enum-sidebar.html">

<div>

# <span class="kind-enum">TimingProfile</span> enum

</div>

<div class="section desc markdown">

Identifies the timing profile used for emitting notifications and warnings.

</div>

## Values

<span class="name">slowSpeed</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a></span>  
Timing profile used when the speed is slow. This timing profile is applied for speed limits or speeds greater than 0 meters/second but slower or equal to 16.39 meters/second (aproximately 60 kilometers/hour). There is also an additional check if the area is built up and if it is, the timing profile is also considerd as `SLOW_SPEED` regardless of the speed limit or the current speed.

<span class="name">regularSpeed</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a></span>  
Timing profile used when the speed is regular. This timing profile is applied for speed limits or speeds greater than 16.39 meters/second (aproximately 60 kilometer/hour) but slower or equal to 27.78 meters/second (aproximately 100 kilometer/hour).

<span class="name">fastSpeed</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a></span>  
Timing profile used when the speed is fast. This timing profile is applied for speed limits or speeds greater than 27.78 meters/second (aproximately 100 kilometer/hour) or no speed limits.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-timingprofile-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-timingprofile-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-timingprofile-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-timingprofile-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-timingprofile-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-timingprofile-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-navigation-timingprofile-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
