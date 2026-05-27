---
title: "Constructors"
slug: "sdk-for-flutter-explore-core-location-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- Location-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core/Location-class.html#constructors">Constructors</a></li>
<li><a href="core/Location/Location.withCoordinates.html">withCoordinates</a></li>
<li class="section-title">
<a href="core/Location-class.html#instance-properties">Properties</a>
</li>
<li><a href="core/Location/bearingAccuracyInDegrees.html">bearingAccuracyInDegrees</a></li>
<li><a href="core/Location/bearingInDegrees.html">bearingInDegrees</a></li>
<li><a href="core/Location/coordinates.html">coordinates</a></li>
<li><a href="core/Location/gnssTime.html">gnssTime</a></li>
<li><a href="core/Location/hashCode.html">hashCode</a></li>
<li><a href="core/Location/horizontalAccuracyInMeters.html">horizontalAccuracyInMeters</a></li>
<li><a href="core/Location/locationTechnology.html">locationTechnology</a></li>
<li><a href="core/Location/pitchInDegrees.html">pitchInDegrees</a></li>
<li class="inherited"><a href="core/Location/runtimeType.html">runtimeType</a></li>
<li><a href="core/Location/source.html">source</a></li>
<li><a href="core/Location/speedAccuracyInMetersPerSecond.html">speedAccuracyInMetersPerSecond</a></li>
<li><a href="core/Location/speedInMetersPerSecond.html">speedInMetersPerSecond</a></li>
<li><a href="core/Location/time.html">time</a></li>
<li><a href="core/Location/timestampSinceBoot.html">timestampSinceBoot</a></li>
<li><a href="core/Location/verticalAccuracyInMeters.html">verticalAccuracyInMeters</a></li>
<li class="section-title inherited"><a href="core/Location-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="core/Location/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core/Location/toString.html">toString</a></li>
<li class="section-title"><a href="core/Location-class.html#operators">Operators</a></li>
<li><a href="core/Location/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
<li class="self-crumb">Location class</li>
</ol>
<div class="self-name">Location</div>
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
<div class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/Location-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>Location class</h1></div>
<section class="desc markdown">
<p>Describes a location in the world at a given time.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Location.withCoordinates">
<a href="../core/Location/Location.withCoordinates.html">/sdk-for-flutter-explore-core-location-location-withcoordinates</a>(<a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> coordinates)
</dt>
<dd>
          Creates a new Location instance from the provided GeoCoordinates value.
timestamp is initialized with <code>January 1, 1970, 00:00:00 GMT</code> value.
The rest of the fields will be initialized to null.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="bearingAccuracyInDegrees">
<a href="../core/Location/bearingAccuracyInDegrees.html">/sdk-for-flutter-explore-core-location-bearingaccuracyindegrees</a>
↔ double?
</dt>
<dd>
  Estimated bearing accuracy for this location, in degrees.
If it cannot be determined, the value is <code>null</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="bearingInDegrees">
<a href="../core/Location/bearingInDegrees.html">/sdk-for-flutter-explore-core-location-bearingindegrees</a>
↔ double?
</dt>
<dd>
  Bearing (also known as course) is the device's horizontal direction of travel.
Starts at 0 in the geographical north and rotates around the compass in a clockwise
direction. This means for going north it is equal to 0, for northeast it is 45,
for east it is 90 and so on. Note that this may be different from the orientation of
the device. If it cannot be determined, the value is <code>null</code>. Otherwise, it is
guaranteed to be in the range [0, 360).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="coordinates">
<a href="../core/Location/coordinates.html">/sdk-for-flutter-explore-core-location-coordinates</a>
↔ <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>
</dt>
<dd>
  The geographic coordinates of the location.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="gnssTime">
<a href="../core/Location/gnssTime.html">/sdk-for-flutter-explore-core-location-gnsstime</a>
↔ Duration?
</dt>
<dd>
  Optional gnss time at which the location was determined.
It is a time interval from the Unix time epoch in milliseconds.
If it cannot be determined, the value is <code>null</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../core/Location/hashCode.html">/sdk-for-flutter-explore-core-location-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="horizontalAccuracyInMeters">
<a href="../core/Location/horizontalAccuracyInMeters.html">/sdk-for-flutter-explore-core-location-horizontalaccuracyinmeters</a>
↔ double?
</dt>
<dd>
  The estimated horizontal accuracy. The actual location will lie within this radius of uncertainty.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="locationTechnology">
<a href="../core/Location/locationTechnology.html">/sdk-for-flutter-explore-core-location-locationtechnology</a>
↔ <a href="../core/LocationTechnology.html">/sdk-for-flutter-explore-core-locationtechnology</a>?
</dt>
<dd>
  Optional technology or provider of this location.
If it cannot be determined, the value is <code>null</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="pitchInDegrees">
<a href="../core/Location/pitchInDegrees.html">/sdk-for-flutter-explore-core-location-pitchindegrees</a>
↔ double?
</dt>
<dd>
  Pitch of this location, in degrees.
If it cannot be determined, the value is <code>null</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../core/Location/runtimeType.html">/sdk-for-flutter-explore-core-location-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="source">
<a href="../core/Location/source.html">/sdk-for-flutter-explore-core-location-source</a>
↔ <a href="../core/LocationSource.html">/sdk-for-flutter-explore-core-locationsource</a>?
</dt>
<dd>
  Optional source of this location.
If it cannot be determined, the value is <code>null</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="speedAccuracyInMetersPerSecond">
<a href="../core/Location/speedAccuracyInMetersPerSecond.html">/sdk-for-flutter-explore-core-location-speedaccuracyinmeterspersecond</a>
↔ double?
</dt>
<dd>
  Estimated speed accuracy of this location, in meters per second.
If it cannot be determined, the value is <code>null</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="speedInMetersPerSecond">
<a href="../core/Location/speedInMetersPerSecond.html">/sdk-for-flutter-explore-core-location-speedinmeterspersecond</a>
↔ double?
</dt>
<dd>
  Current speed of the device. If it cannot be determined, the value is <code>null</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="time">
<a href="../core/Location/time.html">/sdk-for-flutter-explore-core-location-time</a>
↔ DateTime?
</dt>
<dd>
  The time at which the location was determined.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="timestampSinceBoot">
<a href="../core/Location/timestampSinceBoot.html">/sdk-for-flutter-explore-core-location-timestampsinceboot</a>
↔ Duration?
</dt>
<dd>
  The time at which the location was determined, relative to device
boot time. This time is monotonic and not affected by leap time or other system
time adjustments, so this is the recommended basis for general purpose interval timing
between location updates.
If it cannot be determined, the value is <code>null</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="verticalAccuracyInMeters">
<a href="../core/Location/verticalAccuracyInMeters.html">/sdk-for-flutter-explore-core-location-verticalaccuracyinmeters</a>
↔ double?
</dt>
<dd>
  Estimated vertical accuracy.
Given that the received Location contains the altitude, the real value of the altitude
is estimated to lie within the following range:
[altitude - vertical accuracy, altitude + vertical accuracy].
For example, when the altitude is equal to 50 and the vertical accuracy
is 8, then the actual value is most likely in the range [42, 58].
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../core/Location/noSuchMethod.html">/sdk-for-flutter-explore-core-location-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../core/Location/toString.html">/sdk-for-flutter-explore-core-location-tostring</a>(<wbr/>)
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
<a href="../core/Location/operator_equals.html">/sdk-for-flutter-explore-core-location-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
<li class="self-crumb">Location class</li>
</ol>
<h5>core library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
</HTMLBlock>
