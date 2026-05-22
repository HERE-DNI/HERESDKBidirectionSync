---
title: "Untitled"
slug: "sdk-for-flutter-navigate-location-notificationoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- NotificationOptions-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li class="self-crumb">NotificationOptions class</li>
</ol>
<div class="self-name">NotificationOptions</div>
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
<div class="main-content" data-above-sidebar="location/location-library-sidebar.html" data-below-sidebar="location/NotificationOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>NotificationOptions class</h1></div>
<section class="desc markdown">
<p>Positioning notification options.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="NotificationOptions">
/sdk-for-flutter-navigate-location-notificationoptions-notificationoptions()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="desiredIntervalMilliseconds">
/sdk-for-flutter-navigate-location-notificationoptions-desiredintervalmilliseconds
↔ int
</dt>
<dd>
  Desired interval for position updates in milliseconds. This interval
is not guaranteed.
Default interval is 30 seconds.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-location-notificationoptions-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-location-notificationoptions-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="smallestIntervalMilliseconds">
/sdk-for-flutter-navigate-location-notificationoptions-smallestintervalmilliseconds
↔ int
</dt>
<dd>
  Smallest allowed interval for position updates in milliseconds.  It is
guaranteed that positions are not provided more often than this value.
Smallest interval could be used for throttling position updates, e.g.
when each position update triggers CPU intensive calculations in the
client application. This value is used as a minimum update interval
when requesting GNSS location updates from the operating system.
When hdEnabled is set to <code>true</code> in SatellitePositioningOptions, the
smallest_interval_milliseconds value has a limited range. The SDK will
adjust the value to allow location updates with a frequency of 1Hz to
10Hz (1000 ms to 100 ms, respectively).
Default interval is 900 milliseconds.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-location-notificationoptions-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-location-notificationoptions-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-location-notificationoptions-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
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
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li class="self-crumb">NotificationOptions class</li>
</ol>
<h5>location library</h5>
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
