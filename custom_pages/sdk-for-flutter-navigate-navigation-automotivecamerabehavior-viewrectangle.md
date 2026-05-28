---
title: "viewRectangle property"
slug: "sdk-for-flutter-navigate-navigation-automotivecamerabehavior-viewrectangle"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- viewRectangle.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-automotivecamerabehavior-class</li>
<li class="self-crumb">viewRectangle property</li>
</ol>
<div class="self-name">viewRectangle</div>
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
<div class="main-content" data-above-sidebar="navigation/AutomotiveCameraBehavior-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>viewRectangle property</h1></div>
<section id="getter">
<section class="multi-line-signature">
/sdk-for-flutter-navigate-core-rectangle2d-class?
viewRectangle
</section>
<section class="desc markdown">
<p>The view rectangle for camera updates.
Defines a sub-space of the screen that the behavior should consider
for camera updates. This property is forwarded to both the tracking and area cameras,
ensuring consistent viewport constraints across all camera modes.
If not set, it uses the viewport bounds of the underlying map view.
Gets the current view rectangle, if it's set.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Rectangle2D? get viewRectangle;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
viewRectangle=(<wbr/>/sdk-for-flutter-navigate-core-rectangle2d-class? value)
</section>
<section class="desc markdown">
<p>The view rectangle for camera updates.
Defines a sub-space of the screen that the behavior should consider
for camera updates. This property is forwarded to both the tracking and area cameras,
ensuring consistent viewport constraints across all camera modes.
If not set, it uses the viewport bounds of the underlying map view.
Sets a view rectangle for both child cameras.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set viewRectangle(Rectangle2D? value);</code></pre>
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-automotivecamerabehavior-class</li>
<li class="self-crumb">viewRectangle property</li>
</ol>
<h5>AutomotiveCameraBehavior class</h5>
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
