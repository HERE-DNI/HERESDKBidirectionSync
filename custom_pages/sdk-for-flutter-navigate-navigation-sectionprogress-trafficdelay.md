---
title: "trafficDelay property"
slug: "sdk-for-flutter-navigate-navigation-sectionprogress-trafficdelay"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- trafficDelay.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-sectionprogress-class</li>
<li class="self-crumb">trafficDelay property</li>
</ol>
<div class="self-name">trafficDelay</div>
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
<div class="main-content" data-above-sidebar="navigation/SectionProgress-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>trafficDelay property</h1></div>
<section class="multi-line-signature">
        
        Duration
        trafficDelay
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>The estimated traffic delay in seconds from current location until the end of the
/sdk-for-flutter-navigate-routing-section-class is reached.
Note that the value is accumulated per section, and that the last section contains the overall
traffic delay until the destination is reached. The delay might be a negative value:
Negative values indicate that the part of this section can be traversed faster than usual.
Note that this is based on a delay value received at the moment of route calculation.
Defaults to 0 seconds.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Duration trafficDelay;</code></pre>
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
<li>/sdk-for-flutter-navigate-navigation-sectionprogress-class</li>
<li class="self-crumb">trafficDelay property</li>
</ol>
<h5>SectionProgress class</h5>
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
