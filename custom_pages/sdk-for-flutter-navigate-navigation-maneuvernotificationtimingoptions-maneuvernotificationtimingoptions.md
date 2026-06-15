---
title: "ManeuverNotificationTimingOptions constructor"
slug: "sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-maneuvernotificationtimingoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ManeuverNotificationTimingOptions.html -->


<div>
<h1>ManeuverNotificationTimingOptions constructor</h1></div>

ManeuverNotificationTimingOptions(<ol class="parameter-list"> <li>int rangeNotificationDistanceInMeters, </li>
<li>int rangeNotificationTimeInSeconds, </li>
<li>int reminderNotificationDistanceInMeters, </li>
<li>int reminderNotificationTimeInSeconds, </li>
<li>int distanceNotificationDistanceInMeters, </li>
<li>int distanceNotificationTimeInSeconds, </li>
<li>int actionNotificationDistanceInMeters, </li>
<li>int actionNotificationTimeInSeconds, </li>
<li>int doubleNotificationDistanceInMeters, </li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>rangeNotificationDistanceInMeters</code> The default distance setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.range</a> notification. A configuration value of 0 is only allowed for
<a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationdistanceinmeters">ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters</a> and <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationtimeinseconds">ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds</a>. It means that the maneuver notifications of type
<a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.range</a> should be generated as soon as the maneuver location is known - no matter how far away it may be.</li>
</ul>
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
<ul>
<li><code>rangeNotificationTimeInSeconds</code> The default time setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.range</a> notification. A configuration value of 0 is only allowed for
<a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationdistanceinmeters">ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters</a> and <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationtimeinseconds">ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds</a>. It means that the maneuver notifications of type
<a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.range</a> should be generated as soon as the maneuver location is known - no matter how far away it may be.</li>
</ul>
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
<ul>
<li><code>reminderNotificationDistanceInMeters</code> The default distance setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.reminder</a> notification.</li>
</ul>
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
<td>500</td>
</tr>
<tr>
<td><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a></td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a></td>
<td>500</td>
</tr>
<tr>
<td><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a></td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a></td>
<td>500</td>
</tr>
<tr>
<td>Others</td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a></td>
<td>2300</td>
</tr>
<tr>
<td>Others</td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a></td>
<td>800</td>
</tr>
<tr>
<td>Others</td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a></td>
<td>600</td>
</tr>
</tbody>
</table>
<ul>
<li><code>reminderNotificationTimeInSeconds</code> The default time setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.reminder</a> notification.</li>
</ul>
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
<td>40</td>
</tr>
<tr>
<td><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a></td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a></td>
<td>40</td>
</tr>
<tr>
<td><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a></td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a></td>
<td>40</td>
</tr>
<tr>
<td>Others</td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a></td>
<td>40</td>
</tr>
<tr>
<td>Others</td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a></td>
<td>40</td>
</tr>
<tr>
<td>Others</td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a></td>
<td>40</td>
</tr>
</tbody>
</table>
<ul>
<li><code>distanceNotificationDistanceInMeters</code> The default distance setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.distance</a> notification.</li>
</ul>
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
<td>100</td>
</tr>
<tr>
<td><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a></td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a></td>
<td>100</td>
</tr>
<tr>
<td><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a></td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a></td>
<td>100</td>
</tr>
<tr>
<td>Others</td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a></td>
<td>1300</td>
</tr>
<tr>
<td>Others</td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a></td>
<td>300</td>
</tr>
<tr>
<td>Others</td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a></td>
<td>300</td>
</tr>
</tbody>
</table>
<ul>
<li><code>distanceNotificationTimeInSeconds</code> The default time setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.distance</a> notification.</li>
</ul>
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
<td>18</td>
</tr>
<tr>
<td><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a></td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a></td>
<td>18</td>
</tr>
<tr>
<td><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a></td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a></td>
<td>18</td>
</tr>
<tr>
<td>Others</td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a></td>
<td>18</td>
</tr>
<tr>
<td>Others</td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a></td>
<td>18</td>
</tr>
<tr>
<td>Others</td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a></td>
<td>18</td>
</tr>
</tbody>
</table>
<ul>
<li><code>actionNotificationDistanceInMeters</code> The default distance setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.action</a> notification.</li>
</ul>
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
<td>10</td>
</tr>
<tr>
<td><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a></td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a></td>
<td>10</td>
</tr>
<tr>
<td><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a></td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a></td>
<td>10</td>
</tr>
<tr>
<td>Others</td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a></td>
<td>400</td>
</tr>
<tr>
<td>Others</td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a></td>
<td>100</td>
</tr>
<tr>
<td>Others</td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a></td>
<td>50</td>
</tr>
</tbody>
</table>
<ul>
<li><code>actionNotificationTimeInSeconds</code> The default time setting for <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.action</a> notification.</li>
</ul>
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
<td>5</td>
</tr>
<tr>
<td><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a></td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a></td>
<td>5</td>
</tr>
<tr>
<td><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a></td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a></td>
<td>5</td>
</tr>
<tr>
<td>Others</td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a></td>
<td>5</td>
</tr>
<tr>
<td>Others</td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a></td>
<td>5</td>
</tr>
<tr>
<td>Others</td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a></td>
<td>5</td>
</tr>
</tbody>
</table>
<ul>
<li><code>doubleNotificationDistanceInMeters</code> The default distance setting for double notification.</li>
</ul>
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
<td>20</td>
</tr>
<tr>
<td><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a></td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a></td>
<td>20</td>
</tr>
<tr>
<td><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.pedestrian</a></td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a></td>
<td>20</td>
</tr>
<tr>
<td>Others</td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a></td>
<td>750</td>
</tr>
<tr>
<td>Others</td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a></td>
<td>250</td>
</tr>
<tr>
<td>Others</td>
<td><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a></td>
<td>150</td>
</tr>
</tbody>
</table>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ManeuverNotificationTimingOptions(this.rangeNotificationDistanceInMeters, this.rangeNotificationTimeInSeconds, this.reminderNotificationDistanceInMeters, this.reminderNotificationTimeInSeconds, this.distanceNotificationDistanceInMeters, this.distanceNotificationTimeInSeconds, this.actionNotificationDistanceInMeters, this.actionNotificationTimeInSeconds, this.doubleNotificationDistanceInMeters);</code></pre>

 



</div>
`
}</HTMLBlock>
