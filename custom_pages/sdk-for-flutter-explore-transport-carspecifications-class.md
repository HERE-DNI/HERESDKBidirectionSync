---
title: "CarSpecifications class - transport library - Dart API"
slug: "sdk-for-flutter-explore-transport-carspecifications-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="transport/transport-library-sidebar.html" data-below-sidebar="transport/CarSpecifications-class-sidebar.html">

<div>

# <span class="kind-class">CarSpecifications</span> class

</div>

<div class="section desc markdown">

Car specifications contain vehicle related attributes.

Examples: Dimensions, weight, axle count. Only the fields that are set are considered for restriction handling.

</div>

<div class="section">

Annotations  
- @Deprecated("Will be removed in v4.28.0. Use \`TransportSpecification\` instead.")

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-transport-carspecifications-carspecifications">CarSpecifications</a></span><span class="signature">(\[<span id="sdk-for-flutter-explore-param-grossWeightInKilograms" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">grossWeightInKilograms</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-explore-param-heightInCentimeters" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">heightInCentimeters</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-explore-param-widthInCentimeters" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">widthInCentimeters</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-explore-param-lengthInCentimeters" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">lengthInCentimeters</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-explore-param-axleCount" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">axleCount</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-explore-param-trailerCount" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">trailerCount</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-explore-param-trailerAxleCount" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">trailerAxleCount</span> = <span class="default-value">null</span></span>\])</span>  
Creates a new instance.

<span class="name"><a href="sdk-for-flutter-explore-transport-carspecifications-carspecifications-withdefaults">CarSpecifications.withDefaults</a></span><span class="signature">()</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-transport-carspecifications-axlecount">axleCount</a></span> <span class="signature">↔ int?</span>  
Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2. By default, it is not set. Route calculation: When not set, possible axle count restrictions will not be taken into consideration. When specifying <a href="sdk-for-flutter-explore-transport-carspecifications-traileraxlecount">CarSpecifications.trailerAxleCount</a>, then <a href="sdk-for-flutter-explore-transport-carspecifications-axlecount">CarSpecifications.axleCount</a> is required and must be greater than <a href="sdk-for-flutter-explore-transport-carspecifications-traileraxlecount">CarSpecifications.trailerAxleCount</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-carspecifications-grossweightinkilograms">grossWeightInKilograms</a></span> <span class="signature">↔ int?</span>  
Car weight including trailers and shipped goods in kilograms. The provided value must be greater than or equal to 0. By default, it is not set. **Note:** This parameter is limited to a maximum weight of 4250 kg without trailer and 7550 kg with trailer.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-carspecifications-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-carspecifications-heightincentimeters">heightInCentimeters</a></span> <span class="signature">↔ int?</span>  
Car height in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-carspecifications-lengthincentimeters">lengthInCentimeters</a></span> <span class="signature">↔ int?</span>  
Car length in centimeters. The provided value must be in the range \[0, 30000\]. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-carspecifications-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-carspecifications-traileraxlecount">trailerAxleCount</a></span> <span class="signature">↔ int?</span>  
Defines total number of axles across all the trailers attached to the vehicle. This number is included in <a href="sdk-for-flutter-explore-transport-carspecifications-axlecount">CarSpecifications.axleCount</a>, hence <a href="sdk-for-flutter-explore-transport-carspecifications-traileraxlecount">CarSpecifications.trailerAxleCount</a> must be less than <a href="sdk-for-flutter-explore-transport-carspecifications-axlecount">CarSpecifications.axleCount</a> and greater than or equal to 1. <a href="sdk-for-flutter-explore-transport-carspecifications-axlecount">CarSpecifications.axleCount</a> and <a href="sdk-for-flutter-explore-transport-carspecifications-trailercount">CarSpecifications.trailerCount</a> are required to specify <a href="sdk-for-flutter-explore-transport-carspecifications-traileraxlecount">CarSpecifications.trailerAxleCount</a>. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-carspecifications-trailercount">trailerCount</a></span> <span class="signature">↔ int?</span>  
Defines number of trailers attached to the vehicle. The provided value must be in the range \[0, 1\]. By default, it is not set. When specifying <a href="sdk-for-flutter-explore-transport-carspecifications-traileraxlecount">CarSpecifications.trailerAxleCount</a>, then <a href="sdk-for-flutter-explore-transport-carspecifications-trailercount">CarSpecifications.trailerCount</a> is required and must be greater than 0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-carspecifications-widthincentimeters">widthInCentimeters</a></span> <span class="signature">↔ int?</span>  
Car width in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-transport-carspecifications-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-transport-carspecifications-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-transport-carspecifications-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

