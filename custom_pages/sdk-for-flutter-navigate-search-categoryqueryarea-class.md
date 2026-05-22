---
title: "Untitled"
slug: "sdk-for-flutter-navigate-search-categoryqueryarea-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CategoryQueryArea-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li class="self-crumb">CategoryQueryArea class</li>
</ol>
<div class="self-name">CategoryQueryArea</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/CategoryQueryArea-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>CategoryQueryArea class</h1></div>
<section class="desc markdown">
<p>Area to perform search on.</p>
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
<dt class="callable" id="CategoryQueryArea.withBox">
/sdk-for-flutter-navigate-search-categoryqueryarea-categoryqueryarea-withbox(/sdk-for-flutter-navigate-core-geocoordinates-class areaCenter, /sdk-for-flutter-navigate-core-geobox-class boxArea)
</dt>
<dd>
          Constructs a new instance of this class from provided parameters.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="CategoryQueryArea.withCenter">
/sdk-for-flutter-navigate-search-categoryqueryarea-categoryqueryarea-withcenter(/sdk-for-flutter-navigate-core-geocoordinates-class areaCenter)
</dt>
<dd>
          Constructs a new instance of this class from provided parameters.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="CategoryQueryArea.withCircle">
/sdk-for-flutter-navigate-search-categoryqueryarea-categoryqueryarea-withcircle(/sdk-for-flutter-navigate-core-geocoordinates-class areaCenter, /sdk-for-flutter-navigate-core-geocircle-class circleArea)
</dt>
<dd>
          Constructs a new instance of this class from provided parameters.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="CategoryQueryArea.withCorridorAndCenter">
/sdk-for-flutter-navigate-search-categoryqueryarea-categoryqueryarea-withcorridorandcenter(/sdk-for-flutter-navigate-core-geocorridor-class corridorArea, /sdk-for-flutter-navigate-core-geocoordinates-class areaCenter)
</dt>
<dd>
          Constructs a new instance of this class from provided parameters.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="areaCenter">
/sdk-for-flutter-navigate-search-categoryqueryarea-areacenter
→ /sdk-for-flutter-navigate-core-geocoordinates-class
</dt>
<dd>
  Geographic coordinates of the center around which to provide the most relevant places.
  <div class="features">final</div>
</dd>
<dt class="property" id="boxArea">
/sdk-for-flutter-navigate-search-categoryqueryarea-boxarea
→ /sdk-for-flutter-navigate-core-geobox-class?
</dt>
<dd>
  Geographic rectangle area in which to provide the most relevant places.
  <div class="features">final</div>
</dd>
<dt class="property" id="circleArea">
/sdk-for-flutter-navigate-search-categoryqueryarea-circlearea
→ /sdk-for-flutter-navigate-core-geocircle-class?
</dt>
<dd>
  Geographic circle area in which to provide the most relevant places.
  <div class="features">final</div>
</dd>
<dt class="property" id="corridorArea">
/sdk-for-flutter-navigate-search-categoryqueryarea-corridorarea
→ /sdk-for-flutter-navigate-core-geocorridor-class?
</dt>
<dd>
  Geographic corridor area in which to provide the most relevant places.
The contained polyline and half-width define the area that will be used in a search query.
  <div class="features">final</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-search-categoryqueryarea-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-search-categoryqueryarea-runtimetype
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
/sdk-for-flutter-navigate-search-categoryqueryarea-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-search-categoryqueryarea-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-search-categoryqueryarea-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li class="self-crumb">CategoryQueryArea class</li>
</ol>
<h5>search library</h5>
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
