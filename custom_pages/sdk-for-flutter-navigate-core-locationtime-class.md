---
title: "LocationTime class"
slug: "sdk-for-flutter-navigate-core-locationtime-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationTime-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core/LocationTime-class.html#constructors">Constructors</a></li>
<li><a href="core/LocationTime/LocationTime.html">LocationTime</a></li>
<li class="section-title">
<a href="core/LocationTime-class.html#instance-properties">Properties</a>
</li>
<li><a href="core/LocationTime/hashCode.html">hashCode</a></li>
<li><a href="core/LocationTime/localTime.html">localTime</a></li>
<li class="inherited"><a href="core/LocationTime/runtimeType.html">runtimeType</a></li>
<li><a href="core/LocationTime/utcOffset.html">utcOffset</a></li>
<li><a href="core/LocationTime/utcTime.html">utcTime</a></li>
<li class="section-title inherited"><a href="core/LocationTime-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="core/LocationTime/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core/LocationTime/toString.html">toString</a></li>
<li class="section-title"><a href="core/LocationTime-class.html#operators">Operators</a></li>
<li><a href="core/LocationTime/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li class="self-crumb">LocationTime class</li>
</ol>
<div class="self-name">LocationTime</div>
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
<div class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/LocationTime-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>LocationTime class</h1></div>
<section class="desc markdown">
<p>This struct presents all the time data tied to a location, like an arrival or departure time.</p>
<p>The time data is originally specified in RFC 3339, section 5.6 format. For example,
"2022-03-23T16:07:31+01:00" in Cracow, Poland, i.e. a Central European Time (CET) location.
Note that this struct doesn't give any data on the tied location. The location should be derived
from the context.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Annotations</dt>
<dd>
<ul class="annotation-list clazz-relationships">
<li>@<a href="https://pub.dev/documentation/meta/1.17.0/meta/immutable-constant.html">immutable</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="LocationTime">
/sdk-for-flutter-navigate-core-locationtime-locationtime(DateTime localTime, DateTime utcTime, Duration utcOffset)
</dt>
<dd>
          Creates a new instance.
            <div class="constructor-modifier features">const</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-core-locationtime-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="localTime">
/sdk-for-flutter-navigate-core-locationtime-localtime
→ DateTime
</dt>
<dd>
  The time as observed in the tied location. For example, if a route is requested in Cracow,
Poland, the local time is "2022-03-23T16:07:31" in CET, i.e. one hour ahead of the UTC time.
  <div class="features">final</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-core-locationtime-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="utcOffset">
/sdk-for-flutter-navigate-core-locationtime-utcoffset
→ Duration
</dt>
<dd>
  The UTC offset is the difference between the local time and the Coordinated Universal Time (UTC)
in seconds. For example, if the local time is UTC+01:00, it is +3600 and if the local time is
UTC-05:00, it is -18000.
  <div class="features">final</div>
</dd>
<dt class="property" id="utcTime">
/sdk-for-flutter-navigate-core-locationtime-utctime
→ DateTime
</dt>
<dd>
  The time as Coordinated Universal Time (UTC). For example, if a route is requested in Poland,
the UTC time is "2022-03-23T15:07:31", i.e. one hour behind the local time.
  <div class="features">final</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-core-locationtime-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-core-locationtime-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-core-locationtime-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li class="self-crumb">LocationTime class</li>
</ol>
<h5>core library</h5>
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
