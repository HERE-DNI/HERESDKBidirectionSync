---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-sectionnotice-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- SectionNotice-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/SectionNotice-class.html#constructors">Constructors</a></li>
<li><a href="routing/SectionNotice/SectionNotice.html">SectionNotice</a></li>
<li class="section-title">
<a href="routing/SectionNotice-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/SectionNotice/code.html">code</a></li>
<li><a href="routing/SectionNotice/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="routing/SectionNotice/runtimeType.html">runtimeType</a></li>
<li><a href="routing/SectionNotice/severity.html">severity</a></li>
<li><a href="routing/SectionNotice/violatedRestrictions.html">violatedRestrictions</a></li>
<li class="section-title inherited"><a href="routing/SectionNotice-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/SectionNotice/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/SectionNotice/toString.html">toString</a></li>
<li class="section-title"><a href="routing/SectionNotice-class.html#operators">Operators</a></li>
<li><a href="routing/SectionNotice/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">SectionNotice class</li>
</ol>
<div class="self-name">SectionNotice</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/SectionNotice-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>SectionNotice class</h1></div>
<section class="desc markdown">
<p>Explains an issue encountered in a <a href="../routing/Section-class.html">/sdk-for-flutter-explore-routing-section-class</a>.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="SectionNotice">
<a href="../routing/SectionNotice/SectionNotice.html">/sdk-for-flutter-explore-routing-sectionnotice-sectionnotice</a>(<a href="../routing/SectionNoticeCode.html">/sdk-for-flutter-explore-routing-sectionnoticecode</a> code, <a href="../routing/NoticeSeverity.html">/sdk-for-flutter-explore-routing-noticeseverity</a> severity)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="code">
<a href="../routing/SectionNotice/code.html">/sdk-for-flutter-explore-routing-sectionnotice-code</a>
↔ <a href="../routing/SectionNoticeCode.html">/sdk-for-flutter-explore-routing-sectionnoticecode</a>
</dt>
<dd>
  The notice code.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../routing/SectionNotice/hashCode.html">/sdk-for-flutter-explore-routing-sectionnotice-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/SectionNotice/runtimeType.html">/sdk-for-flutter-explore-routing-sectionnotice-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="severity">
<a href="../routing/SectionNotice/severity.html">/sdk-for-flutter-explore-routing-sectionnotice-severity</a>
↔ <a href="../routing/NoticeSeverity.html">/sdk-for-flutter-explore-routing-noticeseverity</a>
</dt>
<dd>
  The notice severity.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="violatedRestrictions">
<a href="../routing/SectionNotice/violatedRestrictions.html">/sdk-for-flutter-explore-routing-sectionnotice-violatedrestrictions</a>
↔ List&lt;<wbr/><a href="../routing/ViolatedRestriction-class.html">/sdk-for-flutter-explore-routing-violatedrestriction-class</a>&gt;
</dt>
<dd>
  The following property <code>violated_restrictions</code> contains the notice detail information.
Only three types of restrictions can have notice details: time dependent restriction, vehicle restriction and transport mode restriction.
There is no one-to-one match of the <code>SectionNotice.code</code> and these three restriction types. For example, if <code>SectionNotice.code</code> is
<a href="../routing/SectionNoticeCode.html">/sdk-for-flutter-explore-routing-sectionnoticecode</a>, then it can be either vehicle restriction or transport mode restriction. If <code>SectionNotice.code</code> is
<a href="../routing/SectionNoticeCode.html">/sdk-for-flutter-explore-routing-sectionnoticecode</a>, then it is time dependent restriction.
If the section notice is none of the above-mentioned three types, then this will be an empty list.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../routing/SectionNotice/noSuchMethod.html">/sdk-for-flutter-explore-routing-sectionnotice-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/SectionNotice/toString.html">/sdk-for-flutter-explore-routing-sectionnotice-tostring</a>(<wbr/>)
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
<a href="../routing/SectionNotice/operator_equals.html">/sdk-for-flutter-explore-routing-sectionnotice-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">SectionNotice class</li>
</ol>
<h5>routing library</h5>
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
