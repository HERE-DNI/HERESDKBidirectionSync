---
title: "SectionProgress class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-sectionprogress-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SectionProgress-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/SectionProgress-class-sidebar.html">

<div>

# <span class="kind-class">SectionProgress</span> class

</div>

<div class="section desc markdown">

Indicates a user's progress along a <a href="sdk-for-flutter-navigate-routing-section-class">Section</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-sectionprogress-sectionprogress">SectionProgress</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-sectionprogress-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-sectionprogress-remainingdistanceinmeters">remainingDistanceInMeters</a></span> <span class="signature">↔ int</span>  
The distance in meters from current location until the end of the <a href="sdk-for-flutter-navigate-routing-section-class">Section</a>. Note that the value is accumulated per section, and that the last section contains the overall distance to the destination. Defaults to 0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-sectionprogress-remainingduration">remainingDuration</a></span> <span class="signature">↔ Duration</span>  
The estimated time in seconds from current location until the end of the <a href="sdk-for-flutter-navigate-routing-section-class">Section</a> is reached, including traffic delays if available. Note that the value is accumulated per section, and that the last section contains the overall duration until the destination is reached. Defaults to 0 seconds.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-sectionprogress-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-sectionprogress-trafficdelay">trafficDelay</a></span> <span class="signature">↔ Duration</span>  
The estimated traffic delay in seconds from current location until the end of the <a href="sdk-for-flutter-navigate-routing-section-class">Section</a> is reached. Note that the value is accumulated per section, and that the last section contains the overall traffic delay until the destination is reached. The delay might be a negative value: Negative values indicate that the part of this section can be traversed faster than usual. Note that this is based on a delay value received at the moment of route calculation. Defaults to 0 seconds.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-sectionprogress-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-sectionprogress-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-sectionprogress-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
