---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-pickmapitemsresult-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- PickMapItemsResult-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/PickMapItemsResult-class.html#constructors">Constructors</a></li>
<li><a href="mapview/PickMapItemsResult/PickMapItemsResult.html">PickMapItemsResult</a></li>
<li class="section-title">
<a href="mapview/PickMapItemsResult-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapview/PickMapItemsResult/clusteredMarkers.html">clusteredMarkers</a></li>
<li class="inherited"><a href="mapview/PickMapItemsResult/hashCode.html">hashCode</a></li>
<li><a href="mapview/PickMapItemsResult/markers.html">markers</a></li>
<li><a href="mapview/PickMapItemsResult/markers3d.html">markers3d</a></li>
<li><a href="mapview/PickMapItemsResult/polygons.html">polygons</a></li>
<li><a href="mapview/PickMapItemsResult/polylines.html">polylines</a></li>
<li class="inherited"><a href="mapview/PickMapItemsResult/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="mapview/PickMapItemsResult-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview/PickMapItemsResult/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/PickMapItemsResult/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/PickMapItemsResult-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/PickMapItemsResult/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">PickMapItemsResult class</li>
</ol>
<div class="self-name">PickMapItemsResult</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/PickMapItemsResult-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>PickMapItemsResult class abstract</h1></div>
<section class="desc markdown">
<p>Carries results from the picking of map items on the map scene.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="PickMapItemsResult">
<a href="../mapview/PickMapItemsResult/PickMapItemsResult.html">/sdk-for-flutter-explore-mapview-pickmapitemsresult-pickmapitemsresult</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="clusteredMarkers">
<a href="../mapview/PickMapItemsResult/clusteredMarkers.html">/sdk-for-flutter-explore-mapview-pickmapitemsresult-clusteredmarkers</a>
→ List&lt;<wbr/><a href="../mapview/MapMarkerClusterGrouping-class.html">/sdk-for-flutter-explore-mapview-mapmarkerclustergrouping-class</a>&gt;
</dt>
<dd>
  List of marker groups (represented by a single cluster marker)
or individual markers belonging to a cluster at the location of picking.
Gets list of clustered marker groups at the location of picking.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
<a href="../mapview/PickMapItemsResult/hashCode.html">/sdk-for-flutter-explore-mapview-pickmapitemsresult-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="markers">
<a href="../mapview/PickMapItemsResult/markers.html">/sdk-for-flutter-explore-mapview-pickmapitemsresult-markers</a>
→ List&lt;<wbr/><a href="../mapview/MapMarker-class.html">/sdk-for-flutter-explore-mapview-mapmarker-class</a>&gt;
</dt>
<dd>
  List of markers at the location of picking.
Gets list of markers at the location of picking.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="markers3d">
<a href="../mapview/PickMapItemsResult/markers3d.html">/sdk-for-flutter-explore-mapview-pickmapitemsresult-markers3d</a>
→ List&lt;<wbr/><a href="../mapview/MapMarker3D-class.html">/sdk-for-flutter-explore-mapview-mapmarker3d-class</a>&gt;
</dt>
<dd>
  List of 3d markers at the location of picking.
Gets list of 3d markers at the location of picking.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="polygons">
<a href="../mapview/PickMapItemsResult/polygons.html">/sdk-for-flutter-explore-mapview-pickmapitemsresult-polygons</a>
→ List&lt;<wbr/><a href="../mapview/MapPolygon-class.html">/sdk-for-flutter-explore-mapview-mappolygon-class</a>&gt;
</dt>
<dd>
  List of polygons at the location of picking.
Gets list of polygons at the location of picking.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="polylines">
<a href="../mapview/PickMapItemsResult/polylines.html">/sdk-for-flutter-explore-mapview-pickmapitemsresult-polylines</a>
→ List&lt;<wbr/><a href="../mapview/MapPolyline-class.html">/sdk-for-flutter-explore-mapview-mappolyline-class</a>&gt;
</dt>
<dd>
  List of polylines at the location of picking.
Gets list of polylines at the location of picking.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview/PickMapItemsResult/runtimeType.html">/sdk-for-flutter-explore-mapview-pickmapitemsresult-runtimetype</a>
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
<a href="../mapview/PickMapItemsResult/noSuchMethod.html">/sdk-for-flutter-explore-mapview-pickmapitemsresult-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview/PickMapItemsResult/toString.html">/sdk-for-flutter-explore-mapview-pickmapitemsresult-tostring</a>(<wbr/>)
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
<a href="../mapview/PickMapItemsResult/operator_equals.html">/sdk-for-flutter-explore-mapview-pickmapitemsresult-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">PickMapItemsResult class</li>
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
