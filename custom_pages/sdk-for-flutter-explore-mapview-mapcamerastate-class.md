---
title: "MapCameraState class"
slug: "sdk-for-flutter-explore-mapview-mapcamerastate-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapCameraState-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapCameraState-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapCameraState/MapCameraState.html">MapCameraState</a></li>
<li class="section-title">
<a href="mapview/MapCameraState-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapview/MapCameraState/distanceToTargetInMeters.html">distanceToTargetInMeters</a></li>
<li class="inherited"><a href="mapview/MapCameraState/hashCode.html">hashCode</a></li>
<li><a href="mapview/MapCameraState/orientationAtTarget.html">orientationAtTarget</a></li>
<li class="inherited"><a href="mapview/MapCameraState/runtimeType.html">runtimeType</a></li>
<li><a href="mapview/MapCameraState/targetCoordinates.html">targetCoordinates</a></li>
<li><a href="mapview/MapCameraState/zoomLevel.html">zoomLevel</a></li>
<li class="section-title inherited"><a href="mapview/MapCameraState-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview/MapCameraState/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/MapCameraState/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/MapCameraState-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapCameraState/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">MapCameraState class</li>
</ol>
<div class="self-name">MapCameraState</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapCameraState-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapCameraState class</h1></div>
<section class="desc markdown">
<p>Encapsulates state of the camera.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapCameraState">
/sdk-for-flutter-explore-mapview-mapcamerastate-mapcamerastate(/sdk-for-flutter-explore-core-geocoordinates-class targetCoordinates, /sdk-for-flutter-explore-core-geoorientation-class orientationAtTarget, double distanceToTargetInMeters, double zoomLevel)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="distanceToTargetInMeters">
/sdk-for-flutter-explore-mapview-mapcamerastate-distancetotargetinmeters
↔ double
</dt>
<dd>
  Distance from the camera to the target point in meters.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-mapview-mapcamerastate-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="orientationAtTarget">
/sdk-for-flutter-explore-mapview-mapcamerastate-orientationattarget
↔ /sdk-for-flutter-explore-core-geoorientation-class
</dt>
<dd>
  Camera's orientation at target point.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-mapview-mapcamerastate-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="targetCoordinates">
/sdk-for-flutter-explore-mapview-mapcamerastate-targetcoordinates
↔ /sdk-for-flutter-explore-core-geocoordinates-class
</dt>
<dd>
  Camera's 'LookAt' target position in geodetic space.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="zoomLevel">
/sdk-for-flutter-explore-mapview-mapcamerastate-zoomlevel
↔ double
</dt>
<dd>
  Zoom level corresponding to the current distance to target.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-mapview-mapcamerastate-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-mapview-mapcamerastate-tostring(<wbr/>)
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
/sdk-for-flutter-explore-mapview-mapcamerastate-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">MapCameraState class</li>
</ol>
<h5>mapview library</h5>
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
