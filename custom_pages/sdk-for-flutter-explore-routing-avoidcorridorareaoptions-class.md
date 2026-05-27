---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-avoidcorridorareaoptions-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- AvoidCorridorAreaOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/AvoidCorridorAreaOptions-class.html#constructors">Constructors</a></li>
<li><a href="routing/AvoidCorridorAreaOptions/AvoidCorridorAreaOptions.html">AvoidCorridorAreaOptions</a></li>
<li class="section-title">
<a href="routing/AvoidCorridorAreaOptions-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/AvoidCorridorAreaOptions/avoidCorridorArea.html">avoidCorridorArea</a></li>
<li><a href="routing/AvoidCorridorAreaOptions/boundingBoxExceptionAreas.html">boundingBoxExceptionAreas</a></li>
<li><a href="routing/AvoidCorridorAreaOptions/corridorExceptionAreas.html">corridorExceptionAreas</a></li>
<li><a href="routing/AvoidCorridorAreaOptions/hashCode.html">hashCode</a></li>
<li><a href="routing/AvoidCorridorAreaOptions/polygonExceptionAreas.html">polygonExceptionAreas</a></li>
<li class="inherited"><a href="routing/AvoidCorridorAreaOptions/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="routing/AvoidCorridorAreaOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/AvoidCorridorAreaOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/AvoidCorridorAreaOptions/toString.html">toString</a></li>
<li class="section-title"><a href="routing/AvoidCorridorAreaOptions-class.html#operators">Operators</a></li>
<li><a href="routing/AvoidCorridorAreaOptions/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">AvoidCorridorAreaOptions class</li>
</ol>
<div class="self-name">AvoidCorridorAreaOptions</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/AvoidCorridorAreaOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>AvoidCorridorAreaOptions class</h1></div>
<section class="desc markdown">
<p>Area of corridor shape which routes must not cross and exceptions for this area.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="AvoidCorridorAreaOptions">
<a href="../routing/AvoidCorridorAreaOptions/AvoidCorridorAreaOptions.html">/sdk-for-flutter-explore-routing-avoidcorridorareaoptions-avoidcorridorareaoptions</a>(<a href="../core/GeoCorridor-class.html">/sdk-for-flutter-explore-core-geocorridor-class</a> avoidCorridorArea)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="avoidCorridorArea">
<a href="../routing/AvoidCorridorAreaOptions/avoidCorridorArea.html">/sdk-for-flutter-explore-routing-avoidcorridorareaoptions-avoidcorridorarea</a>
↔ <a href="../core/GeoCorridor-class.html">/sdk-for-flutter-explore-core-geocorridor-class</a>
</dt>
<dd>
  Area of corridor shape which routes must not cross. Strictly enforced.
Violations are reported as <a href="../routing/SectionNoticeCode.html">/sdk-for-flutter-explore-routing-sectionnoticecode</a>.
<strong>Note:</strong>
This avoidance option is not supported for <code>IsolineOptions</code>. If it is defined for isoline calculation then an <code>sdk.routing.RoutingError.INVALID_PARAMETER</code> error is generated.
Even though <code>GeoCorridor.half_width_in_meters</code> is an optional property in case of exception areas it is mandatory.
Otherwise route calculation will fail with an <code>sdk.routing.RoutingError.INVALID_PARAMETER</code> error.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="boundingBoxExceptionAreas">
<a href="../routing/AvoidCorridorAreaOptions/boundingBoxExceptionAreas.html">/sdk-for-flutter-explore-routing-avoidcorridorareaoptions-boundingboxexceptionareas</a>
↔ List&lt;<wbr/><a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>&gt;
</dt>
<dd>
  Areas of rectangular shape to exclude from avoidance.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="corridorExceptionAreas">
<a href="../routing/AvoidCorridorAreaOptions/corridorExceptionAreas.html">/sdk-for-flutter-explore-routing-avoidcorridorareaoptions-corridorexceptionareas</a>
↔ List&lt;<wbr/><a href="../core/GeoCorridor-class.html">/sdk-for-flutter-explore-core-geocorridor-class</a>&gt;
</dt>
<dd>
  Areas of corridor shape to exclude from avoidance.
<strong>Note:</strong>
Even though <code>GeoCorridor.half_width_in_meters</code> is an optional property in case of exception areas it is mandatory.
Otherwise route calculation will fail with an <code>sdk.routing.RoutingError.INVALID_PARAMETER</code> error.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../routing/AvoidCorridorAreaOptions/hashCode.html">/sdk-for-flutter-explore-routing-avoidcorridorareaoptions-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="polygonExceptionAreas">
<a href="../routing/AvoidCorridorAreaOptions/polygonExceptionAreas.html">/sdk-for-flutter-explore-routing-avoidcorridorareaoptions-polygonexceptionareas</a>
↔ List&lt;<wbr/><a href="../core/GeoPolygon-class.html">/sdk-for-flutter-explore-core-geopolygon-class</a>&gt;
</dt>
<dd>
  Areas of polygon shape to exclude from avoidance.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/AvoidCorridorAreaOptions/runtimeType.html">/sdk-for-flutter-explore-routing-avoidcorridorareaoptions-runtimetype</a>
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
<a href="../routing/AvoidCorridorAreaOptions/noSuchMethod.html">/sdk-for-flutter-explore-routing-avoidcorridorareaoptions-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/AvoidCorridorAreaOptions/toString.html">/sdk-for-flutter-explore-routing-avoidcorridorareaoptions-tostring</a>(<wbr/>)
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
<a href="../routing/AvoidCorridorAreaOptions/operator_equals.html">/sdk-for-flutter-explore-routing-avoidcorridorareaoptions-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">AvoidCorridorAreaOptions class</li>
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
</div></div>
</div>
</HTMLBlock>
