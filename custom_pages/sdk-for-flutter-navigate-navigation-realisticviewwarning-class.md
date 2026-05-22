---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-realisticviewwarning-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RealisticViewWarning-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">RealisticViewWarning class</li>
</ol>
<div class="self-name">RealisticViewWarning</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/RealisticViewWarning-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RealisticViewWarning class</h1></div>
<section class="desc markdown">
<p>A realistic view notification.</p>
<p>This notification is given for complex junctions and it includes a visual
representation of that junction, in order to help the user to better navigate it. When
<code>RealisticViewWarning.distanceType</code> is /sdk-for-flutter-navigate-navigation-distancetype, the /sdk-for-flutter-navigate-navigation-realisticviewwarning-realisticviewvectorimage object
will be provided with the junction view and the signpost representations. For <code>RealisticViewWarning.distanceType</code>
with value /sdk-for-flutter-navigate-navigation-distancetype, the /sdk-for-flutter-navigate-navigation-realisticviewwarning-realisticviewvectorimage object will be null.
Use <code>RealisticViewWarningListener</code> to get notifications about the realistic views of the upcoming junctions.</p>
<p>Realistic view notifications require an online connection in order to function properly, or that the
junction or signpost map layer data is cached, installed or preloaded as part of a <code>Region</code>.
This can be enabled via feature configurations.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RealisticViewWarning">
/sdk-for-flutter-navigate-navigation-realisticviewwarning-realisticviewwarning(double distanceToRealisticViewInMeters, /sdk-for-flutter-navigate-navigation-distancetype distanceType)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="distanceToRealisticViewInMeters">
/sdk-for-flutter-navigate-navigation-realisticviewwarning-distancetorealisticviewinmeters
↔ double
</dt>
<dd>
  Distance to the junction, for which the realistic view is given, expressed in meters.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="distanceType">
/sdk-for-flutter-navigate-navigation-realisticviewwarning-distancetype
↔ /sdk-for-flutter-navigate-navigation-distancetype
</dt>
<dd>
  The distance type for the warning, e.g. a warning for a new realistic view ahead or a warning
for passing a realistic view. Since the realistic view warning is given relative to a single
position on the route, /sdk-for-flutter-navigate-navigation-distancetype will never be given for this warning.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-realisticviewwarning-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
/sdk-for-flutter-navigate-navigation-realisticviewwarning-id
↔ int
</dt>
<dd>
  Unique identifier for this specific realistic view warning instance.
Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
Use this ID to track, update, or dismiss individual warning instances of this type.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="realisticViewRasterImage">
/sdk-for-flutter-navigate-navigation-realisticviewwarning-realisticviewrasterimage
↔ /sdk-for-flutter-navigate-navigation-realisticviewrasterimage-class?
</dt>
<dd>
  The realistic view object for which the warning is given.
Image resources are stored as raster graphics.
Within /sdk-for-flutter-navigate-navigation-realisticviewwarning-class, only one type of image, either raster or vector, will be provided.
If this property is not <code>null</code>, then /sdk-for-flutter-navigate-navigation-realisticviewwarning-realisticviewvectorimage will be <code>null</code>.
<strong>Note:</strong> Certain countries support only raster images as realistic views. Currently, this is the case
only for Japan, but in the future, more countries might support this type of realistic views.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="realisticViewVectorImage">
/sdk-for-flutter-navigate-navigation-realisticviewwarning-realisticviewvectorimage
↔ /sdk-for-flutter-navigate-navigation-realisticviewvectorimage-class?
</dt>
<dd>
  The realistic view object for which the warning is given.
Image resources are stored as vector graphics.
Within /sdk-for-flutter-navigate-navigation-realisticviewwarning-class, only one type of image, either raster or vector, will be provided.
If this property is not <code>null</code>, then /sdk-for-flutter-navigate-navigation-realisticviewwarning-realisticviewrasterimage will be <code>null</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-realisticviewwarning-runtimetype
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
/sdk-for-flutter-navigate-navigation-realisticviewwarning-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-realisticviewwarning-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-realisticviewwarning-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">RealisticViewWarning class</li>
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
