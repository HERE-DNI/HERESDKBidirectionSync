---
title: "AngleRange constructor"
slug: "sdk-for-flutter-navigate-core-anglerange-anglerange"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- AngleRange.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li>/sdk-for-flutter-navigate-core-anglerange-class</li>
<li class="self-crumb">AngleRange factory constructor</li>
</ol>
<div class="self-name">AngleRange</div>
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
<div class="main-content" data-above-sidebar="core/AngleRange-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>AngleRange constructor</h1></div>
<section class="multi-line-signature">
AngleRange(<wbr/><ol class="parameter-list single-line"> <li>double start, </li>
<li>double extent</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Constructs an AngleRange from the provided start and extent angles.</p>
<p>Corrects values if they exceed the ranges.</p>
<ul>
<li>
<p><code>start</code> Start angle, running clockwise, in degrees from north.
The value will be normalized to [0.0, 360.0).</p>
</li>
<li>
<p><code>extent</code> The range's extent, running clockwise, in degrees from start.
The value will be clamped to the range of [0, 360] degrees.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory AngleRange(double start, double extent) =&gt; $prototype.$init(start, extent);</code></pre>
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
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li>/sdk-for-flutter-navigate-core-anglerange-class</li>
<li class="self-crumb">AngleRange factory constructor</li>
</ol>
<h5>AngleRange class</h5>
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
