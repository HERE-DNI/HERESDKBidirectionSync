---
title: "VehicleRestriction class - transport library - Dart API"
slug: "sdk-for-flutter-navigate-transport-vehiclerestriction-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VehicleRestriction-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="transport/transport-library-sidebar.html" data-below-sidebar="transport/VehicleRestriction-class-sidebar.html">

<div>

# <span class="kind-class">VehicleRestriction</span> class

</div>

<div class="section desc markdown">

Represents a vehicle restriction.

Any non `null` property adds more details to the restriction. A general truck restriction is represented with `null` values for properties `restriction` and `hazmatRestriction`.

**Note:** This is a beta release of this feature. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclerestriction-vehiclerestriction">VehicleRestriction</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-restriction" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-specificrestriction-class">SpecificRestriction</a>?</span> <span class="parameter-name">restriction</span></span>)</span>  
Creates an unconditional restriction.

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclerestriction-vehiclerestriction-generalrestriction">VehicleRestriction.generalRestriction</a></span><span class="signature">()</span>  
Creates an uncoditional general restriction.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclerestriction-appliestodelivery">appliesToDelivery</a></span> <span class="signature">↔ bool</span>  
Flag indicating whether this restriction applies to delivery vehicles.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclerestriction-axlecount">axleCount</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-integerrange-class">IntegerRange</a>?</span>  
The axle count for which the current restriction applies. Can be used in conjunction with <a href="sdk-for-flutter-navigate-transport-restrictiontype">RestrictionType.weightPerAxleCount</a> to specify restriction based on weight per number of axles. The `axleCount` considers total number of axles on the whole vehicle (truck + trailers). This can be used to limit the weight per axle for the whole truck. If `axleCount` is null, the restriction is general and applies regardless of axle count. If the upper limit of the `axleCount` range is 0 or `null` then it means the restriction applies for values \>= lower limit, i.e. the upper limit of range if infinite or unbound. When a user taps the icon, the allowed `axleCount` range can be retrieved directly from `VehicleRestriction.axleCount`. Examples:

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclerestriction-axlecountingroup">axleCountInGroup</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-integerrange-class">IntegerRange</a>?</span>  
Number of axles in a group for which the current restriction applies. `axleCountInGroup` is a set of axles close together: single, tandem (2), triple (3), etc. Can be used in conjunction with <a href="sdk-for-flutter-navigate-transport-restrictiontype">RestrictionType.weightPerAxleGroup</a> to specify restriction based on weight per axle group. The `axleCountInGroup` considers number of axles in a specific axle group (usually rear axles on the truck or trailer). This can be used to limit weight for a tandem/triple rear axle group. If the upper limit of the `axleCountInGroup` range is 0 or `null` then it means the restriction applies for values \>= lower limit, i.e. the upper limit of range if infinite or unbound. Examples:

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclerestriction-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclerestriction-hazmatrestriction">hazmatRestriction</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-transport-hazardousmaterialrestriction-class">HazardousMaterialRestriction</a>?</span>  
Restriction on transport of hazardous materials and max allowed tunnel category. For example, (FLAMMABLE, TunnelCategory.D) means, a restriction applying for trucks carrying flammable materials are not allowed to enter tunnels category D and E - (TunnelCategory.B and TunnelCategory.C allowed).

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclerestriction-restriction">restriction</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-transport-specificrestriction-class">SpecificRestriction</a>?</span>  
A `SpecificRestriction` defines what type of restriction applies (weight, height, etc.) and the range of allowed values.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclerestriction-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclerestriction-timerestriction">timeRestriction</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-transport-timerestriction-class">TimeRestriction</a>?</span>  
Restriction applies during specific time.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclerestriction-trailercount">trailerCount</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-integerrange-class">IntegerRange</a>?</span>  
Number of trailers for which the restriction applies.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclerestriction-truckcategory">truckCategory</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-transport-truckcategory">TruckCategory</a>?</span>  
Restriction applies to a specific truck category.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclerestriction-weather">weather</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-weathertype">WeatherType</a>?</span>  
Type of weather in which restriction applies.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclerestriction-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclerestriction-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-transport-vehiclerestriction-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
