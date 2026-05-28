---
title: "AvoidBoundingBoxAreaOptions class"
slug: "sdk-for-flutter-navigate-routing-avoidboundingboxareaoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- AvoidBoundingBoxAreaOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/AvoidBoundingBoxAreaOptions-class.html#constructors">Constructors</a></li>
<li><a href="routing/AvoidBoundingBoxAreaOptions/AvoidBoundingBoxAreaOptions.html">AvoidBoundingBoxAreaOptions</a></li>
<li class="section-title">
<a href="routing/AvoidBoundingBoxAreaOptions-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/AvoidBoundingBoxAreaOptions/avoidBoundingBoxArea.html">avoidBoundingBoxArea</a></li>
<li><a href="routing/AvoidBoundingBoxAreaOptions/boundingBoxExceptionAreas.html">boundingBoxExceptionAreas</a></li>
<li><a href="routing/AvoidBoundingBoxAreaOptions/corridorExceptionAreas.html">corridorExceptionAreas</a></li>
<li><a href="routing/AvoidBoundingBoxAreaOptions/hashCode.html">hashCode</a></li>
<li><a href="routing/AvoidBoundingBoxAreaOptions/polygonExceptionAreas.html">polygonExceptionAreas</a></li>
<li class="inherited"><a href="routing/AvoidBoundingBoxAreaOptions/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="routing/AvoidBoundingBoxAreaOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/AvoidBoundingBoxAreaOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/AvoidBoundingBoxAreaOptions/toString.html">toString</a></li>
<li class="section-title"><a href="routing/AvoidBoundingBoxAreaOptions-class.html#operators">Operators</a></li>
<li><a href="routing/AvoidBoundingBoxAreaOptions/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li class="self-crumb">AvoidBoundingBoxAreaOptions class</li>
</ol>
<div class="self-name">AvoidBoundingBoxAreaOptions</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/AvoidBoundingBoxAreaOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>AvoidBoundingBoxAreaOptions class</h1></div>
<section class="desc markdown">
<p>The options to specify rectangular shape which routes must not cross.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="AvoidBoundingBoxAreaOptions">
/sdk-for-flutter-navigate-routing-avoidboundingboxareaoptions-avoidboundingboxareaoptions(/sdk-for-flutter-navigate-core-geobox-class avoidBoundingBoxArea)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="avoidBoundingBoxArea">
/sdk-for-flutter-navigate-routing-avoidboundingboxareaoptions-avoidboundingboxarea
↔ /sdk-for-flutter-navigate-core-geobox-class
</dt>
<dd>
  Area of rectangular shape which routes must not cross. Strictly enforced.
<strong>Note:</strong>
Violations are reported as <code>sdk.routing.SectionNoticeCode.VIOLATED_BLOCKED_ROAD</code>.
This avoidance option is not supported for <code>IsolineOptions</code>. If it is defined for isoline calculation then an <code>sdk.routing.RoutingError.INVALID_PARAMETER</code> error is generated.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="boundingBoxExceptionAreas">
/sdk-for-flutter-navigate-routing-avoidboundingboxareaoptions-boundingboxexceptionareas
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-core-geobox-class&gt;
</dt>
<dd>
  Areas of rectangular shape to exclude from avoidance.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="corridorExceptionAreas">
/sdk-for-flutter-navigate-routing-avoidboundingboxareaoptions-corridorexceptionareas
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-core-geocorridor-class&gt;
</dt>
<dd>
  Areas of corridor shape to exclude from avoidance.
<strong>Note:</strong>
Even though <code>GeoCorridor.half_width_in_meters</code> is an optional property in case of exception areas it is mandatory.
Otherwise route calculation will fail with an <code>sdk.routing.RoutingError.INVALID_PARAMETER</code> error.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-routing-avoidboundingboxareaoptions-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="polygonExceptionAreas">
/sdk-for-flutter-navigate-routing-avoidboundingboxareaoptions-polygonexceptionareas
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-core-geopolygon-class&gt;
</dt>
<dd>
  Areas of polygon shape to exclude from avoidance.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-routing-avoidboundingboxareaoptions-runtimetype
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
/sdk-for-flutter-navigate-routing-avoidboundingboxareaoptions-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-routing-avoidboundingboxareaoptions-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-routing-avoidboundingboxareaoptions-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li class="self-crumb">AvoidBoundingBoxAreaOptions class</li>
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
`
}</HTMLBlock>
