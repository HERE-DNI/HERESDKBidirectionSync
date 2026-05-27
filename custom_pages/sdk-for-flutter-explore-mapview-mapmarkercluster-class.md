---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-mapmarkercluster-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- MapMarkerCluster-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapMarkerCluster-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapMarkerCluster/MapMarkerCluster.html">MapMarkerCluster</a></li>
<li><a href="mapview/MapMarkerCluster/MapMarkerCluster.WithCounter.html">WithCounter</a></li>
<li class="section-title">
<a href="mapview/MapMarkerCluster-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview/MapMarkerCluster/hashCode.html">hashCode</a></li>
<li><a href="mapview/MapMarkerCluster/markers.html">markers</a></li>
<li><a href="mapview/MapMarkerCluster/opacity.html">opacity</a></li>
<li class="inherited"><a href="mapview/MapMarkerCluster/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview/MapMarkerCluster-class.html#instance-methods">Methods</a></li>
<li><a href="mapview/MapMarkerCluster/addMapMarker.html">addMapMarker</a></li>
<li><a href="mapview/MapMarkerCluster/addMapMarkers.html">addMapMarkers</a></li>
<li class="inherited"><a href="mapview/MapMarkerCluster/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="mapview/MapMarkerCluster/removeAllMapMarkers.html">removeAllMapMarkers</a></li>
<li><a href="mapview/MapMarkerCluster/removeMapMarker.html">removeMapMarker</a></li>
<li><a href="mapview/MapMarkerCluster/removeMapMarkers.html">removeMapMarkers</a></li>
<li class="inherited"><a href="mapview/MapMarkerCluster/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/MapMarkerCluster-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapMarkerCluster/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapMarkerCluster class</li>
</ol>
<div class="self-name">MapMarkerCluster</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapMarkerCluster-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapMarkerCluster class abstract</h1></div>
<section class="desc markdown">
<p>Groups map markers and enables their clustering to reduce visual clutter when there are many of
them in a small area.</p>
<p>The markers that are close to each other are replaced by a single cluster marker. Cluster groups
are generated based on geographical distance between objects, not based on screen space collision.
Hence it is possible, that cluster markers can overlap.</p>
<p>The markers can be added to a cluster or to a scene, but not to both. To display the cluster on the
map, add it to the scene using <a href="../mapview/MapScene/addMapMarkerCluster.html">/sdk-for-flutter-explore-mapview-mapscene-addmapmarkercluster</a>. The display of a cluster is only
guaranteed in case its origin is within the viewport. At the moment, this is a known limitation
that mostly affects clusters which are visually large and cover a sizeable part of the viewport.</p>
<p>Markers part of the cluster with opacity set to zero are still on the map and are considered for picking and clustering.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapMarkerCluster">
<a href="../mapview/MapMarkerCluster/MapMarkerCluster.html">/sdk-for-flutter-explore-mapview-mapmarkercluster-mapmarkercluster</a>(<a href="../mapview/MapMarkerClusterImageStyle-class.html">/sdk-for-flutter-explore-mapview-mapmarkerclusterimagestyle-class</a> imageStyle)
</dt>
<dd>
          Creates a new instance of a map marker cluster which is represented as an image.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="MapMarkerCluster.WithCounter">
<a href="../mapview/MapMarkerCluster/MapMarkerCluster.WithCounter.html">/sdk-for-flutter-explore-mapview-mapmarkercluster-mapmarkercluster-withcounter</a>(<a href="../mapview/MapMarkerClusterImageStyle-class.html">/sdk-for-flutter-explore-mapview-mapmarkerclusterimagestyle-class</a> imageStyle, <a href="../mapview/MapMarkerClusterCounterStyle-class.html">/sdk-for-flutter-explore-mapview-mapmarkerclustercounterstyle-class</a> counterStyle)
</dt>
<dd>
          Creates a new instance of a map marker cluster which is represented as an image along with a counter
showing how many markers are actually grouped under particular cluster icon.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../mapview/MapMarkerCluster/hashCode.html">/sdk-for-flutter-explore-mapview-mapmarkercluster-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="markers">
<a href="../mapview/MapMarkerCluster/markers.html">/sdk-for-flutter-explore-mapview-mapmarkercluster-markers</a>
→ List&lt;<wbr/><a href="../mapview/MapMarker-class.html">/sdk-for-flutter-explore-mapview-mapmarker-class</a>&gt;
</dt>
<dd>
  The list of map markers which currently belong to this cluster.
Modifying the list has no effect on the marker cluster.
Returns the list of map markers which currently belong to this cluster.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="opacity">
<a href="../mapview/MapMarkerCluster/opacity.html">/sdk-for-flutter-explore-mapview-mapmarkercluster-opacity</a>
↔ double
</dt>
<dd>
  Opacity is the factor which is applied to the alpha channel of the image used for marker cluster.
Gets the current opacity of the marker cluster image.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview/MapMarkerCluster/runtimeType.html">/sdk-for-flutter-explore-mapview-mapmarkercluster-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="addMapMarker">
<a href="../mapview/MapMarkerCluster/addMapMarker.html">/sdk-for-flutter-explore-mapview-mapmarkercluster-addmapmarker</a>(<wbr/><a href="../mapview/MapMarker-class.html">/sdk-for-flutter-explore-mapview-mapmarker-class</a> marker)
    → void

</dt>
<dd>
  Adds a map marker to this cluster.
  

</dd>
<dt class="callable" id="addMapMarkers">
<a href="../mapview/MapMarkerCluster/addMapMarkers.html">/sdk-for-flutter-explore-mapview-mapmarkercluster-addmapmarkers</a>(<wbr/>List&lt;<wbr/><a href="../mapview/MapMarker-class.html">/sdk-for-flutter-explore-mapview-mapmarker-class</a>&gt; markers)
    → void

</dt>
<dd>
  Adds a list of map markers to this cluster.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview/MapMarkerCluster/noSuchMethod.html">/sdk-for-flutter-explore-mapview-mapmarkercluster-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="removeAllMapMarkers">
<a href="../mapview/MapMarkerCluster/removeAllMapMarkers.html">/sdk-for-flutter-explore-mapview-mapmarkercluster-removeallmapmarkers</a>(<wbr/>)
    → void

</dt>
<dd>
  Removes all map markers from this cluster.
  

</dd>
<dt class="callable" id="removeMapMarker">
<a href="../mapview/MapMarkerCluster/removeMapMarker.html">/sdk-for-flutter-explore-mapview-mapmarkercluster-removemapmarker</a>(<wbr/><a href="../mapview/MapMarker-class.html">/sdk-for-flutter-explore-mapview-mapmarker-class</a> marker)
    → void

</dt>
<dd>
  Removes a map marker from this cluster.
  

</dd>
<dt class="callable" id="removeMapMarkers">
<a href="../mapview/MapMarkerCluster/removeMapMarkers.html">/sdk-for-flutter-explore-mapview-mapmarkercluster-removemapmarkers</a>(<wbr/>List&lt;<wbr/><a href="../mapview/MapMarker-class.html">/sdk-for-flutter-explore-mapview-mapmarker-class</a>&gt; markers)
    → void

</dt>
<dd>
  Removes a list of map markers from this cluster.
  

</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview/MapMarkerCluster/toString.html">/sdk-for-flutter-explore-mapview-mapmarkercluster-tostring</a>(<wbr/>)
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
<a href="../mapview/MapMarkerCluster/operator_equals.html">/sdk-for-flutter-explore-mapview-mapmarkercluster-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">MapMarkerCluster class</li>
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
