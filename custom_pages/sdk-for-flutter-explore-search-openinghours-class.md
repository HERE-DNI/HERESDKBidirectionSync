---
title: "Constructors"
slug: "sdk-for-flutter-explore-search-openinghours-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- OpeningHours-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/OpeningHours-class.html#constructors">Constructors</a></li>
<li><a href="search/OpeningHours/OpeningHours.html">OpeningHours</a></li>
<li class="section-title">
<a href="search/OpeningHours-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/OpeningHours/categories.html">categories</a></li>
<li><a href="search/OpeningHours/hashCode.html">hashCode</a></li>
<li><a href="search/OpeningHours/isOpen.html">isOpen</a></li>
<li class="inherited"><a href="search/OpeningHours/runtimeType.html">runtimeType</a></li>
<li><a href="search/OpeningHours/scheduleDetailsList.html">scheduleDetailsList</a></li>
<li><a href="search/OpeningHours/text.html">text</a></li>
<li class="section-title inherited"><a href="search/OpeningHours-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/OpeningHours/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/OpeningHours/toString.html">toString</a></li>
<li class="section-title"><a href="search/OpeningHours-class.html#operators">Operators</a></li>
<li><a href="search/OpeningHours/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">OpeningHours class</li>
</ol>
<div class="self-name">OpeningHours</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/OpeningHours-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>OpeningHours class</h1></div>
<section class="desc markdown">
<p>Represents opening hours information.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="OpeningHours">
<a href="../search/OpeningHours/OpeningHours.html">/sdk-for-flutter-explore-search-openinghours-openinghours</a>(List&lt;<wbr/>String&gt; text, bool isOpen, List&lt;<wbr/><a href="../search/ScheduleDetails-class.html">/sdk-for-flutter-explore-search-scheduledetails-class</a>&gt; scheduleDetailsList, List&lt;<wbr/><a href="../search/PlaceCategory-class.html">/sdk-for-flutter-explore-search-placecategory-class</a>&gt; categories)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="categories">
<a href="../search/OpeningHours/categories.html">/sdk-for-flutter-explore-search-openinghours-categories</a>
↔ List&lt;<wbr/><a href="../search/PlaceCategory-class.html">/sdk-for-flutter-explore-search-placecategory-class</a>&gt;
</dt>
<dd>
  The list of categories related to opening hours information.
This data is not available in offline search.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../search/OpeningHours/hashCode.html">/sdk-for-flutter-explore-search-openinghours-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="isOpen">
<a href="../search/OpeningHours/isOpen.html">/sdk-for-flutter-explore-search-openinghours-isopen</a>
↔ bool
</dt>
<dd>
  Boolean flag informing if the place is open or closed at the time when the search request was initiated.
For offline search, this is calculated using device's time,
so it may give incorrect value if device and place are located in different time zones.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../search/OpeningHours/runtimeType.html">/sdk-for-flutter-explore-search-openinghours-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="scheduleDetailsList">
<a href="../search/OpeningHours/scheduleDetailsList.html">/sdk-for-flutter-explore-search-openinghours-scheduledetailslist</a>
↔ List&lt;<wbr/><a href="../search/ScheduleDetails-class.html">/sdk-for-flutter-explore-search-scheduledetails-class</a>&gt;
</dt>
<dd>
  The list of schedule details.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="text">
<a href="../search/OpeningHours/text.html">/sdk-for-flutter-explore-search-openinghours-text</a>
↔ List&lt;<wbr/>String&gt;
</dt>
<dd>
  The list of opening hours presented as localized text.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../search/OpeningHours/noSuchMethod.html">/sdk-for-flutter-explore-search-openinghours-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../search/OpeningHours/toString.html">/sdk-for-flutter-explore-search-openinghours-tostring</a>(<wbr/>)
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
<a href="../search/OpeningHours/operator_equals.html">/sdk-for-flutter-explore-search-openinghours-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">OpeningHours class</li>
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
