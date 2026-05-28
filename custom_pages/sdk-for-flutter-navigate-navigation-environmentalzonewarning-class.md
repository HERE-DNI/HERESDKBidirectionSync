---
title: "EnvironmentalZoneWarning class"
slug: "sdk-for-flutter-navigate-navigation-environmentalzonewarning-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EnvironmentalZoneWarning-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/EnvironmentalZoneWarning-class.html#constructors">Constructors</a></li>
<li><a href="navigation/EnvironmentalZoneWarning/EnvironmentalZoneWarning.html">EnvironmentalZoneWarning</a></li>
<li class="section-title">
<a href="navigation/EnvironmentalZoneWarning-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/EnvironmentalZoneWarning/description.html">description</a></li>
<li><a href="navigation/EnvironmentalZoneWarning/distanceInMeters.html">distanceInMeters</a></li>
<li><a href="navigation/EnvironmentalZoneWarning/distanceType.html">distanceType</a></li>
<li><a href="navigation/EnvironmentalZoneWarning/hashCode.html">hashCode</a></li>
<li><a href="navigation/EnvironmentalZoneWarning/id.html">id</a></li>
<li><a href="navigation/EnvironmentalZoneWarning/name.html">name</a></li>
<li class="inherited"><a href="navigation/EnvironmentalZoneWarning/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/EnvironmentalZoneWarning/websiteUrl.html">websiteUrl</a></li>
<li><a href="navigation/EnvironmentalZoneWarning/zoneId.html">zoneId</a></li>
<li class="section-title inherited"><a href="navigation/EnvironmentalZoneWarning-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/EnvironmentalZoneWarning/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/EnvironmentalZoneWarning/toString.html">toString</a></li>
<li class="section-title"><a href="navigation/EnvironmentalZoneWarning-class.html#operators">Operators</a></li>
<li><a href="navigation/EnvironmentalZoneWarning/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">EnvironmentalZoneWarning class</li>
</ol>
<div class="self-name">EnvironmentalZoneWarning</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/EnvironmentalZoneWarning-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>EnvironmentalZoneWarning class</h1></div>
<section class="desc markdown">
<p>Represents Environmental zones.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="EnvironmentalZoneWarning">
/sdk-for-flutter-navigate-navigation-environmentalzonewarning-environmentalzonewarning(double distanceInMeters, /sdk-for-flutter-navigate-navigation-distancetype distanceType, String zoneId, String name)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="description">
/sdk-for-flutter-navigate-navigation-environmentalzonewarning-description
↔ /sdk-for-flutter-navigate-core-localizedtexts-class
</dt>
<dd>
  Indicates the description of the environmental zone in the available languages.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="distanceInMeters">
/sdk-for-flutter-navigate-navigation-environmentalzonewarning-distanceinmeters
↔ double
</dt>
<dd>
  The distance from the current location to the environmental zone.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="distanceType">
/sdk-for-flutter-navigate-navigation-environmentalzonewarning-distancetype
↔ /sdk-for-flutter-navigate-navigation-distancetype
</dt>
<dd>
  Indicates if the specified zone is ahead of the vehicle or has just passed by. If it is
ahead, then /sdk-for-flutter-navigate-navigation-environmentalzonewarning-distanceinmeters is greater than 0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-environmentalzonewarning-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
/sdk-for-flutter-navigate-navigation-environmentalzonewarning-id
↔ int
</dt>
<dd>
  Unique identifier for this specific environmental zone warning instance.
Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
Use this ID to track, update, or dismiss individual warning instances of this type.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="name">
/sdk-for-flutter-navigate-navigation-environmentalzonewarning-name
↔ String
</dt>
<dd>
  Indicates the official name of the environmental zone.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-environmentalzonewarning-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="websiteUrl">
/sdk-for-flutter-navigate-navigation-environmentalzonewarning-websiteurl
↔ String?
</dt>
<dd>
  Indicates the website of the environmental zone, if available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="zoneId">
/sdk-for-flutter-navigate-navigation-environmentalzonewarning-zoneid
↔ String
</dt>
<dd>
  Indicates the environmental zone id in the map data.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-environmentalzonewarning-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-environmentalzonewarning-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-environmentalzonewarning-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">EnvironmentalZoneWarning class</li>
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
