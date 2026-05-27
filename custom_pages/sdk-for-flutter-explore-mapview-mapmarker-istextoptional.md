---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-mapmarker-istextoptional"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- isTextOptional.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapMarker-class.html">/sdk-for-flutter-explore-mapview-mapmarker-class</a></li>
<li class="self-crumb">isTextOptional property</li>
</ol>
<div class="self-name">isTextOptional</div>
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
<div class="main-content" data-above-sidebar="mapview/MapMarker-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>isTextOptional property</h1></div>
<section id="getter">
<section class="multi-line-signature">
bool
isTextOptional
</section>
<section class="desc markdown">
<p>Determines if the marker can be displayed with icon and without text.
Returns <code>true</code> if the marker allows text to be hidden, <code>false</code> otherwise.
Defaults to <code>false</code>.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool get isTextOptional;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
isTextOptional=(<wbr/>bool value)
</section>
<section class="desc markdown">
<p>Determines if the marker can be displayed with icon and without text.
Sets whether the marker is allowed to appear without text.</p>
<p>Controls whenever <code>MapMarker</code> can be shown as icon only when <a href="../../mapview/MapMarker/isOverlapAllowed.html">/sdk-for-flutter-explore-mapview-mapmarker-isoverlapallowed</a>
is <code>false</code>, has no effect otherwise. If <code>false</code> then the <code>MapMarker</code> will not appear
when icon or text are blocked by other labels.
If <code>true</code>, icon will appear even if the text part is blocked by other labels.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set isTextOptional(bool value);</code></pre>
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
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapMarker-class.html">/sdk-for-flutter-explore-mapview-mapmarker-class</a></li>
<li class="self-crumb">isTextOptional property</li>
</ol>
<h5>MapMarker class</h5>
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
