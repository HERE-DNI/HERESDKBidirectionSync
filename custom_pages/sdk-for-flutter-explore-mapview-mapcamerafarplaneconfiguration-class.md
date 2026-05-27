---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-mapcamerafarplaneconfiguration-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- MapCameraFarPlaneConfiguration-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapCameraFarPlaneConfiguration-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapCameraFarPlaneConfiguration/MapCameraFarPlaneConfiguration.html">MapCameraFarPlaneConfiguration</a></li>
<li class="section-title">
<a href="mapview/MapCameraFarPlaneConfiguration-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapview/MapCameraFarPlaneConfiguration/distanceFactor.html">distanceFactor</a></li>
<li><a href="mapview/MapCameraFarPlaneConfiguration/hashCode.html">hashCode</a></li>
<li><a href="mapview/MapCameraFarPlaneConfiguration/minDistanceInMeters.html">minDistanceInMeters</a></li>
<li class="inherited"><a href="mapview/MapCameraFarPlaneConfiguration/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="mapview/MapCameraFarPlaneConfiguration-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview/MapCameraFarPlaneConfiguration/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/MapCameraFarPlaneConfiguration/toString.html">toString</a></li>
<li class="section-title"><a href="mapview/MapCameraFarPlaneConfiguration-class.html#operators">Operators</a></li>
<li><a href="mapview/MapCameraFarPlaneConfiguration/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapCameraFarPlaneConfiguration class</li>
</ol>
<div class="self-name">MapCameraFarPlaneConfiguration</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapCameraFarPlaneConfiguration-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapCameraFarPlaneConfiguration class</h1></div>
<section class="desc markdown">
<p>Far plane distance configuration for a zoom level.</p>
<p>Effective far plane is computed from both parameters as:
farPlaneInMeters = max(
minDistanceInMeters,
distanceToTargetInMeters * distanceFactor
)</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapCameraFarPlaneConfiguration">
<a href="../mapview/MapCameraFarPlaneConfiguration/MapCameraFarPlaneConfiguration.html">/sdk-for-flutter-explore-mapview-mapcamerafarplaneconfiguration-mapcamerafarplaneconfiguration</a>(double distanceFactor, double minDistanceInMeters)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="distanceFactor">
<a href="../mapview/MapCameraFarPlaneConfiguration/distanceFactor.html">/sdk-for-flutter-explore-mapview-mapcamerafarplaneconfiguration-distancefactor</a>
↔ double
</dt>
<dd>
  Multiplier applied to the camera distance to target when calculating the far plane.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../mapview/MapCameraFarPlaneConfiguration/hashCode.html">/sdk-for-flutter-explore-mapview-mapcamerafarplaneconfiguration-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="minDistanceInMeters">
<a href="../mapview/MapCameraFarPlaneConfiguration/minDistanceInMeters.html">/sdk-for-flutter-explore-mapview-mapcamerafarplaneconfiguration-mindistanceinmeters</a>
↔ double
</dt>
<dd>
  Minimum far plane clamp in meters.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview/MapCameraFarPlaneConfiguration/runtimeType.html">/sdk-for-flutter-explore-mapview-mapcamerafarplaneconfiguration-runtimetype</a>
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
<a href="../mapview/MapCameraFarPlaneConfiguration/noSuchMethod.html">/sdk-for-flutter-explore-mapview-mapcamerafarplaneconfiguration-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview/MapCameraFarPlaneConfiguration/toString.html">/sdk-for-flutter-explore-mapview-mapcamerafarplaneconfiguration-tostring</a>(<wbr/>)
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
<a href="../mapview/MapCameraFarPlaneConfiguration/operator_equals.html">/sdk-for-flutter-explore-mapview-mapcamerafarplaneconfiguration-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapCameraFarPlaneConfiguration class</li>
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
