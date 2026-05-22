---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mapcontext-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapContext-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
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
/sdk-for-flutter-navigate-mapview-mapcontext-mapcontext()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-mapview-mapcontext-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapview-mapcontext-runtimetype
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
/sdk-for-flutter-navigate-mapview-mapcontext-freeresource(<wbr/>/sdk-for-flutter-navigate-mapview-mapcontextresourcetype type, /sdk-for-flutter-navigate-mapview-mapcontextfreeresourceseverity severity)
    → void

</dt>
<dd>
  Frees a system resource held by the /sdk-for-flutter-navigate-mapview-mapcontext-class and all entities attached to it, like /sdk-for-flutter-navigate-mapview-heremapcontrollercore-class.
  

</dd>
<dt class="callable" id="getMemoryManagementOptions">
/sdk-for-flutter-navigate-mapview-mapcontext-getmemorymanagementoptions(<wbr/>)
    → /sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementoptions-class

</dt>
<dd>
  Returns /sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementoptions-class. Gets the current memory management options.
Returns the actual applied memory limits. If the underlying system limits exceed
int32_t max value (2,147,483,647 KiB or ~2 TiB), the returned value is clamped to int32_t max.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapview-mapcontext-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="setMemoryManagementOptions">
/sdk-for-flutter-navigate-mapview-mapcontext-setmemorymanagementoptions(<wbr/>/sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementoptions-class memoryManagementOptions, /sdk-for-flutter-navigate-mapview-mapcontextsetmemorymanagementoptionscallback? callback)
    → void

</dt>
<dd>
  Sets memory management options for controlling tile cache and video memory usage.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapview-mapcontext-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-mapview-mapcontext-operator-equals(<wbr/>Object other)
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



</div>
`
}</HTMLBlock>
