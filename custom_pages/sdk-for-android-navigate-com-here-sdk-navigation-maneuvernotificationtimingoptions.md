---
title: "ManeuverNotificationTimingOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- ManeuverNotificationTimingOptions.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.ManeuverNotificationTimingOptions</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">ManeuverNotificationTimingOptions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>A class defining timing and distance thresholds for maneuver notifications.
 Setting custom values will impact the time when the notification for each supported <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation"><code>ManeuverNotificationType</code></a> is sent - dependent on the <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile" title="enum class in com.here.sdk.navigation"><code>TimingProfile</code></a>.
 <strong>Note:</strong> By default, notification thresholds depend on <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile" title="enum class in com.here.sdk.navigation"><code>TimingProfile</code></a>. When custom values are set, then these rules will still apply.
 The following rules apply for all transport modes:
 <ul>
<li>For <a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a> timing profile, if the current speed limit is less than 62 m/h (100 km/h), then the notification thresholds for <a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a> timing profile will be used instead.</li>
<li>For <a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a> timing profile, if the current speed limit is less than 37 m/h (60 km/h), then the notification thresholds for <a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a> timing profile will be used instead.</li>
<li>For <a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a> timing profile the thresholds will be always used as specified.</li>
</ul>
The timings follow a strict order:
 <ol>
<li><a href="sdk-for-android-navigate-maneuvernotificationtype#RANGE"><code>ManeuverNotificationType.RANGE</code></a>: The first notification, it may be very far away (use 0 for farthest or earliest possible notification).</li>
<li><a href="sdk-for-android-navigate-maneuvernotificationtype#REMINDER"><code>ManeuverNotificationType.REMINDER</code></a>: The second notification.</li>
<li><a href="sdk-for-android-navigate-maneuvernotificationtype#DISTANCE"><code>ManeuverNotificationType.DISTANCE</code></a>: A second reminder notification to take action.</li>
<li><a href="sdk-for-android-navigate-maneuvernotificationtype#ACTION"><code>ManeuverNotificationType.ACTION</code></a>: Final notification, specifying the required action to be taken.</li>
</ol>
Therefore, it is crucial that the set values do not violate the order: range &gt; reminder &gt; distance &gt; action.
 For example, the following values are valid: range = 4000, reminder = 2500, distance = 1000, action = 400.
 If <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#rangeNotificationDistanceInMeters"><code>rangeNotificationDistanceInMeters</code></a> is smaller than <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#reminderNotificationDistanceInMeters"><code>reminderNotificationDistanceInMeters</code></a> the new options will be
 silently ignored and the previous values are kept.
 You always have the choice to specify the thresholds for time or distance. For each <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtype" title="enum class in com.here.sdk.navigation"><code>ManeuverNotificationType</code></a> a
 notification is only sent once, so the value that is reached first, wins. However, it is recommended to always update both, time
 and distance values.
 A configuration value of 0 is only allowed for <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#rangeNotificationDistanceInMeters"><code>rangeNotificationDistanceInMeters</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#rangeNotificationTimeInSeconds"><code>rangeNotificationTimeInSeconds</code></a>.
 It means that the maneuver notifications of type <a href="sdk-for-android-navigate-maneuvernotificationtype#RANGE"><code>ManeuverNotificationType.RANGE</code></a> should be generated as soon
 as the maneuver location is known - no matter how far away it may be.
 It's impossible for the other types to have 0 as value due to the descending ordering rule mentioned above.
 You can also specify the <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#doubleNotificationDistanceInMeters"><code>doubleNotificationDistanceInMeters</code></a> threshold that determines the distance between two maneuvers that
 should be merged into a single maneuver notification, for example, when they are very close to each other. Maneuvers below this
 threshold will be merged like in this example: "After 300 meters turn right and then turn left.".
 Tip: To set the timings to the HERE SDK, you can first call <code>getManeuverNotificationTimingOptions()</code> to get the default values
 for the desired combination of transport mode and timing profile. Then configure the timings, then set it back by calling the
 <code>setManeuverNotificationTimingOptions()</code>.
 Note: In the comment of each attribute, the term <code>Others</code> refers to non-pedestrian transport modes such as
 <a href="sdk-for-android-navigate-transportmode#CAR"><code>TransportMode.CAR</code></a>, <a href="sdk-for-android-navigate-transportmode#BICYCLE"><code>TransportMode.BICYCLE</code></a>, <a href="sdk-for-android-navigate-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a>.
 Attention: The default values for <a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a> on <a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a> are theoretical, as such
 routes cannot be calculated with the HERE SDK as highways are forbidden for pedestrians.
 Usage example:
 <pre><code>
 // Get current values or default values, if no values have been set before.
 ManeuverNotificationTimingOptions car_highway_timings = Navigator.getManeuverNotificationTimingOptions(TransportMode.CAR, TimingProfile.FAST_SPEED);
 // Set a new value for a specific option and keep the previous or default values for the others.
 car_highway_timings.distanceNotificationDistanceInMeters = 1500;
 // Apply the changes to Navigator (or VisualNavigator).
 Navigator.setManeuverNotificationTimingOptions(TransportMode.CAR, TimingProfile.FAST_SPEED, car_fast_speed_timings);
 </code></pre></p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#actionNotificationDistanceInMeters">actionNotificationDistanceInMeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">The default distance setting for <a href="sdk-for-android-navigate-maneuvernotificationtype#ACTION"><code>ManeuverNotificationType.ACTION</code></a> notification.</div>
