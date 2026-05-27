---
title: "Constructors"
slug: "sdk-for-flutter-explore-core-pickedplace-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- PickedPlace-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core/PickedPlace-class.html#constructors">Constructors</a></li>
<li><a href="core/PickedPlace/PickedPlace.html">PickedPlace</a></li>
<li class="section-title">
<a href="core/PickedPlace-class.html#instance-properties">Properties</a>
</li>
<li><a href="core/PickedPlace/coordinates.html">coordinates</a></li>
<li><a href="core/PickedPlace/hashCode.html">hashCode</a></li>
<li><a href="core/PickedPlace/name.html">name</a></li>
<li><a href="core/PickedPlace/placeCategoryId.html">placeCategoryId</a></li>
<li class="inherited"><a href="core/PickedPlace/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="core/PickedPlace-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="core/PickedPlace/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core/PickedPlace/toString.html">toString</a></li>
<li class="section-title"><a href="core/PickedPlace-class.html#operators">Operators</a></li>
<li><a href="core/PickedPlace/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
<li class="self-crumb">PickedPlace class</li>
</ol>
<div class="self-name">PickedPlace</div>
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
<div class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/PickedPlace-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>PickedPlace class</h1></div>
<section class="desc markdown">
<p>Carries the result of picking a Carto POI (point of interest) object.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="PickedPlace">
<a href="../core/PickedPlace/PickedPlace.html">/sdk-for-flutter-explore-core-pickedplace-pickedplace</a>(String name, <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> coordinates, String placeCategoryId)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="coordinates">
<a href="../core/PickedPlace/coordinates.html">/sdk-for-flutter-explore-core-pickedplace-coordinates</a>
↔ <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>
</dt>
<dd>
  The geographic coordinates of the POI.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../core/PickedPlace/hashCode.html">/sdk-for-flutter-explore-core-pickedplace-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="name">
<a href="../core/PickedPlace/name.html">/sdk-for-flutter-explore-core-pickedplace-name</a>
↔ String
</dt>
<dd>
  The name of the POI localized in the currently selected map language.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="placeCategoryId">
<a href="../core/PickedPlace/placeCategoryId.html">/sdk-for-flutter-explore-core-pickedplace-placecategoryid</a>
↔ String
</dt>
<dd>
  The place category ID of the POI.
This is the same String value as <code>PlaceCategory.id</code> that can be obtained from the
<code>SearchEngine</code> and the <code>OfflineSearchEngine</code>. Note that not all editions include the
<code>OfflineSearchEngine</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../core/PickedPlace/runtimeType.html">/sdk-for-flutter-explore-core-pickedplace-runtimetype</a>
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
<a href="../core/PickedPlace/noSuchMethod.html">/sdk-for-flutter-explore-core-pickedplace-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../core/PickedPlace/toString.html">/sdk-for-flutter-explore-core-pickedplace-tostring</a>(<wbr/>)
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
<a href="../core/PickedPlace/operator_equals.html">/sdk-for-flutter-explore-core-pickedplace-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
<li class="self-crumb">PickedPlace class</li>
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
</HTMLBlock>
