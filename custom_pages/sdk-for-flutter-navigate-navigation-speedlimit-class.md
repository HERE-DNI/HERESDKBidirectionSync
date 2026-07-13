---
title: "SpeedLimit class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-speedlimit-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SpeedLimit-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/SpeedLimit-class-sidebar.html">

<div>

# <span class="kind-class">SpeedLimit</span> class

</div>

<div class="section desc markdown">

Represents the speed limit of the current road.

Speed limits that are described as conditional can be time-dependent. For time-dependent speed limits, the HERE SDK internally reads the current device time and notifies only on speed limits that are currently active.

It is recommended to use <a href="sdk-for-flutter-navigate-navigation-speedlimit-effectivespeedlimitinmeterspersecond">SpeedLimit.effectiveSpeedLimitInMetersPerSecond</a> when an application does not offer dedicated speed limit indicators for other cases, such as weather-dependent speed limits.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedlimit-speedlimit">SpeedLimit</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedlimit-advisoryspeedlimitinmeterspersecond">advisorySpeedLimitInMetersPerSecond</a></span> <span class="signature">↔ double?</span>  
A recommended speed limit that may not be indicated on the local road signs, but that serves to warn a driver that the road conditions may indicate a lower speed. Typically, the road condition is a curved road or a ramp but it may be due to a narrow road, narrow bridge, intersecting road, drainage dip, etc. In some cases, the advisory sign is on a different road than the one for which it applies (this can happen with ramps). In this case, the advisory speed is indicated for the road for which it is intended, even if the sign is further than 50 meters from the particular road.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedlimit-fogspeedlimitinmeterspersecond">fogSpeedLimitInMetersPerSecond</a></span> <span class="signature">↔ double?</span>  
A conditional speed limit as indicated on the local road signs. The road speed limit that is in effect only when the visibility decreases due to fog.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedlimit-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedlimit-optimalweatherspeedlimitinmeterspersecond">optimalWeatherSpeedLimitInMetersPerSecond</a></span> <span class="signature">↔ double?</span>  
A conditional speed limit as indicated on the local road signs. The road speed limit that is in effect only when the visibility is optimal due to weather conditions.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedlimit-rainspeedlimitinmeterspersecond">rainSpeedLimitInMetersPerSecond</a></span> <span class="signature">↔ double?</span>  
A conditional speed limit as indicated on the local road signs. The road speed limit that is in effect only when it is raining or there is water on the road.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedlimit-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedlimit-schoolzonespeedlimitinmeterspersecond">schoolZoneSpeedLimitInMetersPerSecond</a></span> <span class="signature">↔ double?</span>  
A conditional speed limit as indicated on the local road signs. School zone signs are often placed to slow drivers before reaching an intersection where children are crossing.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedlimit-snowspeedlimitinmeterspersecond">snowSpeedLimitInMetersPerSecond</a></span> <span class="signature">↔ double?</span>  
A conditional speed limit as indicated on the local road signs. The road speed limit that is in effect only when there is snow on the road.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedlimit-speedlimitinmeterspersecond">speedLimitInMetersPerSecond</a></span> <span class="signature">↔ double?</span>  
Regular speed limit if available. In case of unbounded speed limit, the value is zero.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedlimit-timedependentspeedlimitinmeterspersecond">timeDependentSpeedLimitInMetersPerSecond</a></span> <span class="signature">↔ double?</span>  
A conditional speed limit as indicated on the local road signs. Speed limit that is in effect considering the current local time provided by the device's clock.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedlimit-effectivespeedlimitinmeterspersecond">effectiveSpeedLimitInMetersPerSecond</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ double?</span> </span>  
Returns the effective (lowest) speed limit between <a href="sdk-for-flutter-navigate-navigation-speedlimit-speedlimitinmeterspersecond">SpeedLimit.speedLimitInMetersPerSecond</a>, <a href="sdk-for-flutter-navigate-navigation-speedlimit-schoolzonespeedlimitinmeterspersecond">SpeedLimit.schoolZoneSpeedLimitInMetersPerSecond</a>, <a href="sdk-for-flutter-navigate-navigation-speedlimit-timedependentspeedlimitinmeterspersecond">SpeedLimit.timeDependentSpeedLimitInMetersPerSecond</a> and <a href="sdk-for-flutter-navigate-navigation-speedlimit-optimalweatherspeedlimitinmeterspersecond">SpeedLimit.optimalWeatherSpeedLimitInMetersPerSecond</a>.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedlimit-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedlimit-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedlimit-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
