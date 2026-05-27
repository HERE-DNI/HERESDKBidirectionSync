---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-mapcameralimits-class"
---

<HTMLBlock>
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
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
<a href="../mapview/MapCameraLimits/MapCameraLimits.html">/sdk-for-flutter-explore-mapview-mapcameralimits-mapcameralimits</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="bearingRange">
<a href="../mapview/MapCameraLimits/bearingRange.html">/sdk-for-flutter-explore-mapview-mapcameralimits-bearingrange</a>
↔ <a href="../core/AngleRange-class.html">/sdk-for-flutter-explore-core-anglerange-class</a>
</dt>
<dd>
  The bearing range within which the camera can be rotated.
Gets the currently set bearing range.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
<a href="../mapview/MapCameraLimits/hashCode.html">/sdk-for-flutter-explore-mapview-mapcameralimits-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview/MapCameraLimits/runtimeType.html">/sdk-for-flutter-explore-mapview-mapcameralimits-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="targetArea">
<a href="../mapview/MapCameraLimits/targetArea.html">/sdk-for-flutter-explore-mapview-mapcameralimits-targetarea</a>
↔ <a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>?
</dt>
<dd>
  Geographical area to which the camera target is limited.
Gets a GeoBox that limits the camera target to a specific geographical area. Absence of a value means that there is no limit.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="tiltRange">
<a href="../mapview/MapCameraLimits/tiltRange.html">/sdk-for-flutter-explore-mapview-mapcameralimits-tiltrange</a>
↔ <a href="../core/AngleRange-class.html">/sdk-for-flutter-explore-core-anglerange-class</a>
</dt>
<dd>
  The tilt range that can be applied to the camera.
Gets the current tilt range.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="zoomRange">
<a href="../mapview/MapCameraLimits/zoomRange.html">/sdk-for-flutter-explore-mapview-mapcameralimits-zoomrange</a>
↔ <a href="../mapview/MapMeasureRange-class.html">/sdk-for-flutter-explore-mapview-mapmeasurerange-class</a>
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
<a href="../mapview/MapCameraLimits/clearBearingRanges.html">/sdk-for-flutter-explore-mapview-mapcameralimits-clearbearingranges</a>(<wbr/>)
    → void

</dt>
<dd>
  Clears bearing ranges for all zoom values and resets <a href="../mapview/MapCameraLimits/bearingRange.html">/sdk-for-flutter-explore-mapview-mapcameralimits-bearingrange</a>
to default.
  

</dd>
<dt class="callable" id="clearTiltRanges">
<a href="../mapview/MapCameraLimits/clearTiltRanges.html">/sdk-for-flutter-explore-mapview-mapcameralimits-cleartiltranges</a>(<wbr/>)
    → void

</dt>
<dd>
  Clears tilt ranges for all zoom values and resets <a href="../mapview/MapCameraLimits/tiltRange.html">/sdk-for-flutter-explore-mapview-mapcameralimits-tiltrange</a>  to default.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview/MapCameraLimits/noSuchMethod.html">/sdk-for-flutter-explore-mapview-mapcameralimits-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="setBearingRangeAtZoom">
<a href="../mapview/MapCameraLimits/setBearingRangeAtZoom.html">/sdk-for-flutter-explore-mapview-mapcameralimits-setbearingrangeatzoom</a>(<wbr/><a href="../mapview/MapMeasure-class.html">/sdk-for-flutter-explore-mapview-mapmeasure-class</a> zoom, <a href="../core/AngleRange-class.html">/sdk-for-flutter-explore-core-anglerange-class</a> bearingRange)
    → void

</dt>
<dd>
  Sets the bearing range within which the camera can rotate at a given zoom.
  

</dd>
<dt class="callable" id="setTiltRangeAtZoom">
<a href="../mapview/MapCameraLimits/setTiltRangeAtZoom.html">/sdk-for-flutter-explore-mapview-mapcameralimits-settiltrangeatzoom</a>(<wbr/><a href="../mapview/MapMeasure-class.html">/sdk-for-flutter-explore-mapview-mapmeasure-class</a> zoom, <a href="../core/AngleRange-class.html">/sdk-for-flutter-explore-core-anglerange-class</a> tiltRange)
    → void

</dt>
<dd>
  Sets tilt ranges that can be set on the camera at given zoom.
  

</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview/MapCameraLimits/toString.html">/sdk-for-flutter-explore-mapview-mapcameralimits-tostring</a>(<wbr/>)
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
<a href="../mapview/MapCameraLimits/operator_equals.html">/sdk-for-flutter-explore-mapview-mapcameralimits-operator-equals</a>(<wbr/>Object other)
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
<a href="../mapview/MapCameraLimits/maxTilt.html">/sdk-for-flutter-explore-mapview-mapcameralimits-maxtilt</a>
→ double
</dt>
<dd>
  Absolute maximum possible value of tilt angle.
  <div class="features">final</div>
</dd>
<dt class="property" id="maxZoomLevel">
<a href="../mapview/MapCameraLimits/maxZoomLevel.html">/sdk-for-flutter-explore-mapview-mapcameralimits-maxzoomlevel</a>
→ double
</dt>
<dd>
  Absolute maximum possible value of zoom level.
  <div class="features">final</div>
</dd>
<dt class="property" id="minTilt">
<a href="../mapview/MapCameraLimits/minTilt.html">/sdk-for-flutter-explore-mapview-mapcameralimits-mintilt</a>
→ double
</dt>
<dd>
  Absolute minimum possible value of tilt angle.
  <div class="features">final</div>
</dd>
<dt class="property" id="minZoomLevel">
<a href="../mapview/MapCameraLimits/minZoomLevel.html">/sdk-for-flutter-explore-mapview-mapcameralimits-minzoomlevel</a>
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
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
</HTMLBlock>
