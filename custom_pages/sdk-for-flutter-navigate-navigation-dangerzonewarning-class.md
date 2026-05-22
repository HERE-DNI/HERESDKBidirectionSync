---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-dangerzonewarning-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- DangerZoneWarning-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">DangerZoneWarning class</li>
</ol>
<div class="self-name">DangerZoneWarning</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/DangerZoneWarning-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>DangerZoneWarning class</h1></div>
<section class="desc markdown">
<p>Represents danger zones.</p>
<p>A danger zone refers to areas where there is an increased risk of
traffic incidents. These zones are designated to alert drivers to potential hazards and encourage
safer driving behaviors. Legally, certain devices can alert you to being in a danger zone,
typically indicating the presence of a speed camera. In line with applicable law and industry
standard, these alerts are usually provided along a road within a range of 4 km on a motorway,
2 km outside built-up areas, and 300 m in built-up areas​​. The HERE SDK warns when approaching
the danger zone, as well as when leaving such a zone. A danger zone may or may not have one or
more speed cameras in it. The exact location of such speed cameras is not provided. Note that
danger zones are only available in selected countries, such as France.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="DangerZoneWarning">
/sdk-for-flutter-navigate-navigation-dangerzonewarning-dangerzonewarning(bool isZoneStart, double distanceInMeters, /sdk-for-flutter-navigate-navigation-distancetype distanceType)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="distanceInMeters">
/sdk-for-flutter-navigate-navigation-dangerzonewarning-distanceinmeters
↔ double
</dt>
<dd>
  The distance from the current location to the Danger zone.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="distanceType">
/sdk-for-flutter-navigate-navigation-dangerzonewarning-distancetype
↔ /sdk-for-flutter-navigate-navigation-distancetype
</dt>
<dd>
  Indicates if the specified zone is ahead of the vehicle or has just passed by. If it is
ahead, then /sdk-for-flutter-navigate-navigation-dangerzonewarning-distanceinmeters is greater than 0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-dangerzonewarning-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
/sdk-for-flutter-navigate-navigation-dangerzonewarning-id
↔ int
</dt>
<dd>
  Unique identifier for this specific danger zone warning instance.
Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
Use this ID to track, update, or dismiss individual warning instances of this type.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isZoneStart">
/sdk-for-flutter-navigate-navigation-dangerzonewarning-iszonestart
↔ bool
</dt>
<dd>
  A flag indicating whether the Danger Zone officially start in the location the user is
entering it.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-dangerzonewarning-runtimetype
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
/sdk-for-flutter-navigate-navigation-dangerzonewarning-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-dangerzonewarning-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-dangerzonewarning-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">DangerZoneWarning class</li>
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
