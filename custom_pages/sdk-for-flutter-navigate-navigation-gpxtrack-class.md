---
title: "GPXTrack class abstract"
slug: "sdk-for-flutter-navigate-navigation-gpxtrack-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- GPXTrack-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/GPXTrack-class.html#constructors">Constructors</a></li>
<li><a href="navigation/GPXTrack/GPXTrack.html">GPXTrack</a></li>
<li class="section-title">
<a href="navigation/GPXTrack-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/GPXTrack/description.html">description</a></li>
<li class="inherited"><a href="navigation/GPXTrack/hashCode.html">hashCode</a></li>
<li><a href="navigation/GPXTrack/name.html">name</a></li>
<li class="inherited"><a href="navigation/GPXTrack/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="navigation/GPXTrack-class.html#instance-methods">Methods</a></li>
<li><a href="navigation/GPXTrack/getLocations.html">getLocations</a></li>
<li class="inherited"><a href="navigation/GPXTrack/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/GPXTrack/toString.html">toString</a></li>
<li class="section-title inherited"><a href="navigation/GPXTrack-class.html#operators">Operators</a></li>
<li class="inherited"><a href="navigation/GPXTrack/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">GPXTrack class</li>
</ol>
<div class="self-name">GPXTrack</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/GPXTrack-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>GPXTrack class abstract</h1></div>
<section class="desc markdown">
<p>Single track from the /sdk-for-flutter-navigate-navigation-gpxdocument-class.</p>
<p>Can be used as an input to the /sdk-for-flutter-navigate-navigation-locationsimulator-class.
Can be created and modified via /sdk-for-flutter-navigate-navigation-gpxtrackwriter-class.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="GPXTrack">
/sdk-for-flutter-navigate-navigation-gpxtrack-gpxtrack()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="description">
/sdk-for-flutter-navigate-navigation-gpxtrack-description
↔ String
</dt>
<dd>
  The value of the description of the element in the trkType.
Can be overridden by the user. If nothing was set before, defaults to an empty string.
Gets the value of the description of the element in the trkType. If nothing was set before, defaults to an empty string.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-navigation-gpxtrack-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="name">
/sdk-for-flutter-navigate-navigation-gpxtrack-name
↔ String
</dt>
<dd>
  The value of the name of the element in the trkType.
Can be overridden by the user. If nothing was set before, defaults to an empty string.
Gets the value of the name of the element in the trkType. If nothing was set before, defaults to an empty string.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-gpxtrack-runtimetype
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
<dt class="callable" id="getLocations">
/sdk-for-flutter-navigate-navigation-gpxtrack-getlocations(<wbr/>)
    → List&lt;<wbr/>/sdk-for-flutter-navigate-core-location-class&gt;

</dt>
<dd>
  Provides a list of all stored track points converted to a /sdk-for-flutter-navigate-core-location-class object.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-gpxtrack-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-gpxtrack-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-gpxtrack-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">GPXTrack class</li>
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
