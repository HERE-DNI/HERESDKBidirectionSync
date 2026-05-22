---
title: "Untitled"
slug: "sdk-for-flutter-navigate-maploader-mapdownloaderconstructioncallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapDownloaderConstructionCallback.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li class="self-crumb">MapDownloaderConstructionCallback typedef</li>
</ol>
<div class="self-name">MapDownloaderConstructionCallback</div>
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
<div class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MapDownloaderConstructionCallback typedef</h1></div>
<section class="multi-line-signature">
MapDownloaderConstructionCallback =
     void Function(/sdk-for-flutter-navigate-maploader-mapdownloader-class mapDownloader)
</section>
<section class="desc markdown">
<p>A method which is called on the main thread when /sdk-for-flutter-navigate-maploader-mapdownloader-fromsdkengineasync has been completed.</p>
<p>The <code>MapDownloader</code> instance is created on a background thread to not block the calling
thread.</p>
<p>During construction an online connection is established to fetch configuration data for
internal use. If no online connection is available, cached or default values will be used.
This is only for internal reasons and has no effect on the operability of the resulting
instance. When configuration data is available from the cache, construction can still take
a reasonable amount of time. Applications should consider to show a loading indicator.</p>
<ul>
<li><code>mapDownloader</code> Represents a constructed MapDownloader object.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef MapDownloaderConstructionCallback = void Function(MapDownloader mapDownloader);</code></pre>
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
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li class="self-crumb">MapDownloaderConstructionCallback typedef</li>
</ol>
<h5>maploader library</h5>
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
