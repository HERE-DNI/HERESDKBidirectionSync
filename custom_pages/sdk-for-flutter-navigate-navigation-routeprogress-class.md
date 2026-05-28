---
title: "RouteProgress class"
slug: "sdk-for-flutter-navigate-navigation-routeprogress-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RouteProgress-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/RouteProgress-class.html#constructors">Constructors</a></li>
<li><a href="navigation/RouteProgress/RouteProgress.html">RouteProgress</a></li>
<li class="section-title">
<a href="navigation/RouteProgress-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/RouteProgress/hashCode.html">hashCode</a></li>
<li><a href="navigation/RouteProgress/maneuverProgress.html">maneuverProgress</a></li>
<li><a href="navigation/RouteProgress/routeMatchedLocation.html">routeMatchedLocation</a></li>
<li class="inherited"><a href="navigation/RouteProgress/runtimeType.html">runtimeType</a></li>
<li><a class="deprecated" href="navigation/RouteProgress/sectionIndex.html">sectionIndex</a></li>
<li><a href="navigation/RouteProgress/sectionProgress.html">sectionProgress</a></li>
<li><a class="deprecated" href="navigation/RouteProgress/spanIndex.html">spanIndex</a></li>
<li class="section-title inherited"><a href="navigation/RouteProgress-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/RouteProgress/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/RouteProgress/toString.html">toString</a></li>
<li class="section-title"><a href="navigation/RouteProgress-class.html#operators">Operators</a></li>
<li><a href="navigation/RouteProgress/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">RouteProgress class</li>
</ol>
<div class="self-name">RouteProgress</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/RouteProgress-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RouteProgress class</h1></div>
<section class="desc markdown">
<p>Contains all the relevant information on the user's progress along a route.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RouteProgress">
/sdk-for-flutter-navigate-navigation-routeprogress-routeprogress(List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-sectionprogress-class&gt; sectionProgress, List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-maneuverprogress-class&gt; maneuverProgress)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-routeprogress-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="maneuverProgress">
/sdk-for-flutter-navigate-navigation-routeprogress-maneuverprogress
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-maneuverprogress-class&gt;
</dt>
<dd>
  The progress for next and next-next maneuvers (see /sdk-for-flutter-navigate-routing-maneuver-class). Note that the list
can contain at maximum two items (for next and next-next maneuvers) and one or zero when approaching the
destination.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="routeMatchedLocation">
/sdk-for-flutter-navigate-navigation-routeprogress-routematchedlocation
↔ /sdk-for-flutter-navigate-navigation-routematchedlocation-class
</dt>
<dd>
  Route matched location.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-routeprogress-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="sectionIndex">
/sdk-for-flutter-navigate-navigation-routeprogress-sectionindex
↔ int
</dt>
<dd>
  Index of the /sdk-for-flutter-navigate-routing-section-class in the route.
Note that this section index does not point to the current /sdk-for-flutter-navigate-navigation-sectionprogress-class
but to the route /sdk-for-flutter-navigate-routing-section-class that you can access via /sdk-for-flutter-navigate-navigation-navigatorinterface-route
and /sdk-for-flutter-navigate-routing-route-sections.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="sectionProgress">
/sdk-for-flutter-navigate-navigation-routeprogress-sectionprogress
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-sectionprogress-class&gt;
</dt>
<dd>
  The progress for each /sdk-for-flutter-navigate-routing-section-class from the current one to the last one.
Note that the progress information is accumulated successively, therefore information relative
to the final destination is in the last item of the list. The list is guaranteed to be non-empty.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="spanIndex">
/sdk-for-flutter-navigate-navigation-routeprogress-spanindex
↔ int
</dt>
<dd>
  Index of the /sdk-for-flutter-navigate-routing-span-class in the route section.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-routeprogress-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-routeprogress-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-routeprogress-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">RouteProgress class</li>
</ol>
<h5>navigation library</h5>
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
