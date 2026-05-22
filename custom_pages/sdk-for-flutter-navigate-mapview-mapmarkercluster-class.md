---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mapmarkercluster-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarkerCluster-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
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
map, add it to the scene using /sdk-for-flutter-navigate-mapview-mapscene-addmapmarkercluster. The display of a cluster is only
guaranteed in case its origin is within the viewport. At the moment, this is a known limitation
that mostly affects clusters which are visually large and cover a sizeable part of the viewport.</p>
<p>Markers part of the cluster with opacity set to zero are still on the map and are considered for picking and clustering.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapMarkerCluster">
/sdk-for-flutter-navigate-mapview-mapmarkercluster-mapmarkercluster(/sdk-for-flutter-navigate-mapview-mapmarkerclusterimagestyle-class imageStyle)
</dt>
<dd>
          Creates a new instance of a map marker cluster which is represented as an image.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="MapMarkerCluster.WithCounter">
/sdk-for-flutter-navigate-mapview-mapmarkercluster-mapmarkercluster-withcounter(/sdk-for-flutter-navigate-mapview-mapmarkerclusterimagestyle-class imageStyle, /sdk-for-flutter-navigate-mapview-mapmarkerclustercounterstyle-class counterStyle)
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
/sdk-for-flutter-navigate-mapview-mapmarkercluster-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="markers">
/sdk-for-flutter-navigate-mapview-mapmarkercluster-markers
→ List&lt;<wbr/>/sdk-for-flutter-navigate-mapview-mapmarker-class&gt;
</dt>
<dd>
  The list of map markers which currently belong to this cluster.
Modifying the list has no effect on the marker cluster.
Returns the list of map markers which currently belong to this cluster.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="opacity">
/sdk-for-flutter-navigate-mapview-mapmarkercluster-opacity
↔ double
</dt>
<dd>
  Opacity is the factor which is applied to the alpha channel of the image used for marker cluster.
Gets the current opacity of the marker cluster image.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapview-mapmarkercluster-runtimetype
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
/sdk-for-flutter-navigate-mapview-mapmarkercluster-addmapmarker(<wbr/>/sdk-for-flutter-navigate-mapview-mapmarker-class marker)
    → void

</dt>
<dd>
  Adds a map marker to this cluster.
  

</dd>
<dt class="callable" id="addMapMarkers">
/sdk-for-flutter-navigate-mapview-mapmarkercluster-addmapmarkers(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-mapview-mapmarker-class&gt; markers)
    → void

</dt>
<dd>
  Adds a list of map markers to this cluster.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapview-mapmarkercluster-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="removeAllMapMarkers">
/sdk-for-flutter-navigate-mapview-mapmarkercluster-removeallmapmarkers(<wbr/>)
    → void

</dt>
<dd>
  Removes all map markers from this cluster.
  

</dd>
<dt class="callable" id="removeMapMarker">
/sdk-for-flutter-navigate-mapview-mapmarkercluster-removemapmarker(<wbr/>/sdk-for-flutter-navigate-mapview-mapmarker-class marker)
    → void

</dt>
<dd>
  Removes a map marker from this cluster.
  

</dd>
<dt class="callable" id="removeMapMarkers">
/sdk-for-flutter-navigate-mapview-mapmarkercluster-removemapmarkers(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-mapview-mapmarker-class&gt; markers)
    → void

</dt>
<dd>
  Removes a list of map markers from this cluster.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapview-mapmarkercluster-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-mapview-mapmarkercluster-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
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



</div>
`
}</HTMLBlock>
