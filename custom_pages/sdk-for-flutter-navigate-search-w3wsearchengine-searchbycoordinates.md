---
title: "searchByCoordinates abstract method"
slug: "sdk-for-flutter-navigate-search-w3wsearchengine-searchbycoordinates"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- searchByCoordinates.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li>/sdk-for-flutter-navigate-search-w3wsearchengine-class</li>
<li class="self-crumb">searchByCoordinates abstract method</li>
</ol>
<div class="self-name">searchByCoordinates</div>
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
<div class="main-content" data-above-sidebar="search/W3WSearchEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>searchByCoordinates abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-core-threading-taskhandle-class
searchByCoordinates(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-geocoordinates-class coordinates, </li>
<li>String? language, </li>
<li>/sdk-for-flutter-navigate-search-w3wsearchcallback callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Performs an asynchronous request to search for a /sdk-for-flutter-navigate-search-w3wsquare-class, which includes
the 3 word address, that corresponds to the given coordinates.</p>
<ul>
<li>
<p><code>coordinates</code> The coordinates where to search.</p>
</li>
<li>
<p><code>language</code> A supported 3 word address language as an ISO 639-1 2 letter code.
For Bosnian-Croatian-Montenegrin-Serbian use "oo". Defaults to "en" (English).</p>
</li>
<li>
<p><code>callback</code> Callback which receives the result on the main thread.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-core-threading-taskhandle-class. Handle that can be used to manipulate the execution of the task.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle searchByCoordinates(GeoCoordinates coordinates, String? language, W3WSearchCallback callback);</code></pre>
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
<li>/sdk-for-flutter-navigate-search-w3wsearchengine-class</li>
<li class="self-crumb">searchByCoordinates abstract method</li>
</ol>
<h5>W3WSearchEngine class</h5>
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
