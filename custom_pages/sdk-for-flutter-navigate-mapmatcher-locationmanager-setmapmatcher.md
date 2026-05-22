---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapmatcher-locationmanager-setmapmatcher"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setMapMatcher.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapmatcher-mapmatcher-library</li>
<li>/sdk-for-flutter-navigate-mapmatcher-locationmanager-class</li>
<li class="self-crumb">setMapMatcher abstract method</li>
</ol>
<div class="self-name">setMapMatcher</div>
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
<div class="main-content" data-above-sidebar="mapmatcher/LocationManager-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>setMapMatcher abstract method</h1></div>
<section class="multi-line-signature">
void
setMapMatcher(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-mapmatcher-mapmatcher-class? mapMatcher</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Sets the /sdk-for-flutter-navigate-mapmatcher-mapmatcher-class for exclusive use by /sdk-for-flutter-navigate-mapmatcher-locationmanager-class.</p>
<p><strong>Threading:</strong> This method is asynchronous and performs the switch in an internal thread of /sdk-for-flutter-navigate-mapmatcher-locationmanager-class.
<strong>Note:</strong> After calling this method, the /sdk-for-flutter-navigate-mapmatcher-mapmatcher-class is owned and used exclusively
by /sdk-for-flutter-navigate-mapmatcher-locationmanager-class in its internal processing thread.
Do not use or access the /sdk-for-flutter-navigate-mapmatcher-mapmatcher-class elsewhere while it is set.</p>
<ul>
<li><code>mapMatcher</code> The /sdk-for-flutter-navigate-mapmatcher-mapmatcher-class instance to be used exclusively by /sdk-for-flutter-navigate-mapmatcher-locationmanager-class.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setMapMatcher(MapMatcher? mapMatcher);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapmatcher-mapmatcher-library</li>
<li>/sdk-for-flutter-navigate-mapmatcher-locationmanager-class</li>
<li class="self-crumb">setMapMatcher abstract method</li>
</ol>
<h5>LocationManager class</h5>
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
