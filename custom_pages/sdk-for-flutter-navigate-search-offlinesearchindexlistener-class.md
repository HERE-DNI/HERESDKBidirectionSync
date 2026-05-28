---
title: "OfflineSearchIndexListener class abstract"
slug: "sdk-for-flutter-navigate-search-offlinesearchindexlistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- OfflineSearchIndexListener-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/OfflineSearchIndexListener-class.html#constructors">Constructors</a></li>
<li><a href="search/OfflineSearchIndexListener/OfflineSearchIndexListener.html">OfflineSearchIndexListener</a></li>
<li class="section-title inherited">
<a href="search/OfflineSearchIndexListener-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="search/OfflineSearchIndexListener/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="search/OfflineSearchIndexListener/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="search/OfflineSearchIndexListener-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/OfflineSearchIndexListener/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="search/OfflineSearchIndexListener/onComplete.html">onComplete</a></li>
<li><a href="search/OfflineSearchIndexListener/onProgress.html">onProgress</a></li>
<li><a href="search/OfflineSearchIndexListener/onStarted.html">onStarted</a></li>
<li class="inherited"><a href="search/OfflineSearchIndexListener/toString.html">toString</a></li>
<li class="section-title inherited"><a href="search/OfflineSearchIndexListener-class.html#operators">Operators</a></li>
<li class="inherited"><a href="search/OfflineSearchIndexListener/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li class="self-crumb">OfflineSearchIndexListener class</li>
</ol>
<div class="self-name">OfflineSearchIndexListener</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/OfflineSearchIndexListener-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>OfflineSearchIndexListener class abstract</h1></div>
<section class="desc markdown">
<p>Abstract class to get updates about progress
of creating persistent map index.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="OfflineSearchIndexListener">
/sdk-for-flutter-navigate-search-offlinesearchindexlistener-offlinesearchindexlistener(void onStartedLambda(/sdk-for-flutter-navigate-search-offlinesearchindexoperation), void onProgressLambda(int), void onCompleteLambda(/sdk-for-flutter-navigate-search-offlinesearchindexerror?))
</dt>
<dd>
          Abstract class to get updates about progress
of creating persistent map index.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-search-offlinesearchindexlistener-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-search-offlinesearchindexlistener-runtimetype
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
/sdk-for-flutter-navigate-search-offlinesearchindexlistener-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="onComplete">
/sdk-for-flutter-navigate-search-offlinesearchindexlistener-oncomplete(<wbr/>/sdk-for-flutter-navigate-search-offlinesearchindexerror? error)
    → void

</dt>
<dd>
  Called after index creation or deletion has been completed.
  

</dd>
<dt class="callable" id="onProgress">
/sdk-for-flutter-navigate-search-offlinesearchindexlistener-onprogress(<wbr/>int percentage)
    → void

</dt>
<dd>
  Called multiple times to indicate the progress of index creation or deletion.
  

</dd>
<dt class="callable" id="onStarted">
/sdk-for-flutter-navigate-search-offlinesearchindexlistener-onstarted(<wbr/>/sdk-for-flutter-navigate-search-offlinesearchindexoperation operation)
    → void

</dt>
<dd>
  Called each time that the indexing has started.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-search-offlinesearchindexlistener-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-search-offlinesearchindexlistener-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li class="self-crumb">OfflineSearchIndexListener class</li>
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
`
}</HTMLBlock>
