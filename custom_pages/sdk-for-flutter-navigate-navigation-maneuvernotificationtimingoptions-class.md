---
title: "ManeuverNotificationTimingOptions class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/ManeuverNotificationTimingOptions-class-sidebar.html">

<div>

# <span class="kind-class">ManeuverNotificationTimingOptions</span> class

</div>

<div class="section desc markdown">

A class defining timing and distance thresholds for maneuver notifications.

Setting custom values will impact the time when the notification for each supported <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType</a> is sent - dependent on the <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a>.

**Note:** By default, notification thresholds depend on <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a>. When custom values are set, then these rules will still apply. The following rules apply for all transport modes:

- For <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a> timing profile, if the current speed limit is less than 62 m/h (100 km/h), then the notification thresholds for <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a> timing profile will be used instead.
- For <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a> timing profile, if the current speed limit is less than 37 m/h (60 km/h), then the notification thresholds for <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a> timing profile will be used instead.
- For <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a> timing profile the thresholds will be always used as specified.

The timings follow a strict order:

1.  <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.range</a>: The first notification, it may be very far away (use 0 for farthest or earliest possible notification).
2.  <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.reminder</a>: The second notification.
3.  <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.distance</a>: A second reminder notification to take action.
4.  <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.action</a>: Final notification, specifying the required action to be taken.

Therefore, it is crucial that the set values do not violate the order: range \> reminder \> distance \> action. For example, the following values are valid: range = 4000, reminder = 2500, distance = 1000, action = 400. If `ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters` is smaller than `ManeuverNotificationTimingOptions.reminderNotificationDistanceInMeters` the new options will be silently ignored and the previous values are kept.

You always have the choice to specify the thresholds for time or distance. For each <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType</a> a notification is only sent once, so the value that is reached first, wins. However, it is recommended to always update both, time and distance values. A configuration value of 0 is only allowed for `ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters` and `ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds`. It means that the maneuver notifications of type <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.range</a> should be generated as soon as the maneuver location is known - no matter how far away it may be. It's impossible for the other types to have 0 as value due to the descending ordering rule mentioned above.

You can also specify the `ManeuverNotificationTimingOptions.doubleNotificationDistanceInMeters` threshold that determines the distance between two maneuvers that should be merged into a single maneuver notification, for example, when they are very close to each other. Maneuvers below this threshold will be merged like in this example: "After 300 meters turn right and then turn left.".

Tip: To set the timings to the HERE SDK, you can first call

    getManeuverNotificationTimingOptions()

to get the default values for the desired combination of transport mode and timing profile. Then configure the timings, then set it back by calling the

    setManeuverNotificationTimingOptions()

.
</p>

Note: In the comment of each attribute, the term `Others` refers to non-pedestrian transport modes such as <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.car</a>, <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.bicycle</a>, <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.truck</a>.

Attention: The default values for <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> on <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a> are theoretical, as such routes cannot be calculated with the HERE SDK as highways are forbidden for pedestrians.

Usage example:

``` dart
// Get current values or default values, if no values have been set before.
ManeuverNotificationTimingOptions car_highway_timings = Navigator.getManeuverNotificationTimingOptions(TransportMode.car, TimingProfile.FAST_SPEED);
// Set a new value for a specific option and keep the previous or default values for the others.
car_highway_timings.distanceNotificationDistanceInMeters = 1500;
// Apply the changes to Navigator (or VisualNavigator).
Navigator.setManeuverNotificationTimingOptions(TransportMode.CAR, TimingProfile.FAST_SPEED, car_fast_speed_timings);
```

</pre>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-maneuvernotificationtimingoptions">ManeuverNotificationTimingOptions</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-rangeNotificationDistanceInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">rangeNotificationDistanceInMeters</span>, </span><span id="sdk-for-flutter-navigate-param-rangeNotificationTimeInSeconds" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">rangeNotificationTimeInSeconds</span>, </span><span id="sdk-for-flutter-navigate-param-reminderNotificationDistanceInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">reminderNotificationDistanceInMeters</span>, </span><span id="sdk-for-flutter-navigate-param-reminderNotificationTimeInSeconds" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">reminderNotificationTimeInSeconds</span>, </span><span id="sdk-for-flutter-navigate-param-distanceNotificationDistanceInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">distanceNotificationDistanceInMeters</span>, </span><span id="sdk-for-flutter-navigate-param-distanceNotificationTimeInSeconds" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">distanceNotificationTimeInSeconds</span>, </span><span id="sdk-for-flutter-navigate-param-actionNotificationDistanceInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">actionNotificationDistanceInMeters</span>, </span><span id="sdk-for-flutter-navigate-param-actionNotificationTimeInSeconds" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">actionNotificationTimeInSeconds</span>, </span><span id="sdk-for-flutter-navigate-param-doubleNotificationDistanceInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">doubleNotificationDistanceInMeters</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-actionnotificationdistanceinmeters">actionNotificationDistanceInMeters</a></span> <span class="signature">↔ int</span>  
The default distance setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.action</a> notification.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-actionnotificationtimeinseconds">actionNotificationTimeInSeconds</a></span> <span class="signature">↔ int</span>  
The default time setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.action</a> notification.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-distancenotificationdistanceinmeters">distanceNotificationDistanceInMeters</a></span> <span class="signature">↔ int</span>  
The default distance setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.distance</a> notification.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-distancenotificationtimeinseconds">distanceNotificationTimeInSeconds</a></span> <span class="signature">↔ int</span>  
The default time setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.distance</a> notification.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-doublenotificationdistanceinmeters">doubleNotificationDistanceInMeters</a></span> <span class="signature">↔ int</span>  
The default distance setting for double notification.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationdistanceinmeters">rangeNotificationDistanceInMeters</a></span> <span class="signature">↔ int</span>  
The default distance setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.range</a> notification. A configuration value of 0 is only allowed for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationdistanceinmeters">ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters</a> and <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationtimeinseconds">ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds</a>. It means that the maneuver notifications of type <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.range</a> should be generated as soon as the maneuver location is known - no matter how far away it may be.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationtimeinseconds">rangeNotificationTimeInSeconds</a></span> <span class="signature">↔ int</span>  
The default time setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.range</a> notification. A configuration value of 0 is only allowed for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationdistanceinmeters">ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters</a> and <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationtimeinseconds">ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds</a>. It means that the maneuver notifications of type <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.range</a> should be generated as soon as the maneuver location is known - no matter how far away it may be.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-remindernotificationdistanceinmeters">reminderNotificationDistanceInMeters</a></span> <span class="signature">↔ int</span>  
The default distance setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.reminder</a> notification.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-remindernotificationtimeinseconds">reminderNotificationTimeInSeconds</a></span> <span class="signature">↔ int</span>  
The default time setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.reminder</a> notification.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

