---
title: "ManeuverNotificationDetails class"
slug: "sdk-for-flutter-navigate-navigation-maneuvernotificationdetails-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ManeuverNotificationDetails-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/ManeuverNotificationDetails-class.html#constructors">Constructors</a></li>
<li><a href="navigation/ManeuverNotificationDetails/ManeuverNotificationDetails.html">ManeuverNotificationDetails</a></li>
<li class="section-title">
<a href="navigation/ManeuverNotificationDetails-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/ManeuverNotificationDetails/hashCode.html">hashCode</a></li>
<li><a href="navigation/ManeuverNotificationDetails/isCombinedManeuverText.html">isCombinedManeuverText</a></li>
<li><a href="navigation/ManeuverNotificationDetails/maneuver.html">maneuver</a></li>
<li><a href="navigation/ManeuverNotificationDetails/maneuverNotificationType.html">maneuverNotificationType</a></li>
<li class="inherited"><a href="navigation/ManeuverNotificationDetails/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="navigation/ManeuverNotificationDetails-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/ManeuverNotificationDetails/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/ManeuverNotificationDetails/toString.html">toString</a></li>
<li class="section-title"><a href="navigation/ManeuverNotificationDetails-class.html#operators">Operators</a></li>
<li><a href="navigation/ManeuverNotificationDetails/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">ManeuverNotificationDetails class</li>
</ol>
<div class="self-name">ManeuverNotificationDetails</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/ManeuverNotificationDetails-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>ManeuverNotificationDetails class</h1></div>
<section class="desc markdown">
<p>This class provides the information regarding the next maneuver to be triggered</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="ManeuverNotificationDetails">
/sdk-for-flutter-navigate-navigation-maneuvernotificationdetails-maneuvernotificationdetails(/sdk-for-flutter-navigate-routing-maneuver-class maneuver, /sdk-for-flutter-navigate-navigation-maneuvernotificationtype maneuverNotificationType)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-maneuvernotificationdetails-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="isCombinedManeuverText">
/sdk-for-flutter-navigate-navigation-maneuvernotificationdetails-iscombinedmaneuvertext
↔ bool
</dt>
<dd>
  Indicates whether the current text notification combines information regarding current and next maneuver,
such as, "Now turn right and then turn left onto Invalidenstrasse", or not.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maneuver">
/sdk-for-flutter-navigate-navigation-maneuvernotificationdetails-maneuver
↔ /sdk-for-flutter-navigate-routing-maneuver-class
</dt>
<dd>
  Current maneuver data. In case of a double maneuver e.g. "Now turn right and then turn left",
this attribute will contain the maneuver data of the first maneuver of the combined maneuver "Now turn right".
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maneuverNotificationType">
/sdk-for-flutter-navigate-navigation-maneuvernotificationdetails-maneuvernotificationtype
↔ /sdk-for-flutter-navigate-navigation-maneuvernotificationtype
</dt>
<dd>
  Indicates the type of the current maneuver notification.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-maneuvernotificationdetails-runtimetype
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
/sdk-for-flutter-navigate-navigation-maneuvernotificationdetails-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-maneuvernotificationdetails-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-maneuvernotificationdetails-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">ManeuverNotificationDetails class</li>
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
