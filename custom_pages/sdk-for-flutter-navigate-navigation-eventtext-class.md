---
title: "EventText class"
slug: "sdk-for-flutter-navigate-navigation-eventtext-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EventText-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/EventText-class.html#constructors">Constructors</a></li>
<li><a href="navigation/EventText/EventText.html">EventText</a></li>
<li class="section-title">
<a href="navigation/EventText-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/EventText/distanceInMeters.html">distanceInMeters</a></li>
<li><a href="navigation/EventText/hashCode.html">hashCode</a></li>
<li><a href="navigation/EventText/maneuverNotificationDetails.html">maneuverNotificationDetails</a></li>
<li class="inherited"><a href="navigation/EventText/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/EventText/spatialNotificationDetails.html">spatialNotificationDetails</a></li>
<li><a href="navigation/EventText/text.html">text</a></li>
<li><a href="navigation/EventText/type.html">type</a></li>
<li class="section-title inherited"><a href="navigation/EventText-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/EventText/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/EventText/toString.html">toString</a></li>
<li class="section-title"><a href="navigation/EventText-class.html#operators">Operators</a></li>
<li><a href="navigation/EventText/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">EventText class</li>
</ol>
<div class="self-name">EventText</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/EventText-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>EventText class</h1></div>
<section class="desc markdown">
<p>Contains all the information regarding the next text announcement.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="EventText">
/sdk-for-flutter-navigate-navigation-eventtext-eventtext(/sdk-for-flutter-navigate-navigation-textnotificationtype type, double distanceInMeters, String text)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="distanceInMeters">
/sdk-for-flutter-navigate-navigation-eventtext-distanceinmeters
↔ double
</dt>
<dd>
  Distance in meters to the location of the event for which the text notification is given.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-eventtext-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="maneuverNotificationDetails">
/sdk-for-flutter-navigate-navigation-eventtext-maneuvernotificationdetails
↔ /sdk-for-flutter-navigate-navigation-maneuvernotificationdetails-class?
</dt>
<dd>
  Information about the next maneuver.
Is non-<code>null</code> only for /sdk-for-flutter-navigate-navigation-eventtext-type equals to /sdk-for-flutter-navigate-navigation-textnotificationtype.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-eventtext-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="spatialNotificationDetails">
/sdk-for-flutter-navigate-navigation-eventtext-spatialnotificationdetails
↔ /sdk-for-flutter-navigate-navigation-spatialnotificationdetails-class?
</dt>
<dd>
  Information for a spatial text notifications.
When /sdk-for-flutter-navigate-navigation-eventtextoptions-enablespatialaudio is false,
then this attribute will be <code>null</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="text">
/sdk-for-flutter-navigate-navigation-eventtext-text
↔ String
</dt>
<dd>
  The text notification instruction. The text is formatted and localized as specified via
/sdk-for-flutter-navigate-routing-routetextoptions-class.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="type">
/sdk-for-flutter-navigate-navigation-eventtext-type
↔ /sdk-for-flutter-navigate-navigation-textnotificationtype
</dt>
<dd>
  Indicates the type of text announcement
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-eventtext-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-eventtext-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-eventtext-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">EventText class</li>
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
