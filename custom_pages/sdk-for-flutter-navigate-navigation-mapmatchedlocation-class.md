---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-mapmatchedlocation-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMatchedLocation-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">MapMatchedLocation class</li>
</ol>
<div class="self-name">MapMatchedLocation</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/MapMatchedLocation-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapMatchedLocation class</h1></div>
<section class="desc markdown">
<p>Describes a map-matched location in the world at a given time.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapMatchedLocation">
/sdk-for-flutter-navigate-navigation-mapmatchedlocation-mapmatchedlocation(/sdk-for-flutter-navigate-core-geocoordinates-class coordinates, double? bearingInDegrees)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="bearingInDegrees">
/sdk-for-flutter-navigate-navigation-mapmatchedlocation-bearingindegrees
↔ double?
</dt>
<dd>
  The bearing orientation points to the direction of travel, and has the same angle as the
street where it is matched to. Therefore, it must not necessarily be the same as the
bearing of a location source.
Starts at 0 in the geographic north and rotates in a clockwise direction around the
compass. It means that for going north it's equal to 0, for northeast it's equal to 45,
for east it's equal to 90, and so on.
If it cannot be determined, the value is <code>null</code>. Otherwise, it is guaranteed to be in the
range [0, 360).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="confidence">
/sdk-for-flutter-navigate-navigation-mapmatchedlocation-confidence
↔ double
</dt>
<dd>
  Confidence level (between 0 and 1) of the matched location.
A low confidence value means that the map-matched vehicle location is not reliable and it may
not be clear which part of the road the vehicle has taken. This can happen when the accuracy
or frequency of the provided location updates is poor. If the confidence level is too small
then, for example, overspeed warnings may be also inaccurate.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="coordinates">
/sdk-for-flutter-navigate-navigation-mapmatchedlocation-coordinates
↔ /sdk-for-flutter-navigate-core-geocoordinates-class
</dt>
<dd>
  The geographic coordinates of the map-matched location.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-mapmatchedlocation-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="horizontalAccuracyInMeters">
/sdk-for-flutter-navigate-navigation-mapmatchedlocation-horizontalaccuracyinmeters
↔ double?
</dt>
<dd>
  Horizontal accuracy measure of location.
Estimated based on accuracy of input location and confidence of this map-matched location.
Currently this value is not being provided by the Navigator.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isDrivingInTheWrongWay">
/sdk-for-flutter-navigate-navigation-mapmatchedlocation-isdrivinginthewrongway
↔ bool
</dt>
<dd>
  Determines if the travel direction on a one-way street is against the allowed traffic direction.
For two-way streets, this value is always <code>false</code>.
This feature is supported in tracking mode and when deviating from a route.
Note that the travel direction is determined based on the map-matched location.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-mapmatchedlocation-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="segmentOffsetInCentimeters">
/sdk-for-flutter-navigate-navigation-mapmatchedlocation-segmentoffsetincentimeters
↔ int
</dt>
<dd>
  Offset from start of segment in centimeters.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="segmentReference">
/sdk-for-flutter-navigate-navigation-mapmatchedlocation-segmentreference
↔ /sdk-for-flutter-navigate-routing-segmentreference-class
</dt>
<dd>
  Reference to the current segment.
The ratio of /sdk-for-flutter-navigate-navigation-mapmatchedlocation-segmentoffsetincentimeters to the segment length is
between /sdk-for-flutter-navigate-routing-segmentreference-offsetstart and /sdk-for-flutter-navigate-routing-segmentreference-offsetend.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="speedInMetersPerSecond">
/sdk-for-flutter-navigate-navigation-mapmatchedlocation-speedinmeterspersecond
↔ double?
</dt>
<dd>
  Speed in meters per second.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="timestamp">
/sdk-for-flutter-navigate-navigation-mapmatchedlocation-timestamp
↔ DateTime?
</dt>
<dd>
  Timestamp of the map matched position.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-mapmatchedlocation-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-mapmatchedlocation-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-mapmatchedlocation-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">MapMatchedLocation class</li>
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
