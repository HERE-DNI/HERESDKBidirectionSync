---
title: "MapCameraLimits class abstract"
slug: "sdk-for-flutter-navigate-mapview-mapcameralimits-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapCameraLimits-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapCameraLimits-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapCameraLimits/MapCameraLimits.html">MapCameraLimits</a></li>
<li class="section-title">
<a href="mapview/MapCameraLimits-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapview/MapCameraLimits/bearingRange.html">bearingRange</a></li>
<li class="inherited"><a href="mapview/MapCameraLimits/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview/MapCameraLimits/runtimeType.html">runtimeType</a></li>
<li><a href="mapview/MapCameraLimits/targetArea.html">targetArea</a></li>
<li><a href="mapview/MapCameraLimits/tiltRange.html">tiltRange</a></li>
<li><a href="mapview/MapCameraLimits/zoomRange.html">zoomRange</a></li>
<li class="section-title"><a href="mapview/MapCameraLimits-class.html#instance-methods">Methods</a></li>
<li><a href="mapview/MapCameraLimits/clearBearingRanges.html">clearBearingRanges</a></li>
<li><a href="mapview/MapCameraLimits/clearTiltRanges.html">clearTiltRanges</a></li>
<li class="inherited"><a href="mapview/MapCameraLimits/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="mapview/MapCameraLimits/setBearingRangeAtZoom.html">setBearingRangeAtZoom</a></li>
<li><a href="mapview/MapCameraLimits/setTiltRangeAtZoom.html">setTiltRangeAtZoom</a></li>
<li class="inherited"><a href="mapview/MapCameraLimits/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/MapCameraLimits-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapCameraLimits/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="mapview/MapCameraLimits-class.html#static-properties">Static properties</a></li>
<li><a href="mapview/MapCameraLimits/maxTilt.html">maxTilt</a></li>
<li><a href="mapview/MapCameraLimits/maxZoomLevel.html">maxZoomLevel</a></li>
<li><a href="mapview/MapCameraLimits/minTilt.html">minTilt</a></li>
<li><a href="mapview/MapCameraLimits/minZoomLevel.html">minZoomLevel</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">MapCameraLimits class</li>
</ol>
<div class="self-name">MapCameraLimits</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapCameraLimits-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapCameraLimits class abstract</h1></div>
<section class="desc markdown">
<p>Controls constraints on map camera parameters.</p>
<p>When constraints are set, they are enforced for current camera state
and for all future changes to the camera.</p>
<p>When setting, limits are applied on next rendering loop.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapCameraLimits">
/sdk-for-flutter-navigate-mapview-mapcameralimits-mapcameralimits()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="bearingRange">
/sdk-for-flutter-navigate-mapview-mapcameralimits-bearingrange
↔ /sdk-for-flutter-navigate-core-anglerange-class
</dt>
<dd>
  The bearing range within which the camera can be rotated.
Gets the currently set bearing range.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-mapview-mapcameralimits-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapview-mapcameralimits-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="targetArea">
/sdk-for-flutter-navigate-mapview-mapcameralimits-targetarea
↔ /sdk-for-flutter-navigate-core-geobox-class?
</dt>
<dd>
  Geographical area to which the camera target is limited.
Gets a GeoBox that limits the camera target to a specific geographical area. Absence of a value means that there is no limit.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="tiltRange">
/sdk-for-flutter-navigate-mapview-mapcameralimits-tiltrange
↔ /sdk-for-flutter-navigate-core-anglerange-class
</dt>
<dd>
  The tilt range that can be applied to the camera.
Gets the current tilt range.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="zoomRange">
/sdk-for-flutter-navigate-mapview-mapcameralimits-zoomrange
↔ /sdk-for-flutter-navigate-mapview-mapmeasurerange-class
</dt>
<dd>
  The zoom range that can be applied to the camera.
Gets the currently set camera zoom range.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="clearBearingRanges">
/sdk-for-flutter-navigate-mapview-mapcameralimits-clearbearingranges(<wbr/>)
    → void

</dt>
<dd>
  Clears bearing ranges for all zoom values and resets /sdk-for-flutter-navigate-mapview-mapcameralimits-bearingrange
to default.
  

</dd>
<dt class="callable" id="clearTiltRanges">
/sdk-for-flutter-navigate-mapview-mapcameralimits-cleartiltranges(<wbr/>)
    → void

</dt>
<dd>
  Clears tilt ranges for all zoom values and resets /sdk-for-flutter-navigate-mapview-mapcameralimits-tiltrange  to default.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapview-mapcameralimits-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="setBearingRangeAtZoom">
/sdk-for-flutter-navigate-mapview-mapcameralimits-setbearingrangeatzoom(<wbr/>/sdk-for-flutter-navigate-mapview-mapmeasure-class zoom, /sdk-for-flutter-navigate-core-anglerange-class bearingRange)
    → void

</dt>
<dd>
  Sets the bearing range within which the camera can rotate at a given zoom.
  

</dd>
<dt class="callable" id="setTiltRangeAtZoom">
/sdk-for-flutter-navigate-mapview-mapcameralimits-settiltrangeatzoom(<wbr/>/sdk-for-flutter-navigate-mapview-mapmeasure-class zoom, /sdk-for-flutter-navigate-core-anglerange-class tiltRange)
    → void

</dt>
<dd>
  Sets tilt ranges that can be set on the camera at given zoom.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapview-mapcameralimits-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-mapview-mapcameralimits-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-properties">
<h2>Static Properties</h2>
<dl class="properties">
<dt class="property" id="maxTilt">
/sdk-for-flutter-navigate-mapview-mapcameralimits-maxtilt
→ double
</dt>
<dd>
  Absolute maximum possible value of tilt angle.
  <div class="features">final</div>
</dd>
<dt class="property" id="maxZoomLevel">
/sdk-for-flutter-navigate-mapview-mapcameralimits-maxzoomlevel
→ double
</dt>
<dd>
  Absolute maximum possible value of zoom level.
  <div class="features">final</div>
</dd>
<dt class="property" id="minTilt">
/sdk-for-flutter-navigate-mapview-mapcameralimits-mintilt
→ double
</dt>
<dd>
  Absolute minimum possible value of tilt angle.
  <div class="features">final</div>
</dd>
<dt class="property" id="minZoomLevel">
/sdk-for-flutter-navigate-mapview-mapcameralimits-minzoomlevel
→ double
</dt>
<dd>
  Absolute minimum possible value of zoom level.
  <div class="features">final</div>
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
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">MapCameraLimits class</li>
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