</div>
<div class="col-first odd-row-color"><code>int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#actionNotificationTimeInSeconds">actionNotificationTimeInSeconds</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The default time setting for <a href="sdk-for-android-navigate-maneuvernotificationtype#ACTION"><code>ManeuverNotificationType.ACTION</code></a> notification.</div>
</div>
<div class="col-first even-row-color"><code>int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#distanceNotificationDistanceInMeters">distanceNotificationDistanceInMeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">The default distance setting for <a href="sdk-for-android-navigate-maneuvernotificationtype#DISTANCE"><code>ManeuverNotificationType.DISTANCE</code></a> notification.</div>
</div>
<div class="col-first odd-row-color"><code>int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#distanceNotificationTimeInSeconds">distanceNotificationTimeInSeconds</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The default time setting for <a href="sdk-for-android-navigate-maneuvernotificationtype#DISTANCE"><code>ManeuverNotificationType.DISTANCE</code></a> notification.</div>
</div>
<div class="col-first even-row-color"><code>int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#doubleNotificationDistanceInMeters">doubleNotificationDistanceInMeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">The default distance setting for double notification.</div>
</div>
<div class="col-first odd-row-color"><code>int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#rangeNotificationDistanceInMeters">rangeNotificationDistanceInMeters</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The default distance setting for <a href="sdk-for-android-navigate-maneuvernotificationtype#RANGE"><code>ManeuverNotificationType.RANGE</code></a> notification.</div>
</div>
<div class="col-first even-row-color"><code>int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#rangeNotificationTimeInSeconds">rangeNotificationTimeInSeconds</a></code></div>
<div class="col-last even-row-color">
<div class="block">The default time setting for <a href="sdk-for-android-navigate-maneuvernotificationtype#RANGE"><code>ManeuverNotificationType.RANGE</code></a> notification.</div>
</div>
<div class="col-first odd-row-color"><code>int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#reminderNotificationDistanceInMeters">reminderNotificationDistanceInMeters</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The default distance setting for <a href="sdk-for-android-navigate-maneuvernotificationtype#REMINDER"><code>ManeuverNotificationType.REMINDER</code></a> notification.</div>
</div>
<div class="col-first even-row-color"><code>int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#reminderNotificationTimeInSeconds">reminderNotificationTimeInSeconds</a></code></div>
<div class="col-last even-row-color">
<div class="block">The default time setting for <a href="sdk-for-android-navigate-maneuvernotificationtype#REMINDER"><code>ManeuverNotificationType.REMINDER</code></a> notification.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#%3Cinit%3E(int,int,int,int,int,int,int,int,int)">ManeuverNotificationTimingOptions</a><wbr/>(int rangeNotificationDistanceInMeters,
 int rangeNotificationTimeInSeconds,
 int reminderNotificationDistanceInMeters,
 int reminderNotificationTimeInSeconds,
 int distanceNotificationDistanceInMeters,
 int distanceNotificationTimeInSeconds,
 int actionNotificationDistanceInMeters,
 int actionNotificationTimeInSeconds,
 int doubleNotificationDistanceInMeters)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#hashCode()">hashCode</a>()</code></div>

