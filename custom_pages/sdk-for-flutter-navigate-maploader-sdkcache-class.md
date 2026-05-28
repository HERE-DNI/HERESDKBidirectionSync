---
title: "SDKCache class abstract"
slug: "sdk-for-flutter-navigate-maploader-sdkcache-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SDKCache-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="maploader/SDKCache-class.html#constructors">Constructors</a></li>
<li><a href="maploader/SDKCache/SDKCache.html">SDKCache</a></li>
<li class="section-title inherited">
<a href="maploader/SDKCache-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="maploader/SDKCache/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="maploader/SDKCache/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="maploader/SDKCache-class.html#instance-methods">Methods</a></li>
<li><a href="maploader/SDKCache/clearAppCache.html">clearAppCache</a></li>
<li class="inherited"><a href="maploader/SDKCache/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="maploader/SDKCache/toString.html">toString</a></li>
<li class="section-title inherited"><a href="maploader/SDKCache-class.html#operators">Operators</a></li>
<li class="inherited"><a href="maploader/SDKCache/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="maploader/SDKCache-class.html#static-methods">Static methods</a></li>
<li><a href="maploader/SDKCache/fromSdkEngine.html">fromSdkEngine</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li class="self-crumb">SDKCache class</li>
</ol>
<div class="self-name">SDKCache</div>
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
<div class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="maploader/SDKCache-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>SDKCache class abstract</h1></div>
<section class="desc markdown">
<p>A class to manage SDK Cache.</p>
<p>Path for SDKCache is specified via /sdk-for-flutter-navigate-core-engine-sdkoptions-cachepath.
SDKCache manages temporary downloaded map data during map interaction and follows LRU (least recently used) strategy to delete
map data when cache size exceeds the specified /sdk-for-flutter-navigate-core-engine-sdkoptions-cachesizeinbytes.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="SDKCache">
/sdk-for-flutter-navigate-maploader-sdkcache-sdkcache()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-maploader-sdkcache-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-maploader-sdkcache-runtimetype
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
<dt class="callable" id="clearAppCache">
/sdk-for-flutter-navigate-maploader-sdkcache-clearappcache(<wbr/>/sdk-for-flutter-navigate-maploader-sdkcachecallback callback)
    → void

</dt>
<dd>
  Clears all data that is currently stored in the SDK cache.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-maploader-sdkcache-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-maploader-sdkcache-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-maploader-sdkcache-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-methods">
<h2>Static Methods</h2>
<dl class="callables">
<dt class="callable" id="fromSdkEngine">
/sdk-for-flutter-navigate-maploader-sdkcache-fromsdkengine(<wbr/>/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine)
    → /sdk-for-flutter-navigate-maploader-sdkcache-class

</dt>
<dd>
  Gets a single instance of this class per provided /sdk-for-flutter-navigate-core-engine-sdknativeengine-class.
  

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
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li class="self-crumb">SDKCache class</li>
</ol>
<h5>maploader library</h5>
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
