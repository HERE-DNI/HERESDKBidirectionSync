---
title: "MapSceneLights class abstract"
slug: "sdk-for-flutter-explore-mapview-mapscenelights-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapSceneLights-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapSceneLights-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapSceneLights/MapSceneLights.html">MapSceneLights</a></li>
<li class="section-title inherited">
<a href="mapview/MapSceneLights-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview/MapSceneLights/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview/MapSceneLights/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview/MapSceneLights-class.html#instance-methods">Methods</a></li>
<li><a href="mapview/MapSceneLights/getColor.html">getColor</a></li>
<li><a href="mapview/MapSceneLights/getDirection.html">getDirection</a></li>
<li><a href="mapview/MapSceneLights/getIntensity.html">getIntensity</a></li>
<li class="inherited"><a href="mapview/MapSceneLights/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="mapview/MapSceneLights/reset.html">reset</a></li>
<li><a href="mapview/MapSceneLights/setColor.html">setColor</a></li>
<li><a href="mapview/MapSceneLights/setDirection.html">setDirection</a></li>
<li><a href="mapview/MapSceneLights/setIntensity.html">setIntensity</a></li>
<li class="inherited"><a href="mapview/MapSceneLights/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/MapSceneLights-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapSceneLights/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">MapSceneLights class</li>
</ol>
<div class="self-name">MapSceneLights</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapSceneLights-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapSceneLights class abstract</h1></div>
<section class="desc markdown">
<p>Manage the lights and their attributes in a scene.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapSceneLights">
/sdk-for-flutter-explore-mapview-mapscenelights-mapscenelights()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-mapview-mapscenelights-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-mapview-mapscenelights-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="getColor">
/sdk-for-flutter-explore-mapview-mapscenelights-getcolor(<wbr/>/sdk-for-flutter-explore-mapview-mapscenelightscategory category)
    → Color?

</dt>
<dd>
  Retrieves the current color of the light based on its category.
  

</dd>
<dt class="callable" id="getDirection">
/sdk-for-flutter-explore-mapview-mapscenelights-getdirection(<wbr/>/sdk-for-flutter-explore-mapview-mapscenelightscategory category)
    → /sdk-for-flutter-explore-mapview-mapscenelightsdirection-class?

</dt>
<dd>
  Retrieves the current direction of the light based on its category.
  

</dd>
<dt class="callable" id="getIntensity">
/sdk-for-flutter-explore-mapview-mapscenelights-getintensity(<wbr/>/sdk-for-flutter-explore-mapview-mapscenelightscategory category)
    → double?

</dt>
<dd>
  Retrieves the current intensity of the light based on its category.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-mapview-mapscenelights-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="reset">
/sdk-for-flutter-explore-mapview-mapscenelights-reset(<wbr/>)
    → void

</dt>
<dd>
  Resets all attributes of each light to their default values based on the current map scene settings.
  

</dd>
<dt class="callable" id="setColor">
/sdk-for-flutter-explore-mapview-mapscenelights-setcolor(<wbr/>/sdk-for-flutter-explore-mapview-mapscenelightscategory category, Color color, /sdk-for-flutter-explore-mapview-mapscenelightsattributesettingcallback? callback)
    → void

</dt>
<dd>
  Set a new color for the light based on its category.
  

</dd>
<dt class="callable" id="setDirection">
/sdk-for-flutter-explore-mapview-mapscenelights-setdirection(<wbr/>/sdk-for-flutter-explore-mapview-mapscenelightscategory category, /sdk-for-flutter-explore-mapview-mapscenelightsdirection-class direction, /sdk-for-flutter-explore-mapview-mapscenelightsattributesettingcallback? callback)
    → void

</dt>
<dd>
  Set a new direction for the light based on its category.
  

</dd>
<dt class="callable" id="setIntensity">
/sdk-for-flutter-explore-mapview-mapscenelights-setintensity(<wbr/>/sdk-for-flutter-explore-mapview-mapscenelightscategory category, double intensity, /sdk-for-flutter-explore-mapview-mapscenelightsattributesettingcallback? callback)
    → void

</dt>
<dd>
  Set a new intensity for the light based on its category.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-mapview-mapscenelights-tostring(<wbr/>)
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
/sdk-for-flutter-explore-mapview-mapscenelights-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">MapSceneLights class</li>
</ol>
<h5>mapview library</h5>
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
