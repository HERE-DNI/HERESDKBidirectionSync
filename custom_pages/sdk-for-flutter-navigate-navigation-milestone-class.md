---
title: "Milestone class"
slug: "sdk-for-flutter-navigate-navigation-milestone-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Milestone-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/Milestone-class.html#constructors">Constructors</a></li>
<li><a href="navigation/Milestone/Milestone.withType.html">withType</a></li>
<li class="section-title">
<a href="navigation/Milestone-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/Milestone/hashCode.html">hashCode</a></li>
<li><a href="navigation/Milestone/mapMatchedCoordinates.html">mapMatchedCoordinates</a></li>
<li><a href="navigation/Milestone/originalCoordinates.html">originalCoordinates</a></li>
<li class="inherited"><a href="navigation/Milestone/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/Milestone/sectionIndex.html">sectionIndex</a></li>
<li><a href="navigation/Milestone/type.html">type</a></li>
<li><a href="navigation/Milestone/waypointIndex.html">waypointIndex</a></li>
<li class="section-title inherited"><a href="navigation/Milestone-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/Milestone/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/Milestone/toString.html">toString</a></li>
<li class="section-title"><a href="navigation/Milestone-class.html#operators">Operators</a></li>
<li><a href="navigation/Milestone/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">Milestone class</li>
</ol>
<div class="self-name">Milestone</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/Milestone-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>Milestone class</h1></div>
<section class="desc markdown">
<p>Represents information about the waypoints along the route.</p>
<p>Note that this can include additional waypoints added during route
calculation that may not have been part of the original user-defined
waypoint list. For example, additional waypoints are added automatically
between sections that require a different transport mode like when taking a
ferry.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Milestone.withType">
/sdk-for-flutter-navigate-navigation-milestone-milestone-withtype(int sectionIndex, int? waypointIndex, /sdk-for-flutter-navigate-core-geocoordinates-class? originalCoordinates, /sdk-for-flutter-navigate-core-geocoordinates-class mapMatchedCoordinates, /sdk-for-flutter-navigate-navigation-milestonetype type)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-milestone-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="mapMatchedCoordinates">
/sdk-for-flutter-navigate-navigation-milestone-mapmatchedcoordinates
↔ /sdk-for-flutter-navigate-core-geocoordinates-class
</dt>
<dd>
  Map-matched geographic coordinates.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="originalCoordinates">
/sdk-for-flutter-navigate-navigation-milestone-originalcoordinates
↔ /sdk-for-flutter-navigate-core-geocoordinates-class?
</dt>
<dd>
  User-defined geographic coordinates. If not available, this waypoint was
added during route calculation.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-milestone-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="sectionIndex">
/sdk-for-flutter-navigate-navigation-milestone-sectionindex
↔ int
</dt>
<dd>
  Index of the section on the route.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="type">
/sdk-for-flutter-navigate-navigation-milestone-type
↔ /sdk-for-flutter-navigate-navigation-milestonetype
</dt>
<dd>
  Type of this Milestone
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="waypointIndex">
/sdk-for-flutter-navigate-navigation-milestone-waypointindex
↔ int?
</dt>
<dd>
  If present, this index corresponds to the waypoint in the original
user-defined waypoint list. Otherwise this waypoint was added during
route calculation by the system.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-milestone-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-milestone-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-milestone-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">Milestone class</li>
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
