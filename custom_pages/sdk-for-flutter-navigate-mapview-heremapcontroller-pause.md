---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-heremapcontroller-pause"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- pause.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-heremapcontroller-class</li>
<li class="self-crumb">pause abstract method</li>
</ol>
<div class="self-name">pause</div>
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
<div class="main-content" data-above-sidebar="mapview/HereMapController-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>pause abstract method</h1></div>
<section class="multi-line-signature">
void
pause(<wbr/>)

      

    </section>
<section class="desc markdown">
<p>Pauses the map widget.</p>
<p>A paused map widget stops rendering updates until it gets resumed. It is recommended to not schedule
any map updates while in the paused state as they are cached in-memory and will pile-up until the
map widget gets resumed.</p>
<p>By default, the map widget gets automatically paused and resumed based on platform specific
events (e.g. client application going into background/foreground). Once this method gets called,
the automatic behavior gets disabled.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void pause();</code></pre>
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
<li>/sdk-for-flutter-navigate-mapview-heremapcontroller-class</li>
<li class="self-crumb">pause abstract method</li>
</ol>
<h5>HereMapController class</h5>
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
