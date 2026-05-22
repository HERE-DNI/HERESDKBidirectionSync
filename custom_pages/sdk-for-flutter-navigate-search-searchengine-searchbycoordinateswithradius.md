---
title: "Untitled"
slug: "sdk-for-flutter-navigate-search-searchengine-searchbycoordinateswithradius"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- searchByCoordinatesWithRadius.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li>/sdk-for-flutter-navigate-search-searchengine-class</li>
<li class="self-crumb">searchByCoordinatesWithRadius abstract method</li>
</ol>
<div class="self-name">searchByCoordinatesWithRadius</div>
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
<div class="main-content" data-above-sidebar="search/SearchEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>searchByCoordinatesWithRadius abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-core-threading-taskhandle-class
searchByCoordinatesWithRadius(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-geocircle-class circle, </li>
<li>/sdk-for-flutter-navigate-search-searchoptions-class options, </li>
<li>/sdk-for-flutter-navigate-search-searchcallback callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Performs an asynchronous request to search for places based on given circular spatial filter.</p>
<p>This is the same process as reverse geocoding, except that more data is returned
than just the /sdk-for-flutter-navigate-search-address-class that belongs to given coordinates. Note that coordinates
can belong to more than one /sdk-for-flutter-navigate-search-place-class result.
Provides candidate places sorted by relevance and located inside the radius of filter.</p>
<ul>
<li>
<p><code>circle</code> The coordinates where to search and radius of the circular spatial filter.
Passed in form of /sdk-for-flutter-navigate-core-geocircle-class.</p>
</li>
<li>
<p><code>options</code> Search options.</p>
</li>
<li>
<p><code>callback</code> Callback which receives result on the main thread.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-core-threading-taskhandle-class. Handle that will be used to manipulate execution of the task.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle searchByCoordinatesWithRadius(GeoCircle circle, SearchOptions options, SearchCallback callback);</code></pre>
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
<li>/sdk-for-flutter-navigate-search-searchengine-class</li>
<li class="self-crumb">searchByCoordinatesWithRadius abstract method</li>
</ol>
<h5>SearchEngine class</h5>
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