</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="rangeNotificationDistanceInMeters">
<h3>rangeNotificationDistanceInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">rangeNotificationDistanceInMeters</span></div>
<div class="block"><p>The default distance setting for <a href="sdk-for-android-navigate-maneuvernotificationtype#RANGE"><code>ManeuverNotificationType.RANGE</code></a> notification. A configuration value of 0 is only allowed for
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#rangeNotificationDistanceInMeters"><code>rangeNotificationDistanceInMeters</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#rangeNotificationTimeInSeconds"><code>rangeNotificationTimeInSeconds</code></a>. It means that the maneuver notifications of type
 <a href="sdk-for-android-navigate-maneuvernotificationtype#RANGE"><code>ManeuverNotificationType.RANGE</code></a> should be generated as soon as the maneuver location is known - no matter how far away it may be.
 <table>
<thead>
<tr><th>Transport Mode</th><th>Timing Profile</th><th>Default value</th></tr>
</thead>
<tbody>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>0</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>0</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>0</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>0</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>0</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>0</td></tr>
</tbody>
</table></p></div>
</section>
</li>
<li>
<section class="detail" id="rangeNotificationTimeInSeconds">
<h3>rangeNotificationTimeInSeconds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">rangeNotificationTimeInSeconds</span></div>
<div class="block"><p>The default time setting for <a href="sdk-for-android-navigate-maneuvernotificationtype#RANGE"><code>ManeuverNotificationType.RANGE</code></a> notification. A configuration value of 0 is only allowed for
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#rangeNotificationDistanceInMeters"><code>rangeNotificationDistanceInMeters</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#rangeNotificationTimeInSeconds"><code>rangeNotificationTimeInSeconds</code></a>. It means that the maneuver notifications of type
 <a href="sdk-for-android-navigate-maneuvernotificationtype#RANGE"><code>ManeuverNotificationType.RANGE</code></a> should be generated as soon as the maneuver location is known - no matter how far away it may be.
 <table>
<thead>
<tr><th>Transport Mode</th><th>Timing Profile</th><th>Default value</th></tr>
</thead>
<tbody>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>0</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>0</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>0</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>0</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>0</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>0</td></tr>
</tbody>
</table></p></div>
</section>
</li>
<li>
<section class="detail" id="reminderNotificationDistanceInMeters">
<h3>reminderNotificationDistanceInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">reminderNotificationDistanceInMeters</span></div>
<div class="block"><p>The default distance setting for <a href="sdk-for-android-navigate-maneuvernotificationtype#REMINDER"><code>ManeuverNotificationType.REMINDER</code></a> notification.
 <table>
<thead>
<tr><th>Transport Mode</th><th>Timing Profile</th><th>Default value</th></tr>
</thead>
<tbody>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>500</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>500</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>500</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>2300</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>800</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>600</td></tr>
</tbody>
</table></p></div>
</section>
</li>
<li>
<section class="detail" id="reminderNotificationTimeInSeconds">
<h3>reminderNotificationTimeInSeconds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">reminderNotificationTimeInSeconds</span></div>
<div class="block"><p>The default time setting for <a href="sdk-for-android-navigate-maneuvernotificationtype#REMINDER"><code>ManeuverNotificationType.REMINDER</code></a> notification.
 <table>
<thead>
<tr><th>Transport Mode</th><th>Timing Profile</th><th>Default value</th></tr>
</thead>
<tbody>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>40</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>40</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>40</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>40</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>40</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>40</td></tr>
</tbody>
</table></p></div>
</section>
</li>
<li>
<section class="detail" id="distanceNotificationDistanceInMeters">
<h3>distanceNotificationDistanceInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">distanceNotificationDistanceInMeters</span></div>
<div class="block"><p>The default distance setting for <a href="sdk-for-android-navigate-maneuvernotificationtype#DISTANCE"><code>ManeuverNotificationType.DISTANCE</code></a> notification.
 <table>
<thead>
<tr><th>Transport Mode</th><th>Timing Profile</th><th>Default value</th></tr>
</thead>
<tbody>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>100</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>100</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>100</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>1300</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>300</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>300</td></tr>
</tbody>
</table></p></div>
</section>
</li>
<li>
<section class="detail" id="distanceNotificationTimeInSeconds">
<h3>distanceNotificationTimeInSeconds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">distanceNotificationTimeInSeconds</span></div>
<div class="block"><p>The default time setting for <a href="sdk-for-android-navigate-maneuvernotificationtype#DISTANCE"><code>ManeuverNotificationType.DISTANCE</code></a> notification.
 <table>
