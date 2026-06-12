---
title: "ManeuverNotificationTimingOptions class"
slug: "sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ManeuverNotificationTimingOptions-class.html -->


<div>
<h1>ManeuverNotificationTimingOptions class</h1></div>

<p>A class defining timing and distance thresholds for maneuver notifications.</p>
<p>Setting custom values will impact the time when the notification for each supported <a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType</a> is sent - dependent on the <a href="/sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a>.</p>
<p><strong>Note:</strong> By default, notification thresholds depend on <a href="/sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a>. When custom values are set, then these rules will still apply.
The following rules apply for all transport modes:</p>
<ul>
<li>For <a href="/sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a> timing profile, if the current speed limit is less than 62 m/h (100 km/h), then the notification thresholds for <a href="/sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a> timing profile will be used instead.</li>
<li>For <a href="/sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a> timing profile, if the current speed limit is less than 37 m/h (60 km/h), then the notification thresholds for <a href="/sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a> timing profile will be used instead.</li>
<li>For <a href="/sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a> timing profile the thresholds will be always used as specified.</li>
</ul>
<p>The timings follow a strict order:</p>
<ol>
<li><a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.range</a>: The first notification, it may be very far away (use 0 for farthest or earliest possible notification).</li>
<li><a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.reminder</a>: The second notification.</li>
<li><a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.distance</a>: A second reminder notification to take action.</li>
<li><a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.action</a>: Final notification, specifying the required action to be taken.</li>
</ol>
<p>Therefore, it is crucial that the set values do not violate the order: range &gt; reminder &gt; distance &gt; action.
For example, the following values are valid: range = 4000, reminder = 2500, distance = 1000, action = 400.
If <code>ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters</code> is smaller than <code>ManeuverNotificationTimingOptions.reminderNotificationDistanceInMeters</code> the new options will be
silently ignored and the previous values are kept.</p>
<p>You always have the choice to specify the thresholds for time or distance. For each <a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType</a> a
notification is only sent once, so the value that is reached first, wins. However, it is recommended to always update both, time
and distance values.
A configuration value of 0 is only allowed for <code>ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters</code> and <code>ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds</code>.
It means that the maneuver notifications of type <a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.range</a> should be generated as soon
as the maneuver location is known - no matter how far away it may be.
It's impossible for the other types to have 0 as value due to the descending ordering rule mentioned above.</p>
<p>You can also specify the <code>ManeuverNotificationTimingOptions.doubleNotificationDistanceInMeters</code> threshold that determines the distance between two maneuvers that
should be merged into a single maneuver notification, for example, when they are very close to each other. Maneuvers below this
threshold will be merged like in this example: "After 300 meters turn right and then turn left.".</p>
<p>Tip: To set the timings to the HERE SDK, you can first call <code>getManeuverNotificationTimingOptions()</code> to get the default values
for the desired combination of transport mode and timing profile. Then configure the timings, then set it back by calling the
<code>setManeuverNotificationTimingOptions()</code>.</p>
<p>Note: In the comment of each attribute, the term <code>Others</code> refers to non-pedestrian transport modes such as
<a href="/sdk-for-flutter-navigate-transport-transportmode">TransportMode.car</a>, <a href="/sdk-for-flutter-navigate-transport-transportmode">TransportMode.bicycle</a>, <a href="/sdk-for-flutter-navigate-transport-transportmode">TransportMode.truck</a>.</p>
<p>Attention: The default values for <a href="/sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a> on <a href="/sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a> are theoretical, as such
routes cannot be calculated with the HERE SDK as highways are forbidden for pedestrians.</p>
<p>Usage example:</p>
<pre class="language-dart"><code>// Get current values or default values, if no values have been set before.
ManeuverNotificationTimingOptions car_highway_timings = Navigator.getManeuverNotificationTimingOptions(TransportMode.car, TimingProfile.FAST_SPEED);
// Set a new value for a specific option and keep the previous or default values for the others.
car_highway_timings.distanceNotificationDistanceInMeters = 1500;
// Apply the changes to Navigator (or VisualNavigator).
Navigator.setManeuverNotificationTimingOptions(TransportMode.CAR, TimingProfile.FAST_SPEED, car_fast_speed_timings);
</code></pre>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-maneuvernotificationtimingoptions">ManeuverNotificationTimingOptions</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-actionnotificationdistanceinmeters">actionNotificationDistanceInMeters</a></li><li><a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-actionnotificationtimeinseconds">actionNotificationTimeInSeconds</a></li><li><a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-distancenotificationdistanceinmeters">distanceNotificationDistanceInMeters</a></li><li><a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-distancenotificationtimeinseconds">distanceNotificationTimeInSeconds</a></li><li><a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-doublenotificationdistanceinmeters">doubleNotificationDistanceInMeters</a></li><li><a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationdistanceinmeters">rangeNotificationDistanceInMeters</a></li><li><a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationtimeinseconds">rangeNotificationTimeInSeconds</a></li><li><a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-remindernotificationdistanceinmeters">reminderNotificationDistanceInMeters</a></li><li><a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-remindernotificationtimeinseconds">reminderNotificationTimeInSeconds</a></li><li><a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
