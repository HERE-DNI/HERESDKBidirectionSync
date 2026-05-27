---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-mapcontext-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- MapContext-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapContext-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapContext/MapContext.html">MapContext</a></li>
<li class="section-title inherited">
<a href="mapview/MapContext-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview/MapContext/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview/MapContext/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview/MapContext-class.html#instance-methods">Methods</a></li>
<li><a href="mapview/MapContext/freeResource.html">freeResource</a></li>
<li><a href="mapview/MapContext/getMemoryManagementOptions.html">getMemoryManagementOptions</a></li>
<li class="inherited"><a href="mapview/MapContext/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="mapview/MapContext/setMemoryManagementOptions.html">setMemoryManagementOptions</a></li>
<li class="inherited"><a href="mapview/MapContext/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/MapContext-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapContext/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapContext class</li>
</ol>
<div class="self-name">MapContext</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapContext-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapContext class abstract</h1></div>
<section class="desc markdown">
<p>MapContext is the rendering engine and the context in which virtual geographic maps get rendered.</p>
<p>It runs the render loop or offers the means for the user to run a custom one.</p>
<p>Data sources, assets and virtual maps can be attached to the context. A virtual map can only
render data from sources attached to the same context.</p>
<p>The graphics backend to be used by the engine can be choosen by the user or a platform suitable
one can be automatically selected internally. Only one graphics backend can be active and once
selected it cannot be changed.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapContext">
<a href="../mapview/MapContext/MapContext.html">/sdk-for-flutter-explore-mapview-mapcontext-mapcontext</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../mapview/MapContext/hashCode.html">/sdk-for-flutter-explore-mapview-mapcontext-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview/MapContext/runtimeType.html">/sdk-for-flutter-explore-mapview-mapcontext-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="freeResource">
<a href="../mapview/MapContext/freeResource.html">/sdk-for-flutter-explore-mapview-mapcontext-freeresource</a>(<wbr/><a href="../mapview/MapContextResourceType.html">/sdk-for-flutter-explore-mapview-mapcontextresourcetype</a> type, <a href="../mapview/MapContextFreeResourceSeverity.html">/sdk-for-flutter-explore-mapview-mapcontextfreeresourceseverity</a> severity)
    → void

</dt>
<dd>
  Frees a system resource held by the <a href="../mapview/MapContext-class.html">/sdk-for-flutter-explore-mapview-mapcontext-class</a> and all entities attached to it, like <a href="../mapview/HereMapControllerCore-class.html">/sdk-for-flutter-explore-mapview-heremapcontrollercore-class</a>.
  

</dd>
<dt class="callable" id="getMemoryManagementOptions">
<a href="../mapview/MapContext/getMemoryManagementOptions.html">/sdk-for-flutter-explore-mapview-mapcontext-getmemorymanagementoptions</a>(<wbr/>)
    → <a href="../mapview/MapContextMemoryManagementOptions-class.html">/sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-class</a>
</dt>
<dd>
  Returns <a href="../mapview/MapContextMemoryManagementOptions-class.html">/sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-class</a>. Gets the current memory management options.
Returns the actual applied memory limits. If the underlying system limits exceed
int32_t max value (2,147,483,647 KiB or ~2 TiB), the returned value is clamped to int32_t max.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview/MapContext/noSuchMethod.html">/sdk-for-flutter-explore-mapview-mapcontext-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="setMemoryManagementOptions">
<a href="../mapview/MapContext/setMemoryManagementOptions.html">/sdk-for-flutter-explore-mapview-mapcontext-setmemorymanagementoptions</a>(<wbr/><a href="../mapview/MapContextMemoryManagementOptions-class.html">/sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-class</a> memoryManagementOptions, <a href="../mapview/MapContextSetMemoryManagementOptionsCallback.html">/sdk-for-flutter-explore-mapview-mapcontextsetmemorymanagementoptionscallback</a>? callback)
    → void

</dt>
<dd>
  Sets memory management options for controlling tile cache and video memory usage.
  

</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview/MapContext/toString.html">/sdk-for-flutter-explore-mapview-mapcontext-tostring</a>(<wbr/>)
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
<a href="../mapview/MapContext/operator_equals.html">/sdk-for-flutter-explore-mapview-mapcontext-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapContext class</li>
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
</HTMLBlock>