<thead>
<tr><th>Transport Mode</th><th>Timing Profile</th><th>Default value</th></tr>
</thead>
<tbody>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>18</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>18</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>18</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>18</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>18</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>18</td></tr>
</tbody>
</table></p></div>
</section>
</li>
<li>
<section class="detail" id="actionNotificationDistanceInMeters">
<h3>actionNotificationDistanceInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">actionNotificationDistanceInMeters</span></div>
<div class="block"><p>The default distance setting for <a href="sdk-for-android-navigate-maneuvernotificationtype#ACTION"><code>ManeuverNotificationType.ACTION</code></a> notification.
 <table>
<thead>
<tr><th>Transport Mode</th><th>Timing Profile</th><th>Default value</th></tr>
</thead>
<tbody>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>10</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>10</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>10</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>400</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>100</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>50</td></tr>
</tbody>
</table></p></div>
</section>
</li>
<li>
<section class="detail" id="actionNotificationTimeInSeconds">
<h3>actionNotificationTimeInSeconds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">actionNotificationTimeInSeconds</span></div>
<div class="block"><p>The default time setting for <a href="sdk-for-android-navigate-maneuvernotificationtype#ACTION"><code>ManeuverNotificationType.ACTION</code></a> notification.
 <table>
<thead>
<tr><th>Transport Mode</th><th>Timing Profile</th><th>Default value</th></tr>
</thead>
<tbody>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>5</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>5</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>5</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>5</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>5</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>5</td></tr>
</tbody>
</table></p></div>
</section>
</li>
<li>
<section class="detail" id="doubleNotificationDistanceInMeters">
<h3>doubleNotificationDistanceInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">doubleNotificationDistanceInMeters</span></div>
<div class="block"><p>The default distance setting for double notification.
 <table>
<thead>
<tr><th>Transport Mode</th><th>Timing Profile</th><th>Default value</th></tr>
</thead>
<tbody>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>20</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>20</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>20</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>750</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>250</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>150</td></tr>
</tbody>
</table></p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(int,int,int,int,int,int,int,int,int)">
<h3>ManeuverNotificationTimingOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ManeuverNotificationTimingOptions</span><wbr/><span class="parameters">(int rangeNotificationDistanceInMeters,
 int rangeNotificationTimeInSeconds,
 int reminderNotificationDistanceInMeters,
 int reminderNotificationTimeInSeconds,
 int distanceNotificationDistanceInMeters,
 int distanceNotificationTimeInSeconds,
 int actionNotificationDistanceInMeters,
 int actionNotificationTimeInSeconds,
 int doubleNotificationDistanceInMeters)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rangeNotificationDistanceInMeters</code> - <p>The default distance setting for <a href="sdk-for-android-navigate-maneuvernotificationtype#RANGE"><code>ManeuverNotificationType.RANGE</code></a> notification. A configuration value of 0 is only allowed for
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#rangeNotificationDistanceInMeters"><code>rangeNotificationDistanceInMeters</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#rangeNotificationTimeInSeconds"><code>rangeNotificationTimeInSeconds</code></a>. It means that the maneuver notifications of type
 <a href="sdk-for-android-navigate-maneuvernotificationtype#RANGE"><code>ManeuverNotificationType.RANGE</code></a> should be generated as soon as the maneuver location is known - no matter how far away it may be.
 <table>
<thead>
<tr><th>Transport Mode</th><th>Timing Profile</th><th>Default value</th></tr>
</thead>
<tbody>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>0</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>0</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>0</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>0</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>0</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>0</td></tr>
</tbody>
</table></p></dd>
<dd><code>rangeNotificationTimeInSeconds</code> - <p>The default time setting for <a href="sdk-for-android-navigate-maneuvernotificationtype#RANGE"><code>ManeuverNotificationType.RANGE</code></a> notification. A configuration value of 0 is only allowed for
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#rangeNotificationDistanceInMeters"><code>rangeNotificationDistanceInMeters</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions#rangeNotificationTimeInSeconds"><code>rangeNotificationTimeInSeconds</code></a>. It means that the maneuver notifications of type
 <a href="sdk-for-android-navigate-maneuvernotificationtype#RANGE"><code>ManeuverNotificationType.RANGE</code></a> should be generated as soon as the maneuver location is known - no matter how far away it may be.
 <table>
