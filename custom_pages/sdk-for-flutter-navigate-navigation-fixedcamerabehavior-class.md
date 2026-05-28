---
title: "FixedCameraBehavior class abstract"
slug: "sdk-for-flutter-navigate-navigation-fixedcamerabehavior-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- FixedCameraBehavior-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/FixedCameraBehavior-class.html#constructors">Constructors</a></li>
<li><a href="navigation/FixedCameraBehavior/FixedCameraBehavior.html">FixedCameraBehavior</a></li>
<li class="section-title">
<a href="navigation/FixedCameraBehavior-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/FixedCameraBehavior/cameraBearingInDegrees.html">cameraBearingInDegrees</a></li>
<li><a class="deprecated" href="navigation/FixedCameraBehavior/cameraDistanceInMeters.html">cameraDistanceInMeters</a></li>
<li><a href="navigation/FixedCameraBehavior/cameraTiltInDegrees.html">cameraTiltInDegrees</a></li>
<li class="inherited"><a href="navigation/CameraBehavior/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="navigation/CameraBehavior/normalizedPrincipalPoint.html">normalizedPrincipalPoint</a></li>
<li class="inherited"><a href="navigation/CameraBehavior/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/FixedCameraBehavior/zoom.html">zoom</a></li>
<li class="section-title inherited"><a href="navigation/FixedCameraBehavior-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/CameraBehavior/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/CameraBehavior/toString.html">toString</a></li>
<li class="section-title inherited"><a href="navigation/FixedCameraBehavior-class.html#operators">Operators</a></li>
<li class="inherited"><a href="navigation/CameraBehavior/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">FixedCameraBehavior class</li>
</ol>
<div class="self-name">FixedCameraBehavior</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/FixedCameraBehavior-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>FixedCameraBehavior class abstract</h1></div>
<section class="desc markdown">
<p>Use this class to follow the current location of the user: The camera will permanently look at
the target location that was fed into the navigator instance.</p>
<p>Since location updates happen in
discrete intervals, locations in-between will be interpolated to achieve a smooth camera
movement.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implemented types</dt>
<dd>
<ul class="comma-separated clazz-relationships">
<li>/sdk-for-flutter-navigate-navigation-camerabehavior-class</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="FixedCameraBehavior">
/sdk-for-flutter-navigate-navigation-fixedcamerabehavior-fixedcamerabehavior()
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="cameraBearingInDegrees">
/sdk-for-flutter-navigate-navigation-fixedcamerabehavior-camerabearingindegrees
↔ double?
</dt>
<dd>
  Camera bearing in degrees.
Optional fixed bearing, from true North (0 degrees) in clockwise direction. The valid range
is [0, 360].
If set, it will prevent the map from rotating to the direction of travel. For example, a
value of zero results in "north up" mode.
Defaults to <code>null</code>, which means the camera derives the bearing from the /sdk-for-flutter-navigate-core-location-class,
so that it points to the direction of travel.
If this property is <code>null</code> and the device does not provide bearing, the last known value is
used or zero otherwise.
Gets the currently set fixed bearing.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="cameraDistanceInMeters">
/sdk-for-flutter-navigate-navigation-fixedcamerabehavior-cameradistanceinmeters
↔ double
</dt>
<dd>
  Camera distance in meters.
Camera distance to current location. The default value is 150 meters.
Gets the currently set camera distance to current location. The default value is 150 meters.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="cameraTiltInDegrees">
/sdk-for-flutter-navigate-navigation-fixedcamerabehavior-cameratiltindegrees
↔ double
</dt>
<dd>
  Camera tilt with axis parallel to the ground.
The default value is 50 degrees.
Gets the currently set camera tilt with axis parallel to the ground. The default value is 50 degrees.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-navigation-camerabehavior-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="normalizedPrincipalPoint">
/sdk-for-flutter-navigate-navigation-camerabehavior-normalizedprincipalpoint
↔ /sdk-for-flutter-navigate-core-anchor2d-class
</dt>
<dd class="inherited">
  The normalized principal point.
Normalized principal point to be used during navigation.
Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom
of the mapview.
Gets the currently set normalized principal point to be used during navigation.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-camerabehavior-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="zoom">
/sdk-for-flutter-navigate-navigation-fixedcamerabehavior-zoom
↔ /sdk-for-flutter-navigate-mapview-mapmeasure-class
</dt>
<dd>
  Zoom configuration. The default value is 150 meters.
Camera zoom configuration. The default value is 150 meters.
Note: /sdk-for-flutter-navigate-mapview-mapmeasurekind is not supported.
Gets the current camera's zoom configuration.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-camerabehavior-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-camerabehavior-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-camerabehavior-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">FixedCameraBehavior class</li>
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
</div></div>
</div>
`
}</HTMLBlock>
