---
title: "Untitled"
slug: "sdk-for-flutter-navigate-routing-isoline-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Isoline-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li class="self-crumb">Isoline class</li>
</ol>
<div class="self-name">Isoline</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/Isoline-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>Isoline class abstract</h1></div>
<section class="desc markdown">
<p>Represents an isoline polygon around a center point.</p>
<p>Any possible route between
the center and any point on the edges of the polygon can be travelled within the
given range restriction. The edges of the polygon are not guaranteed to be on the road as
all reachable road endpoints are smoothened to fit into one polygon shape. This
process can be influenced by setting /sdk-for-flutter-navigate-routing-isolineoptionscalculation-maxpoints.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Isoline">
/sdk-for-flutter-navigate-routing-isoline-isoline(/sdk-for-flutter-navigate-routing-isolinerangetype rangeType, double rangeValue, /sdk-for-flutter-navigate-routing-mapmatchedcoordinates-class center, List&lt;<wbr/>/sdk-for-flutter-navigate-core-geopolygon-class&gt; polygons)
</dt>
<dd>
          Constructs an isoline instance.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="center">
/sdk-for-flutter-navigate-routing-isoline-center
→ /sdk-for-flutter-navigate-routing-mapmatchedcoordinates-class
</dt>
<dd>
  The center point that was used to calculate this isoline.
Specifies the center point that was used to calculate this isoline.
This includes the original center that was passed to the RoutingEngine.
Gets the center point that was used to calculate this isoline.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-routing-isoline-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="polygons">
/sdk-for-flutter-navigate-routing-isoline-polygons
→ List&lt;<wbr/>/sdk-for-flutter-navigate-core-geopolygon-class&gt;
</dt>
<dd>
  A list of polygons that belong to this isoline. An isoline can consist of multiple
polygons. For example, islands that can be reached by a ferry are included.
Each island is then represented as a separate polygon. However, in most cases
only a single polygon is included.
Gets a list of polygons that belong to this isoline. An isoline can consist of multiple
polygons. For example, islands that can be reached by a ferry are included.
Each island is then represented as a separate polygon. However, in most cases
only a single polygon is included.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="rangeType">
/sdk-for-flutter-navigate-routing-isoline-rangetype
→ /sdk-for-flutter-navigate-routing-isolinerangetype
</dt>
<dd>
  Specifies the type of the restriction that was used to calculate this isoline.
Gets the type of the restriction that was used to calculate this isoline.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="rangeValue">
/sdk-for-flutter-navigate-routing-isoline-rangevalue
→ double
</dt>
<dd>
  Specifies the numerical value of the restriction that was used to calculate this isoline.
Gets the numerical value of the restriction that was used to calculate this isoline.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-routing-isoline-runtimetype
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
/sdk-for-flutter-navigate-routing-isoline-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-routing-isoline-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-routing-isoline-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li class="self-crumb">Isoline class</li>
</ol>
<h5>routing library</h5>
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
