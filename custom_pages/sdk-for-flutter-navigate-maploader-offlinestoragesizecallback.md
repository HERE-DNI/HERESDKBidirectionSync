---
title: "Untitled"
slug: "sdk-for-flutter-navigate-maploader-offlinestoragesizecallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- OfflineStorageSizeCallback.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li class="self-crumb">OfflineStorageSizeCallback typedef</li>
</ol>
<div class="self-name">OfflineStorageSizeCallback</div>
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
<h1>OfflineStorageSizeCallback typedef</h1></div>
<section class="multi-line-signature">
OfflineStorageSizeCallback =
     void Function(/sdk-for-flutter-navigate-maploader-maploadererror? error, int? size)
</section>
<section class="desc markdown">
<p>A method which is called on the main thread when /sdk-for-flutter-navigate-maploader-mapdownloader-getofflinemapsstoragesizeinbytesasync has been completed.</p>
<p>The first argument indicates an error in case of a failure. The second argument contains the results.
Both arguments cannot be <code>null</code> at the same time - or not <code>null</code> at the same time.</p>
<ul>
<li>
<p><code>error</code> Represents an error in case of a failure. It is <code>null</code> for an operation that succeeds.</p>
</li>
<li>
<p><code>size</code> The size of  offline map. It is <code>null</code> in case of an error.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef OfflineStorageSizeCallback = void Function(MapLoaderError? error, int? size);</code></pre>
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
<li class="self-crumb">OfflineStorageSizeCallback typedef</li>
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
