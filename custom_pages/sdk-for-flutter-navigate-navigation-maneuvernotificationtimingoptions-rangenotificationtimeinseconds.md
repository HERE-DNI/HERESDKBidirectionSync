---
title: "rangeNotificationTimeInSeconds property"
slug: "sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationtimeinseconds"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- rangeNotificationTimeInSeconds.html -->


<div>
<h1>rangeNotificationTimeInSeconds property</h1></div>

        
        int
        rangeNotificationTimeInSeconds
<div class="features">getter/setter pair</div>


<p>The default time setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.range</a> notification. A configuration value of 0 is only allowed for
<a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationdistanceinmeters">ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters</a> and <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationtimeinseconds">ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds</a>. It means that the maneuver notifications of type
<a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.range</a> should be generated as soon as the maneuver location is known - no matter how far away it may be.</p>
<table>
<thead>
<tr>
<th>Transport Mode</th>
<th>Timing Profile</th>
<th>Default value</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a></td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a></td>
<td>0</td>
</tr>
<tr>
<td><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a></td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a></td>
<td>0</td>
</tr>
<tr>
<td><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a></td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a></td>
<td>0</td>
</tr>
<tr>
<td>Others</td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a></td>
<td>0</td>
</tr>
<tr>
<td>Others</td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a></td>
<td>0</td>
</tr>
<tr>
<td>Others</td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a></td>
<td>0</td>
</tr>
</tbody>
</table>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int rangeNotificationTimeInSeconds;</code></pre>

 



</div>
`
}</HTMLBlock>
