---
title: "TruckRestrictionWarning class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-truckrestrictionwarning-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TruckRestrictionWarning-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/TruckRestrictionWarning-class-sidebar.html">

<div>

# <span class="kind-class">TruckRestrictionWarning</span> class

</div>

<div class="section desc markdown">

Represents truck restrictions.

For example, there can be a bridge ahead not high enough to pass a big truck or there can be a road ahead where the truck’s weight exceeds the permissible limit.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-truckrestrictionwarning">TruckRestrictionWarning</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-distanceInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">distanceInMeters</span>, </span><span id="sdk-for-flutter-navigate-param-distanceType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span> <span class="parameter-name">distanceType</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-axlecount">axleCount</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-integerrange-class">IntegerRange</a>?</span>  
The axle count for which the current restriction applies. If this field is `null`, the restriction does not depend on axle count.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-dimensionrestriction">dimensionRestriction</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-dimensionrestriction-class">DimensionRestriction</a>?</span>  
Vehicle dimension restrictions. It is `null` when there is no known dimension restriction ahead.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-distanceinmeters">distanceInMeters</a></span> <span class="signature">↔ double</span>  
The distance from the current location to the restriction.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-distancetype">distanceType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span>  
Indicates if the specified truck restriction is ahead of the vehicle or has just passed by. If it is ahead, then <a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-distanceinmeters">TruckRestrictionWarning.distanceInMeters</a> is greater than 0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-hazardousmaterials">hazardousMaterials</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-transport-hazardousmaterial">HazardousMaterial</a></span>\></span></span>  
The list of hazardous materials which are restricted on the road section for which the warning applies.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-id">id</a></span> <span class="signature">↔ int</span>  
Unique identifier for this specific truck restriction warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-timerule">timeRule</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-timerule-class">TimeRule</a>?</span>  
Time rule indicating the time periods for which the restriction applies. If the field is 'null' then the restriction is applicable at anytime.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-trailercount">trailerCount</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-integerrange-class">IntegerRange</a>?</span>  
The trailer count for which the current restriction applies. If the field is 'null' then the current restriction does not have a condition based on trailers count.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-truckroadtype">truckRoadType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-transport-truckroadtype">TruckRoadType</a>?</span>  
Truck road type restriction.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-tunnelcategory">tunnelCategory</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory</a>?</span>  
Tunnel category.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-weightrestriction">weightRestriction</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-weightrestriction-class">WeightRestriction</a>?</span>  
Weight restriction. It is `null` when there is no known weight restriction ahead.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-isgeneral">isGeneral</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ bool</span> </span>  
Checks if this truck restriction warning is general.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
