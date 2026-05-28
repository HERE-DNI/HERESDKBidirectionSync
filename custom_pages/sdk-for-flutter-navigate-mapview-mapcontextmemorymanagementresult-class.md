---
title: "MapContextMemoryManagementResult class"
slug: "sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresult-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapContextMemoryManagementResult-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapContextMemoryManagementResult-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapContextMemoryManagementResult/MapContextMemoryManagementResult.html">MapContextMemoryManagementResult</a></li>
<li class="section-title">
<a href="mapview/MapContextMemoryManagementResult-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapview/MapContextMemoryManagementResult/diffBetweenVideoMemoryLimitAndRequirementInKiB.html">diffBetweenVideoMemoryLimitAndRequirementInKiB</a></li>
<li class="inherited"><a href="mapview/MapContextMemoryManagementResult/hashCode.html">hashCode</a></li>
<li><a href="mapview/MapContextMemoryManagementResult/resultCode.html">resultCode</a></li>
<li class="inherited"><a href="mapview/MapContextMemoryManagementResult/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="mapview/MapContextMemoryManagementResult-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview/MapContextMemoryManagementResult/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/MapContextMemoryManagementResult/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/MapContextMemoryManagementResult-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapContextMemoryManagementResult/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">MapContextMemoryManagementResult class</li>
</ol>
<div class="self-name">MapContextMemoryManagementResult</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapContextMemoryManagementResult-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapContextMemoryManagementResult class</h1></div>
<section class="desc markdown">
<p>Memory management result.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapContextMemoryManagementResult">
/sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresult-mapcontextmemorymanagementresult(/sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresultcode resultCode)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="diffBetweenVideoMemoryLimitAndRequirementInKiB">
/sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresult-diffbetweenvideomemorylimitandrequirementinkib
↔ int?
</dt>
<dd>
  The difference in kibibytes between the limit and the video-memory requirement
for only the currently visible data. If positive, the returned value is the surplus
value over the currently required bare minimum. Even when positive, if the limit set
is low, the application could later breach the limit and delete even visible data.
A non positive value means the limit cannot fit the existing visible data and there could
be data disappearing or flickering. If for some reason the callback is ignored or
correct memory limit cannot be calculated, <code>null</code> value is returned.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresult-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="resultCode">
/sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresult-resultcode
↔ /sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresultcode
</dt>
<dd>
  The result code of the memory management request.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresult-runtimetype
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
/sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresult-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresult-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresult-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
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
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">MapContextMemoryManagementResult class</li>
</ol>
<h5>mapview library</h5>
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
