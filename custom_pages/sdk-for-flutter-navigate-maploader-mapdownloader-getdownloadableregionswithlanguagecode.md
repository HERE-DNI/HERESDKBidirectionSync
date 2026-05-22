---
title: "Untitled"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-getdownloadableregionswithlanguagecode"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getDownloadableRegionsWithLanguageCode.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-mapdownloader-class</li>
<li class="self-crumb">getDownloadableRegionsWithLanguageCode abstract method</li>
</ol>
<div class="self-name">getDownloadableRegionsWithLanguageCode</div>
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
<h1>getDownloadableRegionsWithLanguageCode abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-core-threading-taskhandle-class
getDownloadableRegionsWithLanguageCode(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-languagecode languageCode, </li>
<li>/sdk-for-flutter-navigate-maploader-downloadableregionscallback callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Performs an asynchronous request to fetch a list of /sdk-for-flutter-navigate-maploader-region-class objects with /sdk-for-flutter-navigate-maploader-region-name
in given <code>MapDownloader.getDownloadableRegionsWithLanguageCode.languageCode</code>, that can be used to download the actual map data in a separate request.</p>
<ul>
<li>
<p><code>languageCode</code> The language code determines the language of /sdk-for-flutter-navigate-maploader-region-name.</p>
</li>
<li>
<p><code>callback</code> Callback which receives the result on the main thread.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-core-threading-taskhandle-class. Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle getDownloadableRegionsWithLanguageCode(LanguageCode languageCode, DownloadableRegionsCallback callback);</code></pre>
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
<li class="self-crumb">getDownloadableRegionsWithLanguageCode abstract method</li>
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



</div>
`
}</HTMLBlock>
