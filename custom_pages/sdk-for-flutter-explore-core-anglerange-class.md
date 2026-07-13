---
title: "AngleRange class - core library - Dart API"
slug: "sdk-for-flutter-explore-core-anglerange-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/AngleRange-class-sidebar.html">

<div>

# <span class="kind-class">AngleRange</span> class

</div>

<div class="section desc markdown">

Represents angle ranges as a circular sector by using an absolute start angle and a relative range angle called extent.

They both define a sector on a circle. All angles are in degrees and are clockwise-oriented. By default, the AngleRange represents the entire circle, the value is in the range of \[0, 360\]. Values will be corrected during construction using normalization for the start angle and clamping for the extent angle, ensuring a valid range for all possible inputs.

</div>

<div class="section">

Annotations  
- @<a href="https://pub.dev/documentation/meta/1.17.0/meta/immutable-constant.html">immutable</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-core-anglerange-anglerange">AngleRange</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-start" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">start</span>, </span><span id="sdk-for-flutter-explore-param-extent" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">extent</span></span>)</span>  
Constructs an AngleRange from the provided start and extent angles.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-anglerange-anglerange-fullcircle">AngleRange.fullCircle</a></span><span class="signature">()</span>  
Constructs a range covering a full circle.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-core-anglerange-extent">extent</a></span> <span class="signature">→ double</span>  
The angle range extent, running clockwise, in degrees from start. The value is in the range of \[0, 360\] degrees.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-anglerange-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-anglerange-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-anglerange-start">start</a></span> <span class="signature">→ double</span>  
Start angle, running clockwise, in degrees from north. The value is in the range of \<a href="sdk-for-flutter-explore-core-anglerange-closestinrange">0, 360) degrees.

<div class="features">

<span class="feature">final</span>

</div>

## Methods

<span class="name">[closestInRange</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-closestInRange-param-angleClockwiseInDegreesFromNorth" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">angleClockwiseInDegreesFromNorth</span></span>) <span class="returntype parameter">→ double</span> </span>  
Get the angle that is closest to the given one and in range.

<span class="name"><a href="sdk-for-flutter-explore-core-anglerange-inrange">inRange</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-inRange-param-angleClockwiseInDegreesFromNorth" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">angleClockwiseInDegreesFromNorth</span></span>) <span class="returntype parameter">→ bool</span> </span>  
Check if a given angle in degrees, clockwise from north is in range or not.

<span class="name"><a href="sdk-for-flutter-explore-core-anglerange-max">max</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ double</span> </span>  
Get the maximum angle defined by the range in degrees, clockwise from north, normalized to \<a href="sdk-for-flutter-explore-core-anglerange-nosuchmethod">0,360).

<span class="name">[noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-anglerange-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-core-anglerange-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

## Static Methods

<span class="name"><a href="sdk-for-flutter-explore-core-anglerange-fromdirectiondegreesclockwise">fromDirectionDegreesClockwise</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-fromDirectionDegreesClockwise-param-center" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">center</span>, </span><span id="sdk-for-flutter-explore-fromDirectionDegreesClockwise-param-extent" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">extent</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-anglerange-class">AngleRange</a></span> </span>  
Constructs an AngleRange from the provided center angle defining the direction and an angular width to extent the range by 50% clockwise and 50% counter-clockwise from its center angle.

<span class="name"><a href="sdk-for-flutter-explore-core-anglerange-fromminmaxdegreesclockwise">fromMinMaxDegreesClockwise</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-fromMinMaxDegreesClockwise-param-min" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">min</span>, </span><span id="sdk-for-flutter-explore-fromMinMaxDegreesClockwise-param-max" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">max</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-anglerange-class">AngleRange</a></span> </span>  
Constructs an AngleRange from the provided minimum and maximum angles.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

