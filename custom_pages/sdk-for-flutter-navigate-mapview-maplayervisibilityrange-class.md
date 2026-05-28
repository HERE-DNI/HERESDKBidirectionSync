---
title: "MapLayerVisibilityRange class"
slug: "sdk-for-flutter-navigate-mapview-maplayervisibilityrange-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapLayerVisibilityRange-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapLayerVisibilityRange-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapLayerVisibilityRange/MapLayerVisibilityRange.html">MapLayerVisibilityRange</a></li>
<li class="section-title">
<a href="mapview/MapLayerVisibilityRange-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapview/MapLayerVisibilityRange/hashCode.html">hashCode</a></li>
<li><a href="mapview/MapLayerVisibilityRange/maximumZoomLevel.html">maximumZoomLevel</a></li>
<li><a href="mapview/MapLayerVisibilityRange/minimumZoomLevel.html">minimumZoomLevel</a></li>
<li class="inherited"><a href="mapview/MapLayerVisibilityRange/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="mapview/MapLayerVisibilityRange-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview/MapLayerVisibilityRange/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/MapLayerVisibilityRange/toString.html">toString</a></li>
<li class="section-title"><a href="mapview/MapLayerVisibilityRange-class.html#operators">Operators</a></li>
<li><a href="mapview/MapLayerVisibilityRange/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">MapLayerVisibilityRange class</li>
</ol>
<div class="self-name">MapLayerVisibilityRange</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapLayerVisibilityRange-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapLayerVisibilityRange class</h1></div>
<section class="desc markdown">
<p>A layer's visibility along a zoom level range.</p>
<p>The range is half open - [minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Annotations</dt>
<dd>
<ul class="annotation-list clazz-relationships">
<li>@<a href="https://pub.dev/documentation/meta/1.17.0/meta/immutable-constant.html">immutable</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapLayerVisibilityRange">
/sdk-for-flutter-navigate-mapview-maplayervisibilityrange-maplayervisibilityrange(double minimumZoomLevel, double maximumZoomLevel)
</dt>
<dd>
          Creates a new instance.
            <div class="constructor-modifier features">const</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-mapview-maplayervisibilityrange-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="maximumZoomLevel">
/sdk-for-flutter-navigate-mapview-maplayervisibilityrange-maximumzoomlevel
→ double
</dt>
<dd>
  Minimum zoom level from which the layer will not be visible. The value must be less than or equal to the <code>MapCameraLimits.MAX_ZOOM_LEVEL</code>.
Note that the map layer is not visible at the maximum zoom level.
  <div class="features">final</div>
</dd>
<dt class="property" id="minimumZoomLevel">
/sdk-for-flutter-navigate-mapview-maplayervisibilityrange-minimumzoomlevel
→ double
</dt>
<dd>
  Minimum zoom level on which the layer will be visible. The value must be greater than or equal to the <code>MapCameraLimits.MIN_ZOOM_LEVEL</code>.
  <div class="features">final</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapview-maplayervisibilityrange-runtimetype
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
/sdk-for-flutter-navigate-mapview-maplayervisibilityrange-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapview-maplayervisibilityrange-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-mapview-maplayervisibilityrange-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">MapLayerVisibilityRange class</li>
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
