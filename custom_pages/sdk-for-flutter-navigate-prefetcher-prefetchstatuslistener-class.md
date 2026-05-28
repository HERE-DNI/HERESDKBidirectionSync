---
title: "PrefetchStatusListener class abstract"
slug: "sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PrefetchStatusListener-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="prefetcher/PrefetchStatusListener-class.html#constructors">Constructors</a></li>
<li><a href="prefetcher/PrefetchStatusListener/PrefetchStatusListener.html">PrefetchStatusListener</a></li>
<li class="section-title inherited">
<a href="prefetcher/PrefetchStatusListener-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="prefetcher/PrefetchStatusListener/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="prefetcher/PrefetchStatusListener/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="prefetcher/PrefetchStatusListener-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="prefetcher/PrefetchStatusListener/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="prefetcher/PrefetchStatusListener/onComplete.html">onComplete</a></li>
<li><a href="prefetcher/PrefetchStatusListener/onProgress.html">onProgress</a></li>
<li class="inherited"><a href="prefetcher/PrefetchStatusListener/toString.html">toString</a></li>
<li class="section-title inherited"><a href="prefetcher/PrefetchStatusListener-class.html#operators">Operators</a></li>
<li class="inherited"><a href="prefetcher/PrefetchStatusListener/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-prefetcher-prefetcher-library</li>
<li class="self-crumb">PrefetchStatusListener class</li>
</ol>
<div class="self-name">PrefetchStatusListener</div>
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
<div class="main-content" data-above-sidebar="prefetcher/prefetcher-library-sidebar.html" data-below-sidebar="prefetcher/PrefetchStatusListener-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>PrefetchStatusListener class abstract</h1></div>
<section class="desc markdown">
<p>Abstract class to get notified on status updates
when prefetching map data.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="PrefetchStatusListener">
/sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-prefetchstatuslistener(void onProgressLambda(int), void onCompleteLambda(/sdk-for-flutter-navigate-maploader-maploadererror?))
</dt>
<dd>
          Abstract class to get notified on status updates
when prefetching map data.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-runtimetype
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
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="onComplete">
/sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-oncomplete(<wbr/>/sdk-for-flutter-navigate-maploader-maploadererror? error)
    → void

</dt>
<dd>
  Called after the geo-corridor data downloads has been completed either with success or with error.
  

</dd>
<dt class="callable" id="onProgress">
/sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-onprogress(<wbr/>int percentage)
    → void

</dt>
<dd>
  Called multiple times to indicate the update progress.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-prefetcher-prefetcher-library</li>
<li class="self-crumb">PrefetchStatusListener class</li>
</ol>
<h5>prefetcher library</h5>
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
