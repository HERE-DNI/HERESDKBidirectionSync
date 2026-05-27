---
title: "Implementation"
slug: "sdk-for-flutter-explore-search-webimage-hashcode"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- hashCode.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li><a href="../../search/WebImage-class.html">/sdk-for-flutter-explore-search-webimage-class</a></li>
<li class="self-crumb">hashCode property</li>
</ol>
<div class="self-name">hashCode</div>
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
<div class="main-content" data-above-sidebar="search/WebImage-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>hashCode property</h1></div>
<section id="getter">
<section class="multi-line-signature">
<div>
<ol class="annotation-list">
<li>@override</li>
</ol>
</div>
int
hashCode
</section>
<section class="desc markdown">
<p>The hash code for this object.</p>
<p>A hash code is a single integer which represents the state of the object
that affects <a href="../../search/WebImage/operator_equals.html">/sdk-for-flutter-explore-search-webimage-operator-equals</a> comparisons.</p>
<p>All objects have hash codes.
The default hash code implemented by <code>Object</code>
represents only the identity of the object,
the same way as the default <a href="../../search/WebImage/operator_equals.html">/sdk-for-flutter-explore-search-webimage-operator-equals</a> implementation only considers objects
equal if they are identical (see <code>identityHashCode</code>).</p>
<p>If <a href="../../search/WebImage/operator_equals.html">/sdk-for-flutter-explore-search-webimage-operator-equals</a> is overridden to use the object state instead,
the hash code must also be changed to represent that state,
otherwise the object cannot be used in hash based data structures
like the default <code>Set</code> and <code>Map</code> implementations.</p>
<p>Hash codes must be the same for objects that are equal to each other
according to <a href="../../search/WebImage/operator_equals.html">/sdk-for-flutter-explore-search-webimage-operator-equals</a>.
The hash code of an object should only change if the object changes
in a way that affects equality.
There are no further requirements for the hash codes.
They need not be consistent between executions of the same program
and there are no distribution guarantees.</p>
<p>Objects that are not equal are allowed to have the same hash code.
It is even technically allowed that all instances have the same hash code,
but if clashes happen too often,
it may reduce the efficiency of hash-based data structures
like <code>HashSet</code> or <code>HashMap</code>.</p>
<p>If a subclass overrides <a href="../../search/WebImage/hashCode.html">/sdk-for-flutter-explore-search-webimage-hashcode</a>, it should override the
<a href="../../search/WebImage/operator_equals.html">/sdk-for-flutter-explore-search-webimage-operator-equals</a> operator as well to maintain consistency.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@override
int get hashCode {
  int result = 7;
  result = 31 * result + source.hashCode;
  return result;
}</code></pre>
</section>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li><a href="../../search/WebImage-class.html">/sdk-for-flutter-explore-search-webimage-class</a></li>
<li class="self-crumb">hashCode property</li>
</ol>
<h5>WebImage class</h5>
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
