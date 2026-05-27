---
title: "Constructors"
slug: "sdk-for-flutter-explore-search-evchargingopeninghours-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- EVChargingOpeningHours-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/EVChargingOpeningHours-class.html#constructors">Constructors</a></li>
<li><a href="search/EVChargingOpeningHours/EVChargingOpeningHours.html">EVChargingOpeningHours</a></li>
<li class="section-title">
<a href="search/EVChargingOpeningHours-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/EVChargingOpeningHours/chargingWhenClosed.html">chargingWhenClosed</a></li>
<li><a href="search/EVChargingOpeningHours/exceptions.html">exceptions</a></li>
<li><a href="search/EVChargingOpeningHours/hashCode.html">hashCode</a></li>
<li><a href="search/EVChargingOpeningHours/open24x7.html">open24x7</a></li>
<li><a href="search/EVChargingOpeningHours/regularSchedule.html">regularSchedule</a></li>
<li class="inherited"><a href="search/EVChargingOpeningHours/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="search/EVChargingOpeningHours-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/EVChargingOpeningHours/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/EVChargingOpeningHours/toString.html">toString</a></li>
<li class="section-title"><a href="search/EVChargingOpeningHours-class.html#operators">Operators</a></li>
<li><a href="search/EVChargingOpeningHours/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">EVChargingOpeningHours class</li>
</ol>
<div class="self-name">EVChargingOpeningHours</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVChargingOpeningHours-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>EVChargingOpeningHours class</h1></div>
<section class="desc markdown">
<p>Represents the times when the EVSEs at the charging location can be accessed for charging.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="EVChargingOpeningHours">
<a href="../search/EVChargingOpeningHours/EVChargingOpeningHours.html">/sdk-for-flutter-explore-search-evchargingopeninghours-evchargingopeninghours</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="chargingWhenClosed">
<a href="../search/EVChargingOpeningHours/chargingWhenClosed.html">/sdk-for-flutter-explore-search-evchargingopeninghours-chargingwhenclosed</a>
↔ bool
</dt>
<dd>
  Indicates if it is allowed to leave vehicles in the charging location to continue
charging outside opening hours.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="exceptions">
<a href="../search/EVChargingOpeningHours/exceptions.html">/sdk-for-flutter-explore-search-evchargingopeninghours-exceptions</a>
↔ List&lt;<wbr/><a href="../search/EVChargingOpeningHoursException-class.html">/sdk-for-flutter-explore-search-evchargingopeninghoursexception-class</a>&gt;
</dt>
<dd>
  List of opening hours exceptions for EV charging locations.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../search/EVChargingOpeningHours/hashCode.html">/sdk-for-flutter-explore-search-evchargingopeninghours-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="open24x7">
<a href="../search/EVChargingOpeningHours/open24x7.html">/sdk-for-flutter-explore-search-evchargingopeninghours-open24x7</a>
↔ bool
</dt>
<dd>
  Indicates if the charging location is open 24 hours a day, 7 days per week.
If true, <a href="../search/EVChargingOpeningHours/regularSchedule.html">/sdk-for-flutter-explore-search-evchargingopeninghours-regularschedule</a> and <a href="../search/EVChargingOpeningHours/exceptions.html">/sdk-for-flutter-explore-search-evchargingopeninghours-exceptions</a> will be empty.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="regularSchedule">
<a href="../search/EVChargingOpeningHours/regularSchedule.html">/sdk-for-flutter-explore-search-evchargingopeninghours-regularschedule</a>
↔ List&lt;<wbr/><a href="../search/EVChargingOpeningHoursSchedule-class.html">/sdk-for-flutter-explore-search-evchargingopeninghoursschedule-class</a>&gt;
</dt>
<dd>
  List of regular opening hours schedule for EV charging locations.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../search/EVChargingOpeningHours/runtimeType.html">/sdk-for-flutter-explore-search-evchargingopeninghours-runtimetype</a>
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
<a href="../search/EVChargingOpeningHours/noSuchMethod.html">/sdk-for-flutter-explore-search-evchargingopeninghours-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../search/EVChargingOpeningHours/toString.html">/sdk-for-flutter-explore-search-evchargingopeninghours-tostring</a>(<wbr/>)
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
<a href="../search/EVChargingOpeningHours/operator_equals.html">/sdk-for-flutter-explore-search-evchargingopeninghours-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">EVChargingOpeningHours class</li>
</ol>
<h5>search library</h5>
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
</HTMLBlock>
