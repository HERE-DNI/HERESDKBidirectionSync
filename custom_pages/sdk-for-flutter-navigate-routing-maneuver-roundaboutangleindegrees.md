---
title: "roundaboutAngleInDegrees property - Maneuver class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-maneuver-roundaboutangleindegrees"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- roundaboutAngleInDegrees.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/Maneuver-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">roundaboutAngleInDegrees</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">double?</span> <span class="name">roundaboutAngleInDegrees</span>

</div>

<div class="section desc markdown">

The angle is estimated between the incoming and outgoing route parts before entering the actual roundabout. This is done to provide a better orientation for drivers. For better results, the incoming and outcoming route parts can be around 50 meters in length. In addition, these parts lie usually around 30 meters away from the actual roundabout. Therefore, the resulting arc does not necessarily represent the exact curved path a vehicle has to follow within a roundabout from the point of entry to the point of exit. Instead, it reflects the route path before and after the roundabout to highlight the directional change along the route. The angle can have a value from -360.0 to 360.0, and it is positive in right-hand side driving country, and negative in left-hand side countries. Note that the value is available for both the enter roundabout actions and the exit roundabout actions. Both maneuvers have the same value. When the incoming or outgoing route parts are curvy or when the roundabout itself is not representing a perfect circle, then the accuracy of the angle may be compromised. **Note:** These attributes are only available for the Navigate license. The angle is estimated between the incoming and outgoing route parts before entering the actual roundabout.

</div>

## Implementation

``` dart
double? get roundaboutAngleInDegrees;
```

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
