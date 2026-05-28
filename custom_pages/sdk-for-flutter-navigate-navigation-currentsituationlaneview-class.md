---
title: "CurrentSituationLaneView class"
slug: "sdk-for-flutter-navigate-navigation-currentsituationlaneview-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CurrentSituationLaneView-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/CurrentSituationLaneView-class.html#constructors">Constructors</a></li>
<li><a href="navigation/CurrentSituationLaneView/CurrentSituationLaneView.html">CurrentSituationLaneView</a></li>
<li class="section-title">
<a href="navigation/CurrentSituationLaneView-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/CurrentSituationLaneView/access.html">access</a></li>
<li><a href="navigation/CurrentSituationLaneView/directionCategory.html">directionCategory</a></li>
<li><a href="navigation/CurrentSituationLaneView/directions.html">directions</a></li>
<li><a href="navigation/CurrentSituationLaneView/directionsOnRoute.html">directionsOnRoute</a></li>
<li><a href="navigation/CurrentSituationLaneView/hashCode.html">hashCode</a></li>
<li><a href="navigation/CurrentSituationLaneView/laneMarkings.html">laneMarkings</a></li>
<li class="inherited"><a href="navigation/CurrentSituationLaneView/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/CurrentSituationLaneView/type.html">type</a></li>
<li class="section-title inherited"><a href="navigation/CurrentSituationLaneView-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/CurrentSituationLaneView/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/CurrentSituationLaneView/toString.html">toString</a></li>
<li class="section-title"><a href="navigation/CurrentSituationLaneView-class.html#operators">Operators</a></li>
<li><a href="navigation/CurrentSituationLaneView/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">CurrentSituationLaneView class</li>
</ol>
<div class="self-name">CurrentSituationLaneView</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/CurrentSituationLaneView-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>CurrentSituationLaneView class</h1></div>
<section class="desc markdown">
<p>A class that provides current situation lane assistance view
information for the street at the current position of a single lane.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="CurrentSituationLaneView">
/sdk-for-flutter-navigate-navigation-currentsituationlaneview-currentsituationlaneview(/sdk-for-flutter-navigate-navigation-laneaccess-class access, /sdk-for-flutter-navigate-navigation-lanedirectioncategory-class directionCategory, /sdk-for-flutter-navigate-navigation-lanetype-class type)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="access">
/sdk-for-flutter-navigate-navigation-currentsituationlaneview-access
↔ /sdk-for-flutter-navigate-navigation-laneaccess-class
</dt>
<dd>
  Indicates which vehicle types can access this lane.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="directionCategory">
/sdk-for-flutter-navigate-navigation-currentsituationlaneview-directioncategory
↔ /sdk-for-flutter-navigate-navigation-lanedirectioncategory-class
</dt>
<dd>
  Indicates towards which directions this lane leads.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="directions">
/sdk-for-flutter-navigate-navigation-currentsituationlaneview-directions
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-lanedirection&gt;
</dt>
<dd>
  Indicates which lane directions are available for this lane.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="directionsOnRoute">
/sdk-for-flutter-navigate-navigation-currentsituationlaneview-directionsonroute
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-lanedirection&gt;
</dt>
<dd>
  Indicates which lane directions are on the route. Following those directions keeps the driver on the route.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-currentsituationlaneview-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="laneMarkings">
/sdk-for-flutter-navigate-navigation-currentsituationlaneview-lanemarkings
↔ /sdk-for-flutter-navigate-navigation-lanemarkings-class
</dt>
<dd>
  Indicates the lane markings between the lanes.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-currentsituationlaneview-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="type">
/sdk-for-flutter-navigate-navigation-currentsituationlaneview-type
↔ /sdk-for-flutter-navigate-navigation-lanetype-class
</dt>
<dd>
  Indicates this lane's properties.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-currentsituationlaneview-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-currentsituationlaneview-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-currentsituationlaneview-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">CurrentSituationLaneView class</li>
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
