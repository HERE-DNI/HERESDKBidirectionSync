---
title: "LaneDecreaseWarning class - warner library - Dart API"
slug: "sdk-for-flutter-navigate-warner-lanedecreasewarning-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LaneDecreaseWarning-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="warner/warner-library-sidebar.html" data-below-sidebar="warner/LaneDecreaseWarning-class-sidebar.html">

<div>

# <span class="kind-class">LaneDecreaseWarning</span> class

</div>

<div class="section desc markdown">

Represents a lane decrease warning that notifies about upcoming reductions in the number of available lanes.

Lane decrease warnings are generated when the road ahead has fewer lanes than the previous road segment provided by `sdk.electronic_horizon.ElectronicHorizonEngine`, requiring drivers to merge or change lanes. Lane decrease is provided only on highways and motorways. It will not be provided for junctions, when maneuver is given for the lane decrease situation or when the <a href="sdk-for-flutter-navigate-navigation-trafficmergewarning-class">TrafficMergeWarning</a> is provided. Special lanes (e.g. Bus lane, HOV) will only be included to the lane decrease warning generation if the according options are set in <a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a>.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-warner-lanedecreasewarning-lanedecreasewarning">LaneDecreaseWarning</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-distanceInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">distanceInMeters</span>, </span><span id="sdk-for-flutter-navigate-param-distanceType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span> <span class="parameter-name">distanceType</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-warner-lanedecreasewarning-distanceinmeters">distanceInMeters</a></span> <span class="signature">↔ double</span>  
The distance from the current location to the Lane decrease event.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-warner-lanedecreasewarning-distancetype">distanceType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span>  
Indicates if the specified event is ahead of the vehicle or has just passed by. If it is ahead, then <a href="sdk-for-flutter-navigate-warner-lanedecreasewarning-distanceinmeters">LaneDecreaseWarning.distanceInMeters</a> is greater than 0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-warner-lanedecreasewarning-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-warner-lanedecreasewarning-id">id</a></span> <span class="signature">↔ int</span>  
Unique identifier for this lane decrease warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-warner-lanedecreasewarning-lanesdecreasedfromleft">lanesDecreasedFromLeft</a></span> <span class="signature">↔ int?</span>  
Number of lanes decreased on the left side of the road, `null` if the left-side change is unknown or not applicable.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-warner-lanedecreasewarning-lanesdecreasedfromright">lanesDecreasedFromRight</a></span> <span class="signature">↔ int?</span>  
Number of lanes decreased on the right side of the road, `null` if the right-side change is unknown or not applicable.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-warner-lanedecreasewarning-newlanenumber">newLaneNumber</a></span> <span class="signature">↔ int</span>  
Number of lanes after the lane decrease event.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-warner-lanedecreasewarning-previouslanenumber">previousLaneNumber</a></span> <span class="signature">↔ int</span>  
Number of lanes before the lane decrease event.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-warner-lanedecreasewarning-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-warner-lanedecreasewarning-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-warner-lanedecreasewarning-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-warner-lanedecreasewarning-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
