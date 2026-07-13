---
title: "RoadSignWarning class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-roadsignwarning-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoadSignWarning-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/RoadSignWarning-class-sidebar.html">

<div>

# <span class="kind-class">RoadSignWarning</span> class

</div>

<div class="section desc markdown">

A road sign.

The main field describing the sign is `RoadSignWarning.type`. Some road types are standardized, others can be country specific. A valid road sign contains known `RoadSignWarning.type` or `RoadSignWarning.category`. Use `RoadSignWarningListener` to get notifications with current road signs.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarning-roadsignwarning">RoadSignWarning</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-distanceToRoadSignInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">distanceToRoadSignInMeters</span>, </span><span id="sdk-for-flutter-navigate-param-type" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-roadsigntype">RoadSignType</a></span> <span class="parameter-name">type</span>, </span><span id="sdk-for-flutter-navigate-param-category" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-roadsigncategory">RoadSignCategory</a></span> <span class="parameter-name">category</span>, </span><span id="sdk-for-flutter-navigate-param-generalWarningType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-generalwarningroadsigntype">GeneralWarningRoadSignType</a></span> <span class="parameter-name">generalWarningType</span>, </span><span id="sdk-for-flutter-navigate-param-isPrioritySign" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isPrioritySign</span>, </span><span id="sdk-for-flutter-navigate-param-vehicleTypes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-roadsignvehicletype">RoadSignVehicleType</a></span>\></span></span> <span class="parameter-name">vehicleTypes</span>, </span><span id="sdk-for-flutter-navigate-param-weatherType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-weathertype">WeatherType</a></span> <span class="parameter-name">weatherType</span>, </span><span id="sdk-for-flutter-navigate-param-roadSignSegment" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-segmentreference-class">SegmentReference</a></span> <span class="parameter-name">roadSignSegment</span>, </span><span id="sdk-for-flutter-navigate-param-distanceType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span> <span class="parameter-name">distanceType</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarning-category">category</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-roadsigncategory">RoadSignCategory</a></span>  
The main category to which the road sign belongs.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarning-distancetoroadsigninmeters">distanceToRoadSignInMeters</a></span> <span class="signature">↔ double</span>  
Distance to the road sign in meters.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarning-distancetype">distanceType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span>  
The distance type for the warning, e.g. a warning for a new road sign ahead or a warning for passing a road sign. Since the road sign warning is given relative to a single position on the route, <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.reached</a> will never be given for this warning.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarning-duration">duration</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-localizedtext-class">LocalizedText</a>?</span>  
Optional length information during which the warning is applicable. Usually, this information is shown on a separate shield below the main shield. For example, a sign may warn on playing children for a length of 100 m, starting from the location of the warning sign. The length information (most likely with units) is given as printed on the local road sign.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarning-generalwarningtype">generalWarningType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-generalwarningroadsigntype">GeneralWarningRoadSignType</a></span>  
Specifies the general warning to which the road sign belongs.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarning-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarning-id">id</a></span> <span class="signature">↔ int</span>  
Unique identifier for this specific road sign warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarning-isprioritysign">isPrioritySign</a></span> <span class="signature">↔ bool</span>  
Flag indicating if the road sign is a priority sign.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarning-prewarning">preWarning</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-localizedtext-class">LocalizedText</a>?</span>  
Optional pre-warning in terms of distance, of the upcoming warning or regulation. The pre-warning information is given as printed on the local road sign.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarning-roadsignsegment">roadSignSegment</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-segmentreference-class">SegmentReference</a></span>  
The reference to the segment where the road sign is located. It can be used to identify the location of the road sign. It allows to compare the road sign location with the `MapMatchedLocation.segment_reference` provided by the `NavigableLocationListener` or with the <a href="sdk-for-flutter-navigate-routing-span-segmentreference">Span.segmentReference</a> available in the Route's Span. By combining it with the geometry of the segment, that can be loaded using <a href="sdk-for-flutter-navigate-mapdata-segmentdataloader-class">SegmentDataLoader</a>, it is possible to identify the road sign's coordinates.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarning-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarning-signvalue">signValue</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-localizedtext-class">LocalizedText</a>?</span>  
Optional value visible on the main sign related to specific road sign types, as it is printed on the local road sign.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarning-type">type</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-roadsigntype">RoadSignType</a></span>  
Type of the road sign.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarning-validitytime">validityTime</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-localizedtext-class">LocalizedText</a>?</span>  
Optional text visible on the supplemental sign indicating specific time(s) at which the road sign is applicable. The time information is given as printed on the local road sign.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarning-vehicletypes">vehicleTypes</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-roadsignvehicletype">RoadSignVehicleType</a></span>\></span></span>  
Specifies a list of vehicle types for which the road sign is applicable. The list will be empty when the road sign is applicable for all vehicles including cars.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarning-weathertype">weatherType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-weathertype">WeatherType</a></span>  
Specifies the weather type for which the sign is applicable. If weather type is `WeatherType.UNKNOWN`, the sign is actual for all weather types.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarning-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarning-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarning-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
