---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ManeuverNotificationTimingOptions-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">ManeuverNotificationTimingOptions class</li>
</ol>
<div class="self-name">ManeuverNotificationTimingOptions</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/ManeuverNotificationTimingOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>ManeuverNotificationTimingOptions class</h1></div>
<section class="desc markdown">
<p>A class defining timing and distance thresholds for maneuver notifications.</p>
<p>Setting custom values will impact the time when the notification for each supported /sdk-for-flutter-navigate-navigation-maneuvernotificationtype is sent - dependent on the /sdk-for-flutter-navigate-navigation-timingprofile.</p>
<p><strong>Note:</strong> By default, notification thresholds depend on /sdk-for-flutter-navigate-navigation-timingprofile. When custom values are set, then these rules will still apply.
The following rules apply for all transport modes:</p>
<ul>
<li>For /sdk-for-flutter-navigate-navigation-timingprofile timing profile, if the current speed limit is less than 62 m/h (100 km/h), then the notification thresholds for /sdk-for-flutter-navigate-navigation-timingprofile timing profile will be used instead.</li>
<li>For /sdk-for-flutter-navigate-navigation-timingprofile timing profile, if the current speed limit is less than 37 m/h (60 km/h), then the notification thresholds for /sdk-for-flutter-navigate-navigation-timingprofile timing profile will be used instead.</li>
<li>For /sdk-for-flutter-navigate-navigation-timingprofile timing profile the thresholds will be always used as specified.</li>
</ul>
<p>The timings follow a strict order:</p>
<ol>
<li>/sdk-for-flutter-navigate-navigation-maneuvernotificationtype: The first notification, it may be very far away (use 0 for farthest or earliest possible notification).</li>
<li>/sdk-for-flutter-navigate-navigation-maneuvernotificationtype: The second notification.</li>
<li>/sdk-for-flutter-navigate-navigation-maneuvernotificationtype: A second reminder notification to take action.</li>
<li>/sdk-for-flutter-navigate-navigation-maneuvernotificationtype: Final notification, specifying the required action to be taken.</li>
</ol>
<p>Therefore, it is crucial that the set values do not violate the order: range &gt; reminder &gt; distance &gt; action.
For example, the following values are valid: range = 4000, reminder = 2500, distance = 1000, action = 400.
If <code>ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters</code> is smaller than <code>ManeuverNotificationTimingOptions.reminderNotificationDistanceInMeters</code> the new options will be
silently ignored and the previous values are kept.</p>
<p>You always have the choice to specify the thresholds for time or distance. For each /sdk-for-flutter-navigate-navigation-maneuvernotificationtype a
notification is only sent once, so the value that is reached first, wins. However, it is recommended to always update both, time
and distance values.
A configuration value of 0 is only allowed for <code>ManeuverNotificationTimingOptions.rangeNotificationDistanceInMeters</code> and <code>ManeuverNotificationTimingOptions.rangeNotificationTimeInSeconds</code>.
It means that the maneuver notifications of type /sdk-for-flutter-navigate-navigation-maneuvernotificationtype should be generated as soon
as the maneuver location is known - no matter how far away it may be.
It's impossible for the other types to have 0 as value due to the descending ordering rule mentioned above.</p>
<p>You can also specify the <code>ManeuverNotificationTimingOptions.doubleNotificationDistanceInMeters</code> threshold that determines the distance between two maneuvers that
should be merged into a single maneuver notification, for example, when they are very close to each other. Maneuvers below this
threshold will be merged like in this example: "After 300 meters turn right and then turn left.".</p>
<p>Tip: To set the timings to the HERE SDK, you can first call <code>getManeuverNotificationTimingOptions()</code> to get the default values
for the desired combination of transport mode and timing profile. Then configure the timings, then set it back by calling the
<code>setManeuverNotificationTimingOptions()</code>.</p>
<p>Note: In the comment of each attribute, the term <code>Others</code> refers to non-pedestrian transport modes such as
/sdk-for-flutter-navigate-transport-transportmode, /sdk-for-flutter-navigate-transport-transportmode, /sdk-for-flutter-navigate-transport-transportmode.</p>
<p>Attention: The default values for /sdk-for-flutter-navigate-transport-transportmode on /sdk-for-flutter-navigate-navigation-timingprofile are theoretical, as such
routes cannot be calculated with the HERE SDK as highways are forbidden for pedestrians.</p>
<p>Usage example:</p>
<pre class="language-dart"><code>// Get current values or default values, if no values have been set before.
ManeuverNotificationTimingOptions car_highway_timings = Navigator.getManeuverNotificationTimingOptions(TransportMode.car, TimingProfile.FAST_SPEED);
// Set a new value for a specific option and keep the previous or default values for the others.
car_highway_timings.distanceNotificationDistanceInMeters = 1500;
// Apply the changes to Navigator (or VisualNavigator).
Navigator.setManeuverNotificationTimingOptions(TransportMode.CAR, TimingProfile.FAST_SPEED, car_fast_speed_timings);
</code></pre>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="ManeuverNotificationTimingOptions">
/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-maneuvernotificationtimingoptions(int rangeNotificationDistanceInMeters, int rangeNotificationTimeInSeconds, int reminderNotificationDistanceInMeters, int reminderNotificationTimeInSeconds, int distanceNotificationDistanceInMeters, int distanceNotificationTimeInSeconds, int actionNotificationDistanceInMeters, int actionNotificationTimeInSeconds, int doubleNotificationDistanceInMeters)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="actionNotificationDistanceInMeters">
/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-actionnotificationdistanceinmeters
↔ int
</dt>
<dd>
  The default distance setting for /sdk-for-flutter-navigate-navigation-maneuvernotificationtype notification.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="actionNotificationTimeInSeconds">
