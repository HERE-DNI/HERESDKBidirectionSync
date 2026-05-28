---
title: "getInitialPersistentMapStatus abstract method"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-getinitialpersistentmapstatus"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getInitialPersistentMapStatus.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-mapdownloader-class</li>
<li class="self-crumb">getInitialPersistentMapStatus abstract method</li>
</ol>
<div class="self-name">getInitialPersistentMapStatus</div>
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
<div class="main-content" data-above-sidebar="maploader/MapDownloader-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>getInitialPersistentMapStatus abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-maploader-persistentmapstatus
getInitialPersistentMapStatus(<wbr/>)

      

    </section>
<section class="desc markdown">
<p>Gets the initial status of the already downloaded regions at start-up time of the app.</p>
<p>It is not recommended to download or to upload map data while an app is running in
background. However, it can happen, that an app gets shut down during an ongoing
operation, for example, due to a crash. In such a case, some or all of the downloaded map data
may be in a corrupted state.
Refer to the /sdk-for-flutter-navigate-maploader-persistentmapstatus for exact healing procedure for specific
status.
Note: This value will not change during the lifetime of an app.</p>
<p>Returns /sdk-for-flutter-navigate-maploader-persistentmapstatus. Initial status of the persistent map.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">PersistentMapStatus getInitialPersistentMapStatus();</code></pre>
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
<li>/sdk-for-flutter-navigate-maploader-mapdownloader-class</li>
<li class="self-crumb">getInitialPersistentMapStatus abstract method</li>
</ol>
<h5>MapDownloader class</h5>
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
