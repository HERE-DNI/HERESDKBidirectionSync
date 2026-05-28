---
title: "GeoOrientationUpdate class"
slug: "sdk-for-flutter-explore-core-geoorientationupdate-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- GeoOrientationUpdate-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core/GeoOrientationUpdate-class.html#constructors">Constructors</a></li>
<li><a href="core/GeoOrientationUpdate/GeoOrientationUpdate.html">GeoOrientationUpdate</a></li>
<li><a href="core/GeoOrientationUpdate/GeoOrientationUpdate.withGeoOrientation.html">withGeoOrientation</a></li>
<li class="section-title">
<a href="core/GeoOrientationUpdate-class.html#instance-properties">Properties</a>
</li>
<li><a href="core/GeoOrientationUpdate/bearing.html">bearing</a></li>
<li><a href="core/GeoOrientationUpdate/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="core/GeoOrientationUpdate/runtimeType.html">runtimeType</a></li>
<li><a href="core/GeoOrientationUpdate/tilt.html">tilt</a></li>
<li class="section-title inherited"><a href="core/GeoOrientationUpdate-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="core/GeoOrientationUpdate/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core/GeoOrientationUpdate/toString.html">toString</a></li>
<li class="section-title"><a href="core/GeoOrientationUpdate-class.html#operators">Operators</a></li>
<li><a href="core/GeoOrientationUpdate/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-core-library</li>
<li class="self-crumb">GeoOrientationUpdate class</li>
</ol>
<div class="self-name">GeoOrientationUpdate</div>
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
<div class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/GeoOrientationUpdate-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>GeoOrientationUpdate class</h1></div>
<section class="desc markdown">
<p>Describes geodetic orientation update with bearing and tilt.</p>
<p>Updating an orientation value can be skipped by setting <code>null</code> in an appriopriate field.
For example, if one wants bearing not to be updated set it to <code>null</code>.</p>
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
<dt class="callable" id="GeoOrientationUpdate">
/sdk-for-flutter-explore-core-geoorientationupdate-geoorientationupdate(double? bearing, double? tilt)
</dt>
<dd>
<li>
<p><code>bearing</code> Bearing in degrees. When the passed value is <code>null</code> bearing is not updated and the current value is kept.
NaN value is converted to <code>null</code>.</p>
</li>
<li>
<p><code>tilt</code> Tilt in degrees. When the passed value is <code>null</code> tilt is not updated and the current value is kept.
NaN value is converted to <code>null</code>.</p>
</li>
<div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="GeoOrientationUpdate.withGeoOrientation">
/sdk-for-flutter-explore-core-geoorientationupdate-geoorientationupdate-withgeoorientation(/sdk-for-flutter-explore-core-geoorientation-class orientation)
</dt>
<dd>
          Constructs a new GeoOrientationUpdate instance from a GeoOrientation instance.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="bearing">
/sdk-for-flutter-explore-core-geoorientationupdate-bearing
→ double?
</dt>
<dd>
  Bearing in degrees. 0 is north up, positive is clockwise.
A <code>null</code> value means that bearing is not updated and the current value is kept.
  <div class="features">final</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-core-geoorientationupdate-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-core-geoorientationupdate-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="tilt">
/sdk-for-flutter-explore-core-geoorientationupdate-tilt
→ double?
</dt>
<dd>
  Tilt in degrees. 0 is perpendicular to earth surface, a positive value turns the camera's nose up
and changes the camera's location to ensure that the camera target is not changed.
A <code>null</code> value means that tilt is not updated and the current value is kept.
  <div class="features">final</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-core-geoorientationupdate-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-core-geoorientationupdate-tostring(<wbr/>)
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
/sdk-for-flutter-explore-core-geoorientationupdate-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-core-library</li>
<li class="self-crumb">GeoOrientationUpdate class</li>
</ol>
<h5>core library</h5>
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
