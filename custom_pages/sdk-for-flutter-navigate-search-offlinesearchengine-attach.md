---
title: "Untitled"
slug: "sdk-for-flutter-navigate-search-offlinesearchengine-attach"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- attach.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li>/sdk-for-flutter-navigate-search-offlinesearchengine-class</li>
<li class="self-crumb">attach abstract method</li>
</ol>
<div class="self-name">attach</div>
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
<div class="main-content" data-above-sidebar="search/OfflineSearchEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>attach abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-core-threading-taskhandle-class
attach(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-search-myplaces-class dataSource, </li>
<li>/sdk-for-flutter-navigate-core-threading-ontaskcompleted callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Attach data source into SearchEngine instance.</p>
<p>Places from MyPlaces ranked the same
way as places from default source.
New data source replaces old one.
Note: Only OfflineSearchEngine supports search over MyPlaces.</p>
<ul>
<li>
<p><code>dataSource</code> The data source.</p>
</li>
<li>
<p><code>callback</code> The callback to be called when task is completed.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-core-threading-taskhandle-class. Handle that will be used to manipulate the execution of the task.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle attach(MyPlaces dataSource, OnTaskCompleted callback);</code></pre>
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
<li>/sdk-for-flutter-navigate-search-offlinesearchengine-class</li>
<li class="self-crumb">attach abstract method</li>
</ol>
<h5>OfflineSearchEngine class</h5>
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
