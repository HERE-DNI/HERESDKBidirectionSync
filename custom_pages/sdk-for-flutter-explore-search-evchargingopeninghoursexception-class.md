---
title: "Constructors"
slug: "sdk-for-flutter-explore-search-evchargingopeninghoursexception-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- EVChargingOpeningHoursException-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/EVChargingOpeningHoursException-class.html#constructors">Constructors</a></li>
<li><a href="search/EVChargingOpeningHoursException/EVChargingOpeningHoursException.html">EVChargingOpeningHoursException</a></li>
<li class="section-title">
<a href="search/EVChargingOpeningHoursException-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/EVChargingOpeningHoursException/closed.html">closed</a></li>
<li><a href="search/EVChargingOpeningHoursException/date.html">date</a></li>
<li><a href="search/EVChargingOpeningHoursException/hashCode.html">hashCode</a></li>
<li><a href="search/EVChargingOpeningHoursException/periods.html">periods</a></li>
<li class="inherited"><a href="search/EVChargingOpeningHoursException/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="search/EVChargingOpeningHoursException-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/EVChargingOpeningHoursException/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/EVChargingOpeningHoursException/toString.html">toString</a></li>
<li class="section-title"><a href="search/EVChargingOpeningHoursException-class.html#operators">Operators</a></li>
<li><a href="search/EVChargingOpeningHoursException/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">EVChargingOpeningHoursException class</li>
</ol>
<div class="self-name">EVChargingOpeningHoursException</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVChargingOpeningHoursException-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>EVChargingOpeningHoursException class</h1></div>
<section class="desc markdown">
<p>Represents exceptions to the regular opening hours schedule for EV charging locations,
such as special closures or extended hours.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="EVChargingOpeningHoursException">
<a href="../search/EVChargingOpeningHoursException/EVChargingOpeningHoursException.html">/sdk-for-flutter-explore-search-evchargingopeninghoursexception-evchargingopeninghoursexception</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="closed">
<a href="../search/EVChargingOpeningHoursException/closed.html">/sdk-for-flutter-explore-search-evchargingopeninghoursexception-closed</a>
↔ bool
</dt>
<dd>
  True if the charging location is closed on particular date, in which case
<a href="../search/EVChargingOpeningHoursException/periods.html">/sdk-for-flutter-explore-search-evchargingopeninghoursexception-periods</a> is empty.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="date">
<a href="../search/EVChargingOpeningHoursException/date.html">/sdk-for-flutter-explore-search-evchargingopeninghoursexception-date</a>
↔ DateTime
</dt>
<dd>
  Date of special opening hours.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../search/EVChargingOpeningHoursException/hashCode.html">/sdk-for-flutter-explore-search-evchargingopeninghoursexception-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="periods">
<a href="../search/EVChargingOpeningHoursException/periods.html">/sdk-for-flutter-explore-search-evchargingopeninghoursexception-periods</a>
↔ List&lt;<wbr/><a href="../search/TimeOfDayRange-class.html">/sdk-for-flutter-explore-search-timeofdayrange-class</a>&gt;
</dt>
<dd>
  A list of time periods when the charging location is open on the specified date.
The time periods are in the local time zone of the charging location, and
are represented as a list of objects with <a href="../search/TimeOfDayRange/from.html">/sdk-for-flutter-explore-search-timeofdayrange-from</a>
and <a href="../search/TimeOfDayRange/to.html">/sdk-for-flutter-explore-search-timeofdayrange-to</a> properties.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../search/EVChargingOpeningHoursException/runtimeType.html">/sdk-for-flutter-explore-search-evchargingopeninghoursexception-runtimetype</a>
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
<a href="../search/EVChargingOpeningHoursException/noSuchMethod.html">/sdk-for-flutter-explore-search-evchargingopeninghoursexception-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../search/EVChargingOpeningHoursException/toString.html">/sdk-for-flutter-explore-search-evchargingopeninghoursexception-tostring</a>(<wbr/>)
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
<a href="../search/EVChargingOpeningHoursException/operator_equals.html">/sdk-for-flutter-explore-search-evchargingopeninghoursexception-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">EVChargingOpeningHoursException class</li>
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
