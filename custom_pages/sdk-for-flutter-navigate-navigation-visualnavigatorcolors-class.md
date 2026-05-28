---
title: "VisualNavigatorColors class abstract"
slug: "sdk-for-flutter-navigate-navigation-visualnavigatorcolors-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VisualNavigatorColors-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/VisualNavigatorColors-class.html#constructors">Constructors</a></li>
<li><a href="navigation/VisualNavigatorColors/VisualNavigatorColors.html">VisualNavigatorColors</a></li>
<li class="section-title">
<a href="navigation/VisualNavigatorColors-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="navigation/VisualNavigatorColors/hashCode.html">hashCode</a></li>
<li><a href="navigation/VisualNavigatorColors/maneuverArrowColor.html">maneuverArrowColor</a></li>
<li class="inherited"><a href="navigation/VisualNavigatorColors/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/VisualNavigatorColors/trafficOnRouteColors.html">trafficOnRouteColors</a></li>
<li class="section-title"><a href="navigation/VisualNavigatorColors-class.html#instance-methods">Methods</a></li>
<li><a href="navigation/VisualNavigatorColors/getRouteProgressColors.html">getRouteProgressColors</a></li>
<li class="inherited"><a href="navigation/VisualNavigatorColors/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="navigation/VisualNavigatorColors/setRouteProgressColors.html">setRouteProgressColors</a></li>
<li class="inherited"><a href="navigation/VisualNavigatorColors/toString.html">toString</a></li>
<li class="section-title inherited"><a href="navigation/VisualNavigatorColors-class.html#operators">Operators</a></li>
<li class="inherited"><a href="navigation/VisualNavigatorColors/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="navigation/VisualNavigatorColors-class.html#static-methods">Static methods</a></li>
<li><a href="navigation/VisualNavigatorColors/dayColors.html">dayColors</a></li>
<li><a href="navigation/VisualNavigatorColors/nightColors.html">nightColors</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">VisualNavigatorColors class</li>
</ol>
<div class="self-name">VisualNavigatorColors</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/VisualNavigatorColors-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>VisualNavigatorColors class abstract</h1></div>
<section class="desc markdown">
<p>This class contains colors used by /sdk-for-flutter-navigate-navigation-visualnavigator-class to render
the route and the maneuver arrow visualization.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="VisualNavigatorColors">
/sdk-for-flutter-navigate-navigation-visualnavigatorcolors-visualnavigatorcolors()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-navigation-visualnavigatorcolors-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="maneuverArrowColor">
/sdk-for-flutter-navigate-navigation-visualnavigatorcolors-maneuverarrowcolor
↔ Color
</dt>
<dd>
  Maneuver arrow color.
The object containing color used to draw maneuver arrows on the route to highlight lane directions at the end of a street.
The alpha channel is ignored. The color is interpreted as fully opaque.
Gets the color used to draw maneuver arrows on the route.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-visualnavigatorcolors-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="trafficOnRouteColors">
/sdk-for-flutter-navigate-navigation-visualnavigatorcolors-trafficonroutecolors
↔ /sdk-for-flutter-navigate-navigation-trafficonroutecolors-class
</dt>
<dd>
  Colors used to visualize traffic conditions on the route ahead of the current location, for segments with a jam factor of 4.0 or higher.
For route segments with a jam factor below 4.0 and those behind the current location, /sdk-for-flutter-navigate-navigation-routeprogresscolors-class are used instead.
Gets colors used for visualization of traffic conditions on route.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="getRouteProgressColors">
/sdk-for-flutter-navigate-navigation-visualnavigatorcolors-getrouteprogresscolors(<wbr/>/sdk-for-flutter-navigate-routing-sectiontransportmode sectionTransportMode)
    → /sdk-for-flutter-navigate-navigation-routeprogresscolors-class

</dt>
<dd>
  Gets route color for visualization.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-visualnavigatorcolors-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="setRouteProgressColors">
/sdk-for-flutter-navigate-navigation-visualnavigatorcolors-setrouteprogresscolors(<wbr/>/sdk-for-flutter-navigate-routing-sectiontransportmode sectionTransportMode, /sdk-for-flutter-navigate-navigation-routeprogresscolors-class routeProgressColors)
    → void

</dt>
<dd>
  Sets route color for visualization.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-visualnavigatorcolors-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-visualnavigatorcolors-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-methods">
<h2>Static Methods</h2>
<dl class="callables">
<dt class="callable" id="dayColors">
/sdk-for-flutter-navigate-navigation-visualnavigatorcolors-daycolors(<wbr/>)
    → /sdk-for-flutter-navigate-navigation-visualnavigatorcolors-class

</dt>
<dd>
  Retrieves HERE day color presets for route and maneuver arrow visualization.
  

</dd>
<dt class="callable" id="nightColors">
/sdk-for-flutter-navigate-navigation-visualnavigatorcolors-nightcolors(<wbr/>)
    → /sdk-for-flutter-navigate-navigation-visualnavigatorcolors-class

</dt>
<dd>
  Retrieves HERE night color presets for route and maneuver arrow visualization.
  

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
<li class="self-crumb">VisualNavigatorColors class</li>
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
