---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-trafficonroute-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- TrafficOnRoute-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/TrafficOnRoute-class.html#constructors">Constructors</a></li>
<li><a href="routing/TrafficOnRoute/TrafficOnRoute.html">TrafficOnRoute</a></li>
<li class="section-title">
<a href="routing/TrafficOnRoute-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/TrafficOnRoute/hashCode.html">hashCode</a></li>
<li><a href="routing/TrafficOnRoute/lastTraveledSectionIndex.html">lastTraveledSectionIndex</a></li>
<li class="inherited"><a href="routing/TrafficOnRoute/runtimeType.html">runtimeType</a></li>
<li><a href="routing/TrafficOnRoute/trafficSections.html">trafficSections</a></li>
<li><a href="routing/TrafficOnRoute/traveledDistanceOnLastSectionInMeters.html">traveledDistanceOnLastSectionInMeters</a></li>
<li class="section-title inherited"><a href="routing/TrafficOnRoute-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/TrafficOnRoute/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/TrafficOnRoute/toString.html">toString</a></li>
<li class="section-title"><a href="routing/TrafficOnRoute-class.html#operators">Operators</a></li>
<li><a href="routing/TrafficOnRoute/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">TrafficOnRoute class</li>
</ol>
<div class="self-name">TrafficOnRoute</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/TrafficOnRoute-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TrafficOnRoute class</h1></div>
<section class="desc markdown">
<p>Traffic information on a route.</p>
<p>Information for the already traveled portion of the route is
omitted.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TrafficOnRoute">
<a href="../routing/TrafficOnRoute/TrafficOnRoute.html">/sdk-for-flutter-explore-routing-trafficonroute-trafficonroute</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
<a href="../routing/TrafficOnRoute/hashCode.html">/sdk-for-flutter-explore-routing-trafficonroute-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="lastTraveledSectionIndex">
<a href="../routing/TrafficOnRoute/lastTraveledSectionIndex.html">/sdk-for-flutter-explore-routing-trafficonroute-lasttraveledsectionindex</a>
↔ int
</dt>
<dd>
  Indicates the index of the last traveled route section. Traveled part of the route won't
be reused.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/TrafficOnRoute/runtimeType.html">/sdk-for-flutter-explore-routing-trafficonroute-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="trafficSections">
<a href="../routing/TrafficOnRoute/trafficSections.html">/sdk-for-flutter-explore-routing-trafficonroute-trafficsections</a>
↔ List&lt;<wbr/><a href="../routing/TrafficOnSection-class.html">/sdk-for-flutter-explore-routing-trafficonsection-class</a>&gt;
</dt>
<dd>
  List of traffic sections.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="traveledDistanceOnLastSectionInMeters">
<a href="../routing/TrafficOnRoute/traveledDistanceOnLastSectionInMeters.html">/sdk-for-flutter-explore-routing-trafficonroute-traveleddistanceonlastsectioninmeters</a>
↔ int
</dt>
<dd>
  Offset, in meter, to the last visited position on the route section defined by the last
traveled section index.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../routing/TrafficOnRoute/noSuchMethod.html">/sdk-for-flutter-explore-routing-trafficonroute-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/TrafficOnRoute/toString.html">/sdk-for-flutter-explore-routing-trafficonroute-tostring</a>(<wbr/>)
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
<a href="../routing/TrafficOnRoute/operator_equals.html">/sdk-for-flutter-explore-routing-trafficonroute-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">TrafficOnRoute class</li>
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
