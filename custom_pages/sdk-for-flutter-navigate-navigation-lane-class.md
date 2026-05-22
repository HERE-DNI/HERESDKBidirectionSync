---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-lane-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Lane-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">Lane class</li>
</ol>
<div class="self-name">Lane</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/Lane-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>Lane class</h1></div>
<section class="desc markdown">
<p>A class that provides information for a lane.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Lane.withAll">
/sdk-for-flutter-navigate-navigation-lane-lane-withall(/sdk-for-flutter-navigate-navigation-lanetype-class type, /sdk-for-flutter-navigate-navigation-lanerecommendationstate recommendationState, /sdk-for-flutter-navigate-navigation-laneaccess-class access, /sdk-for-flutter-navigate-navigation-lanemarkings-class laneMarkings, List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-lanedirection&gt; directions, List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-lanedirection&gt; directionsOnRoute)
</dt>
<dd>
          Creates a new instance.
        </dd>
<dt class="callable" id="Lane.withDirections">
/sdk-for-flutter-navigate-navigation-lane-lane-withdirections(/sdk-for-flutter-navigate-navigation-lanetype-class type, /sdk-for-flutter-navigate-navigation-laneaccess-class access, /sdk-for-flutter-navigate-navigation-lanemarkings-class laneMarkings, List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-lanedirection&gt; directions, List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-lanedirection&gt; directionsOnRoute)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="access">
/sdk-for-flutter-navigate-navigation-lane-access
↔ /sdk-for-flutter-navigate-navigation-laneaccess-class
</dt>
<dd>
  Indicates which vehicle types can access this lane.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="directions">
/sdk-for-flutter-navigate-navigation-lane-directions
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-lanedirection&gt;
</dt>
<dd>
  Indicates all the lane directions that are available for this lane.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="directionsOnRoute">
/sdk-for-flutter-navigate-navigation-lane-directionsonroute
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-lanedirection&gt;
</dt>
<dd>
  Indicates the lane directions that are on the route.
Following these directions keeps the driver on the route.
This is a subset of /sdk-for-flutter-navigate-navigation-lane-directions.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-lane-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="laneMarkings">
/sdk-for-flutter-navigate-navigation-lane-lanemarkings
↔ /sdk-for-flutter-navigate-navigation-lanemarkings-class
</dt>
<dd>
  Indicates the lane markings between the lanes.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="recommendationState">
/sdk-for-flutter-navigate-navigation-lane-recommendationstate
↔ /sdk-for-flutter-navigate-navigation-lanerecommendationstate
</dt>
<dd>
  Indicates if this lane leads to the upcoming maneuvers.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-lane-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="type">
/sdk-for-flutter-navigate-navigation-lane-type
↔ /sdk-for-flutter-navigate-navigation-lanetype-class
</dt>
<dd>
  Indicates the properties of this lane.
For example, it indicates whether parking is allowed, if it is an acceleration lane,
an express lane, or other attributes.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-lane-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-lane-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-lane-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">Lane class</li>
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



</div>
`
}</HTMLBlock>
