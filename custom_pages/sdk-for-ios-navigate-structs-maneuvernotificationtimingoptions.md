---
title: "ManeuverNotificationTimingOptions"
slug: "sdk-for-ios-navigate-structs-maneuvernotificationtimingoptions"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ManeuverNotificationTimingOptions"></a>
<a title="ManeuverNotificationTimingOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-navigation">Navigation</a>

        ManeuverNotificationTimingOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ManeuverNotificationTimingOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ManeuverNotificationTimingOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A struct defining timing and distance thresholds for maneuver notifications.</p>
<p>Setting custom values will impact the time when the notification for each supported <code><a href="sdk-for-ios-navigate-enums-maneuvernotificationtype">ManeuverNotificationType</a></code> is sent - dependent on the <code><a href="sdk-for-ios-navigate-enums-timingprofile">TimingProfile</a></code>.</p>
<p><strong>Note:</strong> By default, notification thresholds depend on <code><a href="sdk-for-ios-navigate-enums-timingprofile">TimingProfile</a></code>. When custom values are set, then these rules will still apply.
The following rules apply for all transport modes:</p>
<ul>
<li>For <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code> timing profile, if the current speed limit is less than 62 m/h (100 km/h), then the notification thresholds for <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code> timing profile will be used instead.</li>
<li>For <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code> timing profile, if the current speed limit is less than 37 m/h (60 km/h), then the notification thresholds for <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code> timing profile will be used instead.</li>
<li>For <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code> timing profile the thresholds will be always used as specified.</li>
</ul>
<p>The timings follow a strict order:</p>
<ol>
<li><code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO5rangeyA2CmF">ManeuverNotificationType.range</a></code>: The first notification, it may be very far away (use 0 for farthest or earliest possible notification).</li>
<li><code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO8reminderyA2CmF">ManeuverNotificationType.reminder</a></code>: The second notification.</li>
<li><code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO8distanceyA2CmF">ManeuverNotificationType.distance</a></code>: A second reminder notification to take action.</li>
<li><code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO6actionyA2CmF">ManeuverNotificationType.action</a></code>: Final notification, specifying the required action to be taken.</li>
</ol>
<p>Therefore, it is crucial that the set values do not violate the order: range &gt; reminder &gt; distance &gt; action.
For example, the following values are valid: range = 4000, reminder = 2500, distance = 1000, action = 400.
If <code><a href="../Structs/ManeuverNotificationTimingOptions.html#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC16DistanceInMeterss5Int32Vvp">ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters</a></code> is smaller than <code><a href="../Structs/ManeuverNotificationTimingOptions.html#/s:7heresdk33ManeuverNotificationTimingOptionsV08reminderC16DistanceInMeterss5Int32Vvp">ManeuverNotificationTimingOptions.reminderNotificationDistanceInMeters</a></code> the new options will be
silently ignored and the previous values are kept.</p>
<p>You always have the choice to specify the thresholds for time or distance. For each <code><a href="sdk-for-ios-navigate-enums-maneuvernotificationtype">ManeuverNotificationType</a></code> a
notification is only sent once, so the value that is reached first, wins. However, it is recommended to always update both, time
and distance values.
A configuration value of 0 is only allowed for <code><a href="../Structs/ManeuverNotificationTimingOptions.html#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC16DistanceInMeterss5Int32Vvp">ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters</a></code> and <code><a href="../Structs/ManeuverNotificationTimingOptions.html#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC13TimeInSecondss5Int32Vvp">ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds</a></code>.
It means that the maneuver notifications of type <code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO5rangeyA2CmF">ManeuverNotificationType.range</a></code> should be generated as soon
as the maneuver location is known - no matter how far away it may be.
It’s impossible for the other types to have 0 as value due to the descending ordering rule mentioned above.</p>
<p>You can also specify the <code><a href="../Structs/ManeuverNotificationTimingOptions.html#/s:7heresdk33ManeuverNotificationTimingOptionsV06doubleC16DistanceInMeterss5Int32Vvp">ManeuverNotificationTimingOptions.doubleNotificationDistanceInMeters</a></code> threshold that determines the distance between two maneuvers that
should be merged into a single maneuver notification, for example, when they are very close to each other. Maneuvers below this
threshold will be merged like in this example: “After 300 meters turn right and then turn left.”.</p>
<p>Tip: To set the timings to the HERE SDK, you can first call <code>getManeuverNotificationTimingOptions()</code> to get the default values
for the desired combination of transport mode and timing profile. Then configure the timings, then set it back by calling the
<code>setManeuverNotificationTimingOptions()</code>.</p>
<p>Note: In the comment of each attribute, the term <code>Others</code> refers to non-pedestrian transport modes such as
<code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO7bicycleyA2CmF">TransportMode.bicycle</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>.</p>
<p>Attention: The default values for <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> on <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code> are theoretical, as such
routes cannot be calculated with the HERE SDK as highways are forbidden for pedestrians.</p>
<p>Usage example:</p>
<pre class="highlight swift"><code><span class="c1">// Get current values or default values, if no values have been set before.</span>
<span class="kt">ManeuverNotificationTimingOptions</span> <span class="n">car_highway_timings</span> <span class="o">=</span> <span class="kt">Navigator</span><span class="o">.</span><span class="nf">getManeuverNotificationTimingOptions</span><span class="p">(</span><span class="kt">TransportMode</span><span class="o">.</span><span class="n">car</span><span class="p">,</span> <span class="kt">TimingProfile</span><span class="o">.</span><span class="kt">FAST_SPEED</span><span class="p">);</span>
<span class="c1">// Set a new value for a specific option and keep the previous or default values for the others.</span>
<span class="n">car_highway_timings</span><span class="o">.</span><span class="n">distanceNotificationDistanceInMeters</span> <span class="o">=</span> <span class="mi">1500</span><span class="p">;</span>
<span class="c1">// Apply the changes to Navigator (or VisualNavigator).</span>
<span class="kt">Navigator</span><span class="o">.</span><span class="nf">setManeuverNotificationTimingOptions</span><span class="p">(</span><span class="kt">TransportMode</span><span class="o">.</span><span class="n">car</span><span class="p">,</span> <span class="kt">TimingProfile</span><span class="o">.</span><span class="kt">FAST_SPEED</span><span class="p">,</span> <span class="n">car_fast_speed_timings</span><span class="p">);</span>
</code></pre>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC16DistanceInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/rangeNotificationDistanceInMeters"></a>
<a class="token" href="#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC16DistanceInMeterss5Int32Vvp">rangeNotificationDistanceInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The default distance setting for <code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO5rangeyA2CmF">ManeuverNotificationType.range</a></code> notification. A configuration value of 0 is only allowed for
<code>ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters</code> and <code><a href="../Structs/ManeuverNotificationTimingOptions.html#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC13TimeInSecondss5Int32Vvp">ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds</a></code>. It means that the maneuver notifications of type
<code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO5rangeyA2CmF">ManeuverNotificationType.range</a></code> should be generated as soon as the maneuver location is known - no matter how far away it may be.</p>
<table><thead>
<tr>
<th>Transport Mode</th>
<th>Timing Profile</th>
<th>Default value</th>
</tr>
</thead><tbody>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code></td>
<td>0</td>
</tr>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code></td>
<td>0</td>
</tr>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code></td>
<td>0</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code></td>
<td>0</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code></td>
<td>0</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code></td>
<td>0</td>
</tr>
</tbody></table>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">rangeNotificationDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC13TimeInSecondss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/rangeNotificationTimeInSeconds"></a>
<a class="token" href="#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC13TimeInSecondss5Int32Vvp">rangeNotificationTimeInSeconds</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The default time setting for <code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO5rangeyA2CmF">ManeuverNotificationType.range</a></code> notification. A configuration value of 0 is only allowed for
<code><a href="../Structs/ManeuverNotificationTimingOptions.html#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC16DistanceInMeterss5Int32Vvp">ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters</a></code> and <code>ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds</code>. It means that the maneuver notifications of type
<code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO5rangeyA2CmF">ManeuverNotificationType.range</a></code> should be generated as soon as the maneuver location is known - no matter how far away it may be.</p>
<table><thead>
<tr>
<th>Transport Mode</th>
<th>Timing Profile</th>
<th>Default value</th>
</tr>
</thead><tbody>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code></td>
<td>0</td>
</tr>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code></td>
<td>0</td>
</tr>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code></td>
<td>0</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code></td>
<td>0</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code></td>
<td>0</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code></td>
<td>0</td>
</tr>
</tbody></table>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">rangeNotificationTimeInSeconds</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk33ManeuverNotificationTimingOptionsV08reminderC16DistanceInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/reminderNotificationDistanceInMeters"></a>
<a class="token" href="#/s:7heresdk33ManeuverNotificationTimingOptionsV08reminderC16DistanceInMeterss5Int32Vvp">reminderNotificationDistanceInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The default distance setting for <code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO8reminderyA2CmF">ManeuverNotificationType.reminder</a></code> notification.</p>
<table><thead>
<tr>
<th>Transport Mode</th>
<th>Timing Profile</th>
<th>Default value</th>
</tr>
</thead><tbody>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code></td>
<td>500</td>
</tr>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code></td>
<td>500</td>
</tr>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code></td>
<td>500</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code></td>
<td>2300</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code></td>
<td>800</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code></td>
<td>600</td>
</tr>
</tbody></table>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">reminderNotificationDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk33ManeuverNotificationTimingOptionsV08reminderC13TimeInSecondss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/reminderNotificationTimeInSeconds"></a>
<a class="token" href="#/s:7heresdk33ManeuverNotificationTimingOptionsV08reminderC13TimeInSecondss5Int32Vvp">reminderNotificationTimeInSeconds</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The default time setting for <code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO8reminderyA2CmF">ManeuverNotificationType.reminder</a></code> notification.</p>
<table><thead>
<tr>
<th>Transport Mode</th>
<th>Timing Profile</th>
<th>Default value</th>
</tr>
</thead><tbody>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code></td>
<td>40</td>
</tr>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code></td>
<td>40</td>
</tr>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code></td>
<td>40</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code></td>
<td>40</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code></td>
<td>40</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code></td>
<td>40</td>
</tr>
</tbody></table>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">reminderNotificationTimeInSeconds</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk33ManeuverNotificationTimingOptionsV08distanceC16DistanceInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceNotificationDistanceInMeters"></a>
<a class="token" href="#/s:7heresdk33ManeuverNotificationTimingOptionsV08distanceC16DistanceInMeterss5Int32Vvp">distanceNotificationDistanceInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The default distance setting for <code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO8distanceyA2CmF">ManeuverNotificationType.distance</a></code> notification.</p>
<table><thead>
<tr>
<th>Transport Mode</th>
<th>Timing Profile</th>
<th>Default value</th>
</tr>
</thead><tbody>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code></td>
<td>100</td>
</tr>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code></td>
<td>100</td>
</tr>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code></td>
<td>100</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code></td>
<td>1300</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code></td>
<td>300</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code></td>
<td>300</td>
</tr>
</tbody></table>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceNotificationDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk33ManeuverNotificationTimingOptionsV08distanceC13TimeInSecondss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceNotificationTimeInSeconds"></a>
<a class="token" href="#/s:7heresdk33ManeuverNotificationTimingOptionsV08distanceC13TimeInSecondss5Int32Vvp">distanceNotificationTimeInSeconds</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The default time setting for <code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO8distanceyA2CmF">ManeuverNotificationType.distance</a></code> notification.</p>
<table><thead>
<tr>
<th>Transport Mode</th>
<th>Timing Profile</th>
<th>Default value</th>
</tr>
</thead><tbody>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code></td>
<td>18</td>
</tr>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code></td>
<td>18</td>
</tr>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code></td>
<td>18</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code></td>
<td>18</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code></td>
<td>18</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code></td>
<td>18</td>
</tr>
</tbody></table>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceNotificationTimeInSeconds</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk33ManeuverNotificationTimingOptionsV06actionC16DistanceInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/actionNotificationDistanceInMeters"></a>
<a class="token" href="#/s:7heresdk33ManeuverNotificationTimingOptionsV06actionC16DistanceInMeterss5Int32Vvp">actionNotificationDistanceInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The default distance setting for <code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO6actionyA2CmF">ManeuverNotificationType.action</a></code> notification.</p>
<table><thead>
<tr>
<th>Transport Mode</th>
<th>Timing Profile</th>
<th>Default value</th>
</tr>
</thead><tbody>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code></td>
<td>10</td>
</tr>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code></td>
<td>10</td>
</tr>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code></td>
<td>10</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code></td>
<td>400</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code></td>
<td>100</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code></td>
<td>50</td>
</tr>
</tbody></table>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">actionNotificationDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk33ManeuverNotificationTimingOptionsV06actionC13TimeInSecondss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/actionNotificationTimeInSeconds"></a>
<a class="token" href="#/s:7heresdk33ManeuverNotificationTimingOptionsV06actionC13TimeInSecondss5Int32Vvp">actionNotificationTimeInSeconds</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The default time setting for <code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO6actionyA2CmF">ManeuverNotificationType.action</a></code> notification.</p>
<table><thead>
<tr>
<th>Transport Mode</th>
<th>Timing Profile</th>
<th>Default value</th>
</tr>
</thead><tbody>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code></td>
<td>5</td>
</tr>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code></td>
<td>5</td>
</tr>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code></td>
<td>5</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code></td>
<td>5</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code></td>
<td>5</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code></td>
<td>5</td>
</tr>
</tbody></table>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">actionNotificationTimeInSeconds</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk33ManeuverNotificationTimingOptionsV06doubleC16DistanceInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/doubleNotificationDistanceInMeters"></a>
<a class="token" href="#/s:7heresdk33ManeuverNotificationTimingOptionsV06doubleC16DistanceInMeterss5Int32Vvp">doubleNotificationDistanceInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The default distance setting for double notification.</p>
<table><thead>
<tr>
<th>Transport Mode</th>
<th>Timing Profile</th>
<th>Default value</th>
</tr>
</thead><tbody>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code></td>
<td>20</td>
</tr>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code></td>
<td>20</td>
</tr>
<tr>
<td><code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code></td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code></td>
<td>20</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code></td>
<td>750</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code></td>
<td>250</td>
</tr>
<tr>
<td>Others</td>
<td><code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code></td>
<td>150</td>
</tr>
</tbody></table>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">doubleNotificationDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC16DistanceInMeters0fc4TimeH7Seconds08remindercghI00lcjhK008distancecghI00mcjhK006actioncghI00ncjhK006doublecghI0ACs5Int32V_A8Ntcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(rangeNotificationDistanceInMeters:rangeNotificationTimeInSeconds:reminderNotificationDistanceInMeters:reminderNotificationTimeInSeconds:distanceNotificationDistanceInMeters:distanceNotificationTimeInSeconds:actionNotificationDistanceInMeters:actionNotificationTimeInSeconds:doubleNotificationDistanceInMeters:)"></a>
<a class="token" href="#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC16DistanceInMeters0fc4TimeH7Seconds08remindercghI00lcjhK008distancecghI00mcjhK006actioncghI00ncjhK006doublecghI0ACs5Int32V_A8Ntcfc">init(rangeNotificationDistanceInMeters:<wbr/>rangeNotificationTimeInSeconds:<wbr/>reminderNotificationDistanceInMeters:<wbr/>reminderNotificationTimeInSeconds:<wbr/>distanceNotificationDistanceInMeters:<wbr/>distanceNotificationTimeInSeconds:<wbr/>actionNotificationDistanceInMeters:<wbr/>actionNotificationTimeInSeconds:<wbr/>doubleNotificationDistanceInMeters:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>rangeNotificationDistanceInMeters: The default distance setting for <code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO5rangeyA2CmF">ManeuverNotificationType.range</a></code> notification. A configuration value of 0 is only allowed for
<code><a href="../Structs/ManeuverNotificationTimingOptions.html#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC16DistanceInMeterss5Int32Vvp">ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters</a></code> and <code><a href="../Structs/ManeuverNotificationTimingOptions.html#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC13TimeInSecondss5Int32Vvp">ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds</a></code>. It means that the maneuver notifications of type
<code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO5rangeyA2CmF">ManeuverNotificationType.range</a></code> should be generated as soon as the maneuver location is known - no matter how far away it may be.</li>
</ul>
<p>| Transport Mode                           | Timing Profile                | Default value                            |
  | —————————————- | ——————————| —————————————- |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code>    | 0                                        |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code> | 0                                        |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code>    | 0                                        |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code>    | 0                                        |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code> | 0                                        |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code>    | 0                                        |</p>
<ul>
<li>rangeNotificationTimeInSeconds: The default time setting for <code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO5rangeyA2CmF">ManeuverNotificationType.range</a></code> notification. A configuration value of 0 is only allowed for
<code><a href="../Structs/ManeuverNotificationTimingOptions.html#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC16DistanceInMeterss5Int32Vvp">ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters</a></code> and <code><a href="../Structs/ManeuverNotificationTimingOptions.html#/s:7heresdk33ManeuverNotificationTimingOptionsV05rangeC13TimeInSecondss5Int32Vvp">ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds</a></code>. It means that the maneuver notifications of type
<code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO5rangeyA2CmF">ManeuverNotificationType.range</a></code> should be generated as soon as the maneuver location is known - no matter how far away it may be.</li>
</ul>
<p>| Transport Mode                           | Timing Profile                | Default value                            |
  | —————————————- | ——————————| —————————————- |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code>    | 0                                        |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code> | 0                                        |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code>    | 0                                        |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code>    | 0                                        |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code> | 0                                        |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code>    | 0                                        |</p>
<ul>
<li>reminderNotificationDistanceInMeters: The default distance setting for <code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO8reminderyA2CmF">ManeuverNotificationType.reminder</a></code> notification.</li>
</ul>
<p>| Transport Mode                           | Timing Profile                | Default value                            |
  | —————————————- | ——————————| —————————————- |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code>    | 500                                      |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code> | 500                                      |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code>    | 500                                      |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code>    | 2300                                     |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code> | 800                                      |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code>    | 600                                      |</p>
<ul>
<li>reminderNotificationTimeInSeconds: The default time setting for <code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO8reminderyA2CmF">ManeuverNotificationType.reminder</a></code> notification.</li>
</ul>
<p>| Transport Mode                           | Timing Profile                | Default value                            |
  | —————————————- | —————————– | —————————————- |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code>    | 40                                       |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code> | 40                                       |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code>    | 40                                       |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code>    | 40                                       |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code> | 40                                       |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code>    | 40                                       |</p>
<ul>
<li>distanceNotificationDistanceInMeters: The default distance setting for <code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO8distanceyA2CmF">ManeuverNotificationType.distance</a></code> notification.</li>
</ul>
<p>| Transport Mode                           | Timing Profile                | Default value                            |
  | —————————————- | —————————– | —————————————- |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code>    | 100                                      |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code> | 100                                      |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code>    | 100                                      |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code>    | 1300                                     |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code> | 300                                      |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code>    | 300                                      |</p>
<ul>
<li>distanceNotificationTimeInSeconds: The default time setting for <code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO8distanceyA2CmF">ManeuverNotificationType.distance</a></code> notification.</li>
</ul>
<p>| Transport Mode                           | Timing Profile                | Default value                            |
  | —————————————- | —————————– | —————————————- |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code>    | 18                                       |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code> | 18                                       |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code>    | 18                                       |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code>    | 18                                       |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code> | 18                                       |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code>    | 18                                       |</p>
<ul>
<li>actionNotificationDistanceInMeters: The default distance setting for <code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO6actionyA2CmF">ManeuverNotificationType.action</a></code> notification.</li>
</ul>
<p>| Transport Mode                           | Timing Profile                | Default value                            |
  | —————————————- | ——————————| —————————————- |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code>    | 10                                       |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code> | 10                                       |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code>    | 10                                       |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code>    | 400                                      |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code> | 100                                      |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code>    | 50                                       |</p>
<ul>
<li>actionNotificationTimeInSeconds: The default time setting for <code><a href="../Enums/ManeuverNotificationType.html#/s:7heresdk24ManeuverNotificationTypeO6actionyA2CmF">ManeuverNotificationType.action</a></code> notification.</li>
</ul>
<p>| Transport Mode                           | Timing Profile                | Default value                            |
  | —————————————- | —————————– | —————————————- |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code>    | 5                                        |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code> | 5                                        |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code>    | 5                                        |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code>    | 5                                        |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code> | 5                                        |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code>    | 5                                        |</p>
<ul>
<li>doubleNotificationDistanceInMeters: The default distance setting for double notification.</li>
</ul>
<p>| Transport Mode                           | Timing Profile                | Default value                            |
  | —————————————- | —————————– | —————————————- |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code>    | 20                                       |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code> | 20                                       |
  | <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10pedestrianyA2CmF">TransportMode.pedestrian</a></code> | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code>    | 20                                       |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code>    | 750                                      |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code> | 250                                      |
  | Others                                   | <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code>    | 150                                      |</p></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">rangeNotificationDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">rangeNotificationTimeInSeconds</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">reminderNotificationDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">reminderNotificationTimeInSeconds</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">distanceNotificationDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">distanceNotificationTimeInSeconds</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">actionNotificationDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">actionNotificationTimeInSeconds</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">doubleNotificationDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>
</body>
</html>

`
} </HTMLBlock>
