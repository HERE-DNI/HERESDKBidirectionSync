---
title: "BorderCrossingWarning class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-bordercrossingwarning-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- BorderCrossingWarning-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/BorderCrossingWarning-class-sidebar.html">

<div>

# <span class="kind-class">BorderCrossingWarning</span> class

</div>

<div class="section desc markdown">

A border crossing.

The main field describing the border crossing is `BorderCrossingWarning.type` specifying whether the border crossing is given for a country border or a state border. The `BorderCrossingWarning.type` must be known. The country and state codes are contained in `BorderCrossingWarning.administrativeRules` along with other information such as speed limits, u-turn regulations or pre-trip planning information contained by the <a href="sdk-for-flutter-navigate-mapdata-administrativerules-class">AdministrativeRules</a>.

Use `BorderCrossingWarningListener` to get notifications about upcoming country or state border crossings.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-bordercrossingwarning">BorderCrossingWarning</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-distanceToBorderCrossingInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">distanceToBorderCrossingInMeters</span>, </span><span id="sdk-for-flutter-navigate-param-type" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-bordercrossingtype">BorderCrossingType</a></span> <span class="parameter-name">type</span>, </span><span id="sdk-for-flutter-navigate-param-administrativeRules" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-administrativerules-class">AdministrativeRules</a></span> <span class="parameter-name">administrativeRules</span>, </span><span id="sdk-for-flutter-navigate-param-distanceType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span> <span class="parameter-name">distanceType</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-administrativerules">administrativeRules</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-mapdata-administrativerules-class">AdministrativeRules</a></span>  
The administrative rules for the country or state after the border crossing. It contains information regarding rules such as driving side, speed limits, various sticker requirements, toll costs and others.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-commercialvehicleregulations">commercialVehicleRegulations</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-mapdata-administrativecommercialvehiclerules-class">AdministrativeCommercialVehicleRules</a>?</span>  
Commercial vehicle regulations for the administrative region after the border crossing. Contains access restrictions, speed limits, and drive/rest rules applicable to commercial vehicles. This field is only populated when crossing into a region with specific commercial vehicle regulations.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-distancetobordercrossinginmeters">distanceToBorderCrossingInMeters</a></span> <span class="signature">↔ double</span>  
Distance to the border crossing in meters.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-distancetype">distanceType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span>  
The distance type for the warning, e.g. a warning for a new border crossing ahead or a warning for passing a border crossing. Since the border crossing warning is given relative to a single position on the route, <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.reached</a> will never be given for this warning.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-id">id</a></span> <span class="signature">↔ int</span>  
Unique identifier for this specific border crossing warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-type">type</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-bordercrossingtype">BorderCrossingType</a></span>  
Type of border crossing.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