/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-actionnotificationtimeinseconds
↔ int
</dt>
<dd>
  The default time setting for /sdk-for-flutter-navigate-navigation-maneuvernotificationtype notification.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="distanceNotificationDistanceInMeters">
/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-distancenotificationdistanceinmeters
↔ int
</dt>
<dd>
  The default distance setting for /sdk-for-flutter-navigate-navigation-maneuvernotificationtype notification.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="distanceNotificationTimeInSeconds">
/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-distancenotificationtimeinseconds
↔ int
</dt>
<dd>
  The default time setting for /sdk-for-flutter-navigate-navigation-maneuvernotificationtype notification.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="doubleNotificationDistanceInMeters">
/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-doublenotificationdistanceinmeters
↔ int
</dt>
<dd>
  The default distance setting for double notification.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="rangeNotificationDistanceInMeters">
/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationdistanceinmeters
↔ int
</dt>
<dd>
  The default distance setting for /sdk-for-flutter-navigate-navigation-maneuvernotificationtype notification. A configuration value of 0 is only allowed for
/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationdistanceinmeters and /sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationtimeinseconds. It means that the maneuver notifications of type
/sdk-for-flutter-navigate-navigation-maneuvernotificationtype should be generated as soon as the maneuver location is known - no matter how far away it may be.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="rangeNotificationTimeInSeconds">
/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationtimeinseconds
↔ int
</dt>
<dd>
  The default time setting for /sdk-for-flutter-navigate-navigation-maneuvernotificationtype notification. A configuration value of 0 is only allowed for
/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationdistanceinmeters and /sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-rangenotificationtimeinseconds. It means that the maneuver notifications of type
/sdk-for-flutter-navigate-navigation-maneuvernotificationtype should be generated as soon as the maneuver location is known - no matter how far away it may be.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="reminderNotificationDistanceInMeters">
/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-remindernotificationdistanceinmeters
↔ int
</dt>
<dd>
  The default distance setting for /sdk-for-flutter-navigate-navigation-maneuvernotificationtype notification.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="reminderNotificationTimeInSeconds">
/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-remindernotificationtimeinseconds
↔ int
</dt>
<dd>
  The default time setting for /sdk-for-flutter-navigate-navigation-maneuvernotificationtype notification.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

</dd>
</dl>
</section>
</div> 
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">

<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">ManeuverNotificationTimingOptions class</li>
</ol>
<h5>navigation library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>
