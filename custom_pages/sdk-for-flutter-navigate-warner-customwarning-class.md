---
title: "CustomWarning class"
slug: "sdk-for-flutter-navigate-warner-customwarning-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CustomWarning-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="warner/CustomWarning-class.html#constructors">Constructors</a></li>
<li><a href="warner/CustomWarning/CustomWarning.html">CustomWarning</a></li>
<li class="section-title">
<a href="warner/CustomWarning-class.html#instance-properties">Properties</a>
</li>
<li><a href="warner/CustomWarning/customWarningType.html">customWarningType</a></li>
<li><a href="warner/CustomWarning/endOffsetInMeters.html">endOffsetInMeters</a></li>
<li><a href="warner/CustomWarning/hashCode.html">hashCode</a></li>
<li><a href="warner/CustomWarning/id.html">id</a></li>
<li><a href="warner/CustomWarning/payload.html">payload</a></li>
<li class="inherited"><a href="warner/CustomWarning/runtimeType.html">runtimeType</a></li>
<li><a href="warner/CustomWarning/startOffsetInMeters.html">startOffsetInMeters</a></li>
<li class="section-title inherited"><a href="warner/CustomWarning-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="warner/CustomWarning/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="warner/CustomWarning/toString.html">toString</a></li>
<li class="section-title"><a href="warner/CustomWarning-class.html#operators">Operators</a></li>
<li><a href="warner/CustomWarning/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
<li class="self-crumb">CustomWarning class</li>
</ol>
<div class="self-name">CustomWarning</div>
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
<div class="main-content" data-above-sidebar="warner/warner-library-sidebar.html" data-below-sidebar="warner/CustomWarning-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>CustomWarning class</h1></div>
<section class="desc markdown">
<p>class container for custom warning data.</p>
<p>This structure represents the type-specific payload associated
with a custom warning.</p>
<p>Instances of this structure are typically produced by custom warning
evaluation logic and may also be retrieved from the <code>WarningRegistry</code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="CustomWarning">
/sdk-for-flutter-navigate-warner-customwarning-customwarning()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="customWarningType">
/sdk-for-flutter-navigate-warner-customwarning-customwarningtype
↔ int
</dt>
<dd>
  Identifier of the custom warning type.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="endOffsetInMeters">
/sdk-for-flutter-navigate-warner-customwarning-endoffsetinmeters
↔ double?
</dt>
<dd>
  End offset of the warning range along the segment.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-warner-customwarning-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
/sdk-for-flutter-navigate-warner-customwarning-id
↔ int
</dt>
<dd>
  Identifier of the warning.
The ID is unique only within its specific /sdk-for-flutter-navigate-warner-customwarning-customwarningtype and can be used
to retrieve additional information from a corresponding registry.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="payload">
/sdk-for-flutter-navigate-warner-customwarning-payload
↔ /sdk-for-flutter-navigate-core-metadata-class?
</dt>
<dd>
  Custom warning payload.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-warner-customwarning-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="startOffsetInMeters">
/sdk-for-flutter-navigate-warner-customwarning-startoffsetinmeters
↔ double
</dt>
<dd>
  Start offset of the warning range along the segment.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-warner-customwarning-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-warner-customwarning-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-warner-customwarning-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
<li class="self-crumb">CustomWarning class</li>
</ol>
<h5>warner library</h5>
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