<thead>
<tr><th>Transport Mode</th><th>Timing Profile</th><th>Default value</th></tr>
</thead>
<tbody>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>0</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>0</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>0</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>0</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>0</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>0</td></tr>
</tbody>
</table></p></dd>
<dd><code>reminderNotificationDistanceInMeters</code> - <p>The default distance setting for <a href="sdk-for-android-navigate-maneuvernotificationtype#REMINDER"><code>ManeuverNotificationType.REMINDER</code></a> notification.
 <table>
<thead>
<tr><th>Transport Mode</th><th>Timing Profile</th><th>Default value</th></tr>
</thead>
<tbody>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>500</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>500</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>500</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>2300</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>800</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>600</td></tr>
</tbody>
</table></p></dd>
<dd><code>reminderNotificationTimeInSeconds</code> - <p>The default time setting for <a href="sdk-for-android-navigate-maneuvernotificationtype#REMINDER"><code>ManeuverNotificationType.REMINDER</code></a> notification.
 <table>
<thead>
<tr><th>Transport Mode</th><th>Timing Profile</th><th>Default value</th></tr>
</thead>
<tbody>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>40</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>40</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>40</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>40</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>40</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>40</td></tr>
</tbody>
</table></p></dd>
<dd><code>distanceNotificationDistanceInMeters</code> - <p>The default distance setting for <a href="sdk-for-android-navigate-maneuvernotificationtype#DISTANCE"><code>ManeuverNotificationType.DISTANCE</code></a> notification.
 <table>
<thead>
<tr><th>Transport Mode</th><th>Timing Profile</th><th>Default value</th></tr>
</thead>
<tbody>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>100</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>100</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>100</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>1300</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>300</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>300</td></tr>
</tbody>
</table></p></dd>
<dd><code>distanceNotificationTimeInSeconds</code> - <p>The default time setting for <a href="sdk-for-android-navigate-maneuvernotificationtype#DISTANCE"><code>ManeuverNotificationType.DISTANCE</code></a> notification.
 <table>
<thead>
<tr><th>Transport Mode</th><th>Timing Profile</th><th>Default value</th></tr>
</thead>
<tbody>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>18</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>18</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>18</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>18</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>18</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>18</td></tr>
</tbody>
</table></p></dd>
<dd><code>actionNotificationDistanceInMeters</code> - <p>The default distance setting for <a href="sdk-for-android-navigate-maneuvernotificationtype#ACTION"><code>ManeuverNotificationType.ACTION</code></a> notification.
 <table>
<thead>
<tr><th>Transport Mode</th><th>Timing Profile</th><th>Default value</th></tr>
</thead>
<tbody>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>10</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>10</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>10</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>400</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>100</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>50</td></tr>
</tbody>
</table></p></dd>
<dd><code>actionNotificationTimeInSeconds</code> - <p>The default time setting for <a href="sdk-for-android-navigate-maneuvernotificationtype#ACTION"><code>ManeuverNotificationType.ACTION</code></a> notification.
 <table>
<thead>
<tr><th>Transport Mode</th><th>Timing Profile</th><th>Default value</th></tr>
</thead>
<tbody>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>5</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>5</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>5</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>5</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>5</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>5</td></tr>
</tbody>
</table></p></dd>
<dd><code>doubleNotificationDistanceInMeters</code> - <p>The default distance setting for double notification.
 <table>
<thead>
<tr><th>Transport Mode</th><th>Timing Profile</th><th>Default value</th></tr>
</thead>
<tbody>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>20</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>20</td></tr>
<tr><td><a href="sdk-for-android-navigate-transportmode#PEDESTRIAN"><code>TransportMode.PEDESTRIAN</code></a></td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>20</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#FAST_SPEED"><code>TimingProfile.FAST_SPEED</code></a></td><td>750</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#REGULAR_SPEED"><code>TimingProfile.REGULAR_SPEED</code></a></td><td>250</td></tr>
<tr><td>Others</td><td><a href="sdk-for-android-navigate-timingprofile#SLOW_SPEED"><code>TimingProfile.SLOW_SPEED</code></a></td><td>150</td></tr>
</tbody>
</table></p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->






</div>
`
}</HTMLBlock>
